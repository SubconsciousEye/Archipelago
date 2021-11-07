from ..AutoWorld import World
from ..generic.Rules import set_rule, add_item_rule
from BaseClasses import Region, Location, Entrance, Item
from Utils import get_options, output_path
import typing
import lzma
import os
import threading

try:
    import pyevermizer  # from package
except ImportError:
    import traceback
    traceback.print_exc()
    from . import pyevermizer  # as part of the source tree

from . import Logic  # load logic mixin
from .Options import soe_options
from .Patch import generate_patch

"""
In evermizer:

Items are uniquely defined by a pair of (type, id).
For most items this is their vanilla location (i.e. CHECK_GOURD, number).

Items have `provides`, which give the actual progression
instead of providing multiple events per item, we iterate through them in Logic.py
    e.g. Found any weapon

Locations have `requires` and `provides`.
Requirements have to be converted to (access) rules for AP
    e.g. Chest locked behind having a weapon
Provides could be events, but instead we iterate through the entire logic in Logic.py
    e.g. NPC available after fighting a Boss

Rules are special locations that don't have a physical location
instead of implementing virtual locations and virtual items, we simply use them  in Logic.py
    e.g. 2DEs+Wheel+Gauge = Rocket

Rules and Locations live on the same logic tree returned by pyevermizer.get_logic()

TODO: for balancing we may want to generate Regions (with Entrances) for some
common rules, place the locations in those Regions and shorten the rules.
"""

_id_base = 64000
_id_offset: typing.Dict[int, int] = {
    pyevermizer.CHECK_ALCHEMY: _id_base + 0,  # alchemy 64000..64049
    pyevermizer.CHECK_BOSS: _id_base + 50,  # bosses 64050..6499
    pyevermizer.CHECK_GOURD: _id_base + 100,  # gourds 64100..64399
    pyevermizer.CHECK_NPC: _id_base + 400,  # npc 64400..64499
    # TODO: sniff 64500..64799
}

# cache native evermizer items and locations
_items = pyevermizer.get_items()
_locations = pyevermizer.get_locations()
# fix up texts for AP
for _loc in _locations:
    if _loc.type == pyevermizer.CHECK_GOURD:
        _loc.name = f'{_loc.name} #{_loc.index}'


def _get_location_mapping() -> typing.Tuple[typing.Dict[str, int], typing.Dict[int, pyevermizer.Location]]:
    name_to_id = {}
    id_to_raw = {}
    for loc in _locations:
        apid = _id_offset[loc.type] + loc.index
        id_to_raw[apid] = loc
        name_to_id[loc.name] = apid
    name_to_id['Done'] = None
    return name_to_id, id_to_raw


def _get_item_mapping() -> typing.Tuple[typing.Dict[str, int], typing.Dict[int, pyevermizer.Item]]:
    name_to_id = {}
    id_to_raw = {}
    for item in _items:
        if item.name in name_to_id:
            continue
        apid = _id_offset[item.type] + item.index
        id_to_raw[apid] = item
        name_to_id[item.name] = apid
    name_to_id['Victory'] = None
    return name_to_id, id_to_raw


