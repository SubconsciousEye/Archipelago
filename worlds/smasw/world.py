import os
import threading
import typing

import settings
import pkgutil
from collections.abc import Mapping

from BaseClasses import MultiWorld, CollectionState
# Imports of base Archipelago modules must be absolute.
from worlds.AutoWorld import World

# Imports of your world's files must be relative.
from . import items, locations, regions, rules, web_world, pregen
from .items import all_items, item_groups
from .locations import all_locations
from . import options as smasw_options  # rename due to a name conflict with World.options
from .rom import SMASWProcedurePatch, SMASWHASH, patch_rom



class SMASWSettings(settings.Group):
    class RomFile(settings.SNESRomPath):
        """File name of the SMAS+SMW rom"""
        description = "Super Mario All-Stars + Super Mario World ROM File"
        copy_to = "Super Mario All-Stars + Super Mario World (USA).sfc"
        md5s = [SMASWHASH]

    #class ExperimentalFastROM(str):
    #    """
    #    If true, enables FastROM for the game, which can speed up SNES Code processing.
    #    WARNING: Experimental! May cause more bugs and issues not found on SlowROM Speed!
    #    """

    rom_file: RomFile = RomFile(RomFile.copy_to)
    #fastrom: typing.Union[ExperimentalFastROM, bool] = False

# SMASW will go through all the parts of the world api one step at a time,
# with many examples and comments across multiple files.
# If you'd rather read one continuous document, or just like reading multiple sources,
# we also have this document specifying the entire world api:
# https://github.com/ArchipelagoMW/Archipelago/blob/main/docs/world%20api.md


# The world class is the heart and soul of an apworld implementation.
# It holds all the data and functions required to build the world and submit it to the multiworld generator.
# You could have all your world code in just this one class, but for readability and better structure,
# it is common to split up world functionality into multiple files.
# This implementation in particular has the following additional files, each covering one topic:
# regions.py, locations.py, rules.py, items.py, options.py and web_world.py.
# It is recommended that you read these in that specific order, then come back to the world class.
class SMASWWorld(World):
    """
    Mario and Friends have challenged you to play through his Super Collection of games. The catch? Your Abilities
    are stripped away, and some Games are locked away across Worlds.
    Play through Super Mario Bros. 1, Super Mario Bros. 2, Super Mario Bros. 3, Super Mario Bros: The Lost Levels,
    or Super Mario World to complete this Super Challenge!
    Can you prove your worth as a Super Player?
    """

    # The docstring should contain a description of the game, to be displayed on the WebHost.

    # You must override the "game" field to say the name of the game.
    game = "Super Mario All-Stars + Super Mario World"

    # The WebWorld is a definition class that governs how this world will be displayed on the website.
    web = web_world.SMASWWebWorld()
    
    # Disable Universal Tracker (Not currently supported)
    disable_ut = True

    settings: typing.ClassVar[SMASWSettings]
    settings_key = "smasw_options"
    # This is how we associate the options defined in our options.py with our world.
    # (Note: options.py has been imported as "smasw_options" at the top of this file to avoid a name conflict)
    options_dataclass = smasw_options.SMASWOptions
    options: smasw_options.SMASWOptions  # Common mistake: This has to be a colon (:), not an equals sign (=).

    # Our world class must have a static location_name_to_id and item_name_to_id defined.
    # We define these in regions.py and items.py respectively, so we just set them here.
    item_name_to_id = {name: data.idcode for name, data in all_items.items()}
    location_name_to_id = all_locations
    item_name_groups = item_groups
    #location_name_groups = location_groups #TODO

    # There is always one region that the generator starts from & assumes you can always go back to.
    # This defaults to "Menu", but you can change it by overriding origin_region_name.
    origin_region_name = "Game Select"
    ## Debug
    #topology_present = True

    # Grabbed from Kirby Super Star
    def __init__(self, multiworld: MultiWorld, player: int):
        super().__init__(multiworld, player)
        self.rom_name: bytearray = bytearray()
        self.rom_name_available_event = threading.Event()

    # Our world class must have certain functions ("steps") that get called during generation.

    # Defining "Generate Early" to fix up some options
    def generate_early(self) -> None:
        pregen.fix_options(self)
    
    
    # The main ones are: create_regions, set_rules, create_items.
    # For better structure and readability, we put each of these in their own file.
    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)
        
        ## Debug
        #from Utils import visualize_regions
        #state = CollectionState(self.multiworld)
        #state.update_reachable_regions(self.player)
        #visualize_regions(self.get_region("Game Select"), "my_world.puml", show_entrance_names=True,
        #                regions_to_highlight=state.reachable_regions[self.player])

    def create_items(self) -> None:
        items.create_all_items(self)

    # Our world class must also have a create_item function that can create any one of our items by name at any time.
    # We also put this in a different file, the same one that create_items is in.
    def create_item(self, name: str) -> items.SMASWItem:
        return items.create_item_with_correct_classification(self, name)

    # For features such as item links and panic-method start inventory, AP may ask your world to create extra filler.
    # The way it does this is by calling get_filler_item_name.
    # For this purpose, your world *must* have at least one infinitely repeatable item (usually filler).
    # You must override this function and return this infinitely repeatable item's name.
    # In our case, we defined a function called get_random_filler_item_name for this purpose in our items.py.
    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)

    # Borrowed base from Spicy Mycena Waffles APWorld
    def generate_output(self, output_directory: str):
        try:
            patch = SMASWProcedurePatch(player=self.player, player_name=self.multiworld.player_name[self.player])
            patch_rom(self, patch)

            self.rom_name = patch.name

            patch.write(os.path.join(output_directory,
                                     f"{self.multiworld.get_out_file_name_base(self.player)}{patch.patch_file_ending}"))
            patch.write()
        except:
            raise
        finally:
            self.rom_name_available_event.set()  # make sure threading continues and errors are collected

    # multidata base from various SNES APWorlds
    def modify_multidata(self, multidata: dict):
        import base64
        # wait for self.rom_name to be available.
        self.rom_name_available_event.wait()
        rom_name = getattr(self, "rom_name", None)
        # we skip in case of error, so that the original error in the output thread is the one that gets raised
        if rom_name:
            new_name = base64.b64encode(bytes(self.rom_name)).decode()
            multidata["connect_names"][new_name] = multidata["connect_names"][self.multiworld.player_name[self.player]]

    ## There may be data that the game client will need to modify the behavior of the game.
    ## This is what slot_data exists for. Upon every client connection, the slot's slot_data is sent to the client.
    ## slot_data is just a dictionary using basic types, that will be converted to json when sent to the client.
    #def fill_slot_data(self) -> Mapping[str, Any]:
    #    # If you need access to the player's chosen options on the client side, there is a helper for that.
    #    return self.options.as_dict(
    #        "hard_mode", "hammer", "extra_starting_chest", "confetti_explosiveness", "player_sprite"
    #    )