class SoEWorld(World):
    """
    Secret of Evermore is a SNES action RPG. You learn alchemy spells, fight bosses and gather rocket parts to visit a
    space station where the final boss must be defeated. 
    """
    game: str = "Secret of Evermore"
    options = soe_options
    topology_present: bool = True
    remote_items: bool = False  # True only for testing
    data_version = 0

    item_name_to_id, item_id_to_raw = _get_item_mapping()
    location_name_to_id, location_id_to_raw = _get_location_mapping()

    evermizer_seed: int
    restrict_item_placement: bool = False  # placeholder to force certain item types to certain pools
    connect_name: str

    def __init__(self, *args, **kwargs):
        self.connect_name_available_event = threading.Event()
        super(SoEWorld, self).__init__(*args, **kwargs)

    def create_event(self, event: str) -> Item:
        progression = True
        return SoEItem(event, progression, None, self.player)

    def create_item(self, item: typing.Union[pyevermizer.Item, str], force_progression: bool = False) -> Item:
        if type(item) is str:
            item = self.item_id_to_raw[self.item_name_to_id[item]]
        return SoEItem(item.name, force_progression or item.progression, self.item_name_to_id[item.name], self.player)

    def create_regions(self):
        # TODO: generate *some* regions from locations' requirements?
        r = Region('Menu', None, 'Menu', self.player, self.world)
        r.exits = [Entrance(self.player, 'New Game', r)]
        self.world.regions += [r]

        r = Region('Ingame', None, 'Ingame', self.player, self.world)
        r.locations = [SoELocation(self.player, loc.name, self.location_name_to_id[loc.name], r)
                       for loc in _locations]
        r.locations.append(SoELocation(self.player, 'Done', None, r))
        self.world.regions += [r]

        self.world.get_entrance('New Game', self.player).connect(self.world.get_region('Ingame', self.player))

    def create_items(self):
        # clear precollected items since we don't support them yet
        if type(self.world.precollected_items) is dict:
            self.world.precollected_items[self.player] = []
        # add items to the pool
        self.world.itempool += [item for item in
                                map(lambda item: self.create_item(item, self.restrict_item_placement), _items)]

    def set_rules(self):
        self.world.completion_condition[self.player] = lambda state: state.has('Victory', self.player)
        # set Done from goal option once we have multiple goals
        set_rule(self.world.get_location('Done', self.player),
                 lambda state: state._soe_has(pyevermizer.P_FINAL_BOSS, self.world, self.player))
        set_rule(self.world.get_entrance('New Game', self.player), lambda state: True)
        for loc in _locations:
            location = self.world.get_location(loc.name, self.player)
            set_rule(location, self.make_rule(loc.requires))
            # limit location pool by item type
            if self.restrict_item_placement:
                add_item_rule(location, self.make_item_type_limit_rule(loc.type))

    def make_rule(self, requires: typing.List[typing.Tuple[int]]) -> typing.Callable[[typing.Any], bool]:
        def rule(state) -> bool:
            for count, progress in requires:
                if not state._soe_has(progress, self.world, self.player, count):
                    return False
            return True

        return rule

    def make_item_type_limit_rule(self, item_type: int):
        return lambda item: item.player != self.player or self.item_id_to_raw[item.code].type == item_type

    def generate_basic(self):
        # place Victory event
        self.world.get_location('Done', self.player).place_locked_item(self.create_event('Victory'))
        # generate stuff for later
        self.evermizer_seed = self.world.random.randint(0, 2**16-1)  # TODO: make this an option for "full" plando?

    def post_fill(self):
        # fix up the advancement property of items so they are displayed correctly in other games
        if self.restrict_item_placement:
            for location in self.world.get_locations():
                item = location.item
                if item.code and item.player == self.player and not self.item_id_to_raw[location.item.code].progression:
                    item.advancement = False

    def generate_output(self, output_directory: str):
        player_name = self.world.get_player_name(self.player)
        self.connect_name = player_name[:32]
        while len(self.connect_name.encode('utf-8')) > 32:
            self.connect_name = self.connect_name[:-1]
        self.connect_name_available_event.set()
        placement_file = None
        out_file = None
        try:
            money = self.world.money_modifier[self.player].value
            exp = self.world.exp_modifier[self.player].value
            rom_file = get_options()['soe_options']['rom_file']
            out_base = output_path(output_directory, f'AP_{self.world.seed_name}_P{self.player}_{player_name}')
            out_file = out_base + '.sfc'
            placement_file = out_base + '.txt'
            patch_file = out_base + '.apsoe'
            flags = 'l'  # spoiler log
            for option_name in self.options:
                option = getattr(self.world, option_name)[self.player]
                if hasattr(option, 'to_flag'):
                    flags += option.to_flag()

            with open(placement_file, "wb") as f:  # generate placement file
                for location in filter(lambda l: l.player == self.player, self.world.get_locations()):
                    item = location.item
                    if item.code is None:
                        continue  # skip events
                    loc = self.location_id_to_raw[location.address]
                    if item.player != self.player:
                        line = f'{loc.type},{loc.index}:{pyevermizer.CHECK_NONE},{item.code},{item.player}\n'
                    else:
                        item = self.item_id_to_raw[item.code]
                        line = f'{loc.type},{loc.index}:{item.type},{item.index}\n'
                    f.write(line.encode('utf-8'))

            if (pyevermizer.main(rom_file, out_file, placement_file, self.world.seed_name, self.connect_name, self.evermizer_seed,
                                 flags, money, exp)):
                raise RuntimeError()
            with lzma.LZMAFile(patch_file, 'wb') as f:
                f.write(generate_patch(rom_file, out_file))
        except:
            raise
        finally:
            try:
                os.unlink(placement_file)
                os.unlink(out_file)
                os.unlink(out_file[:-4]+'_SPOILER.log')
            except:
                pass

    def modify_multidata(self, multidata: dict):
        # wait for self.connect_name to be available.
        self.connect_name_available_event.wait()
        # we skip in case of error, so that the original error in the output thread is the one that gets raised
        if self.connect_name and self.connect_name != self.world.player_name[self.player]:
            payload = multidata["connect_names"][self.world.player_name[self.player]]
            multidata["connect_names"][self.connect_name] = payload
            del (multidata["connect_names"][self.world.player_name[self.player]])


class SoEItem(Item):
    game: str = "Secret of Evermore"


class SoELocation(Location):
    game: str = "Secret of Evermore"

    def __init__(self, player: int, name: str, address: typing.Optional[int], parent):
        super().__init__(player, name, address, parent)
        self.event = not address
