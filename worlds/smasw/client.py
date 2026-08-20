import logging
import struct
import textwrap
import typing
import time
from struct import pack
from enum import Enum

# File takes reference from Donkey Kong Country 2 APWorld and Tetris Attack APWorld
# Also sometimes from Kirby Super Star and Spicy Mycena Waffles
# It's a bit frakensteined though.

from NetUtils import ClientStatus, color
from worlds.AutoSNIClient import SNIClient, SnesReader, SnesData, Read
from .items import BASE_OFFSET as ITEM_ID_OFFSET
from .locations import BASE_OFFSET_SRAM as SRAM_OFFSET_LOCS
from .locations import BASE_OFFSET_NORMAL as SRAM_OFFSET_NORMAL

from typing import TYPE_CHECKING

if typing.TYPE_CHECKING:
    from SNIClient import SNIContext

snes_logger = logging.getLogger("SNES")

# FXPAK Pro protocol memory mapping used by SNI
ROM_START = 0x000000
WRAM_START = 0xF50000
WRAM_SIZE = 0x20000
SRAM_START = 0xE00000

# Connection/Initialization
SMASW_ROMHASH_START = ROM_START + 0x7FC0
ROMHASH_SIZE = 0x15
SMASW_SRAM_VALID_0 = SRAM_START + 0x0002  # Must be 0x9743
SMASW_SRAM_VALID_1 = SRAM_START + 0x1FFC  # Must be 0x5321

# SNI Protocol Stuff
SMASW_SNI_COMMAND = WRAM_START + 0x0175
#SMASW_SNI_PROTECTION = SRAM_START + 0x1F10 # NOTE: Old
SMASW_SNI_PROTECTION = WRAM_START + 0x0156
#SMASW_SNI_RESYNC = SRAM_START + 0x0600 # TODO: Find a good spot to place this

# Regular SMASW Stuff
SMASW_RECV_INDEX = SRAM_START + 0x0400
SMASW_SRAM_CHECKS_NORMAL = SRAM_START + 0x1000
#SMASW_SRAM_CHECKS_SANITY = SRAM_START + 0x2000 # TODO: Expand SRAM?
SMASW_SRAM_GOAL = SRAM_START + 0x1F01
# SRAM + 0x0800-0x0801 = SMB1 Boss Coins
# SRAM + 0x0802-0x0803 = SMBLL Boss Coins
# SRAM + 0x0804        = SMB2 Boss Coins
# SRAM + 0x0805        = SMB3 Boss Coins
# SRAM + 0x0806-0x0807 = SMW Boss Coins
# SRAM + 0x0810-0x0811 = SubGame Goals
# SRAM + 0x1F00 = Game Goals
# old:
# SRAM + 0x1EF0-0x1EF1 = SMB1 Boss Coins
# SRAM + 0x1EF2-0x1EF3 = SMBLL Boss Coins
# SRAM + 0x1EF4        = SMB2 Boss Coins
# SRAM + 0x1EF5        = SMB3 Boss Coins
# SRAM + 0x1EF6-0x1EF7 = SMW Boss Coins
# SRAM + 0x1EF8-0x1EF9 = SubGame Goals
# SRAM + 0x1F00 = Game Goals
SMASW_ITEM_HANDLER = WRAM_START + 0x0175
#SMASW_RAM_DEATHLINK = WRAM_START + 0x0179
# DEATHLINK PROTOCOL:
# byte 0 = games activated bits, send/receive deathlink, processing death
# byte 1 = deathlink rng chance, send out deathlink if >= value in rom, receiver is handled in-game
# byte 2 = internal deathlink amnesty counter, if zero, count as sending
# byte 3 = internal deathlink amnesty max, used to reset the amnesty counter
#SMASW_RAM_ROOMTRACKER = WRAM_START + 0x017D
# ROOMTRACKER PROTOCOL?:
# byte 3 = currently running game, mainly for SMW
#  SMW:
# bytes 0-1 = Current Room ID, from 0x000-0x1FF, some Rooms are reused for multiple Levels
# byte 2 = Current Overworld Map ID, 0-6, 0 is Main Map
#  SMB3:
# bytes 0-2 = Current Level Pointer, determines the real level to load; Map is handled separate
# alt byte 0 = Current Level ID, from 0x00-0x7F, the high bit (0x80) chooses the Sublevel to track
# alt byte 1 = Current World Map ID, 0-7, self-explanatory
#  SMB2:
# byte 0 = Current Level ID, from 0x00-0x15 (ish)
# byte 1 = Current Room ID, from 0x0-0x9; Room 0xA is subspace or vase only
#  SMB1LL:
# byte 0 = Current Area ID, 0x00-0x7F; the high bit (0x80) denotes World A-D for Ground
# byte 1 = Current World-Level ID, Levels are lower two bits


# SMASW ROM Stuff, if applicable
# TODO: Grab Options Data
# TODO: Deathlink ROM Data
# TODO: Any Extras we may want for the Trackers

class SMASWMemory(Enum):
    rom_hash = Read(SMASW_ROMHASH_START, ROMHASH_SIZE)
    #settings = Read(SMASW_SETTINGS, 0x00)
    sram_init_0 = Read(SMASW_SRAM_VALID_0, 2)
    sram_init_1 = Read(SMASW_SRAM_VALID_1, 2)
    recv_index = Read(SMASW_RECV_INDEX, 0x02)
    item_handler = Read(SMASW_ITEM_HANDLER, 0x04)
    normal_checks = Read(SMASW_SRAM_CHECKS_NORMAL, 0x180)
    #sanity_checks = Read(SMASW_SRAM_CHECKS_NORMAL, 0x400)
    game_goaled = Read(SMASW_SRAM_GOAL, 1)
    #deathlink_protocol = Read(SMASW_RAM_DEATHLINK, 4)
    # Game Options Info, mainly for Trackers
    # TODO: Deathlink ROM Data
    # TODO: Remote Items handling


class ProtocolMemory(Enum):
    sni_command = Read(SMASW_SNI_COMMAND, 4)
    sni_recv_dex = Read(SMASW_RECV_INDEX, 0x02)
    sni_protection = Read(SMASW_SNI_PROTECTION, 1) # 0x80 blocks Writes, 0x01 Re-enables, 0 is unset
    #sni_resync = Read(SMASW_SNI_RESYNC, 1) # TODO: See how we want to handle this


class ConnectMemory(Enum):
    rom_hash = Read(SMASW_ROMHASH_START, ROMHASH_SIZE)
    #settings = Read(SMASW_SETTINGS, 0x00)
    sram_init_0 = Read(SMASW_SRAM_VALID_0, 2)
    sram_init_1 = Read(SMASW_SRAM_VALID_1, 2)


class SMASWClient(SNIClient):
    game = "Super Mario All-Stars + Super Mario World"
    patch_suffix = ".apsmasw"
    #slot_data: dict
    ctx: "SNIContext"
    memory_reader = SnesReader(SMASWMemory)
    protocol_reader = SnesReader(ProtocolMemory)
    connect_reader = SnesReader(ConnectMemory)


    async def validate_rom(self, ctx: "SNIContext") -> bool:
        snes_data = await self.connect_reader.read(ctx)
        if snes_data is None:
            return False

        rom_name = snes_data.get(ConnectMemory.rom_hash)
        #settings = snes_data.get(ConnectMemory.settings)
        sram_valid_0 = snes_data.get(ConnectMemory.sram_init_0)
        sram_valid_1 = snes_data.get(ConnectMemory.sram_init_1)
        sram_valid_0 = int.from_bytes(sram_valid_0, "little")
        sram_valid_1 = int.from_bytes(sram_valid_1, "little")

        if rom_name is None or rom_name == bytes([0] * ROMHASH_SIZE) or rom_name[:5] != b"SMASW":
            return False
        if sram_valid_0 != 0x9743 and sram_valid_1 != 0x5321:
            return False

        ctx.game = self.game
        ctx.items_handling = 0b001  # Start Inventory is handled in-rom, Currently Local Items
        #ctx.receive_option = 0
        #ctx.send_option = 0
        ctx.allow_collect = False  # TODO: Figure out how we want to handle Collect
        ctx.slow_mode = True  # TODO: See if non-slow-mode is too fast.

        # Grabbed from DKC2, reference only
        update_tags = False

        #energy_link = settings[0x19]
        #if energy_link and "EnergyLink" not in ctx.tags:
        #    ctx.tags.add("EnergyLink")
        #    update_tags = True
        #    if "request" not in ctx.command_processor.commands:
        #        ctx.command_processor.commands["request"] = cmd_request
        #
        #trap_link = settings[0x1A]
        #if trap_link and "TrapLink" not in ctx.tags:
        #    ctx.tags.add("TrapLink")
        #    update_tags = True
        #
        #death_link = settings[0x18]
        #if death_link:
        #    await ctx.update_death_link(bool(death_link & 0b1))
        #
        #if update_tags:
        #    await ctx.send_msgs([{"cmd": "ConnectUpdate", "tags": ctx.tags}])

        ctx.rom = rom_name

        return True


    async def game_watcher(self, ctx: "SNIContext") -> None:
        from SNIClient import snes_buffered_write, snes_flush_writes, snes_read

        ## DEBUG:
        #perf_counter = time.perf_counter()

        # KSS does this here, which makes some sense since it's connection related
        if not ctx.slot or not ctx.server:
            return

        snes_data = await self.memory_reader.read(ctx)
        protocols = await self.protocol_reader.read(ctx)
        if snes_data is None or protocols is None:
            snes_logger.info(f'SNI Memory Reads not yet done')
            return
        if snes_data.get(SMASWMemory.rom_hash) != ctx.rom:
            snes_logger.info(f'Game was switched off, disconnecting...')
            ctx.rom = None
            return
        sram_valid_0 = snes_data.get(SMASWMemory.sram_init_0)
        sram_valid_1 = snes_data.get(SMASWMemory.sram_init_1)
        sram_valid_0 = int.from_bytes(sram_valid_0, "little")
        sram_valid_1 = int.from_bytes(sram_valid_1, "little")
        validate_sram = sram_valid_1 << 16 | sram_valid_0
        if validate_sram != 0x53219743:
            snes_logger.info(f'SRAM not yet Initialized or got Corrupted, waiting...')
            return


        ## Disable Slowmode if needed?
        #if ctx.slow_mode == True:
        #    ctx.slow_mode = False

        # Assign Memories to tempnames
        smasw_recv_index = snes_data.get(SMASWMemory.recv_index)
        smasw_item_processor = snes_data.get(SMASWMemory.item_handler)
        smasw_normal_checks = snes_data.get(SMASWMemory.normal_checks)
        #smasw_sanity_checks = snes_data.get(SMASWMemory.sanity_checks)
        smasw_game_goaled = snes_data.get(SMASWMemory.game_goaled)
        #smasw_deathlink_protocol= snes_data.get(SMASWMemory.deathlink_protocol)

        # Some of the following is referenced/borrowed from Tetris Attack
        # Look through goal checks
        if not ctx.finished_game:
            smasw_game_goaled = int.from_bytes(smasw_game_goaled, "little")
            if smasw_game_goaled != 0:
                await ctx.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])
                ctx.finished_game = True

        # Look through location checks
        new_checks = []
        for loc_id in ctx.missing_locations:
            if not loc_id in ctx.locations_checked:
                # TODO: Implement Sanity Checks when we get to it
                loc_addr = (loc_id - SRAM_OFFSET_NORMAL) >> 3
                loc_obtained = smasw_normal_checks[loc_addr]
                bitmask = 1 << (loc_id & 7)
                is_new_check = (loc_obtained & bitmask) != 0
                if is_new_check:
                    location = ctx.location_names.lookup_in_game(loc_id)
                    new_checks.append(loc_id)
                    snes_logger.info(
                        f"New check: {location} ({len(ctx.checked_locations) + len(new_checks)}/{len(ctx.server_locations)})")
        if len(new_checks) > 0:
            await ctx.send_msgs([{"cmd": "LocationChecks", "locations": new_checks}])
            ctx.locations_checked.update(new_checks)

        ## DEBUG:
        #perf_counter = time.perf_counter() - perf_counter
        #print("Time to do Locations Check:")
        #print(perf_counter)
        #perf_counter = time.perf_counter()

        # Re-run Protocols Check in case we have spent more than a frame doing the above
        # (Which is usually the case, anyway)
        protocols = None
        protocols = await self.protocol_reader.read(ctx)
        if protocols is None:
            return

        smasw_recv_index = protocols.get(ProtocolMemory.sni_recv_dex)
        smasw_item_processor = protocols.get(ProtocolMemory.sni_command)

        # Check for new items
        smasw_recv_index = int.from_bytes(smasw_recv_index, "little")
        smasw_item_processor = int.from_bytes(smasw_item_processor, "little")
        sni_protection_byte = protocols.get(ProtocolMemory.sni_protection)
        sni_protection_byte = int.from_bytes(sni_protection_byte, "little")
        # Skip processing the Item if already processing an Item/Command or we are prevented from writing to RAM
        if smasw_recv_index < len(ctx.items_received) and smasw_item_processor == 0x73F873F8 and sni_protection_byte == 1:
            item = ctx.items_received[smasw_recv_index]
            item_id = (item.item - ITEM_ID_OFFSET)
            item_loc = item.location
            item_player = item.player
            smasw_recv_index += 1
            item_byte_1 = 0
            item_upper = 0
            if item_player == ctx.slot: # For same-slot co-op
                item_byte_1 = 1 << (item_loc & 7)
                item_upper = (item_loc - SRAM_OFFSET_LOCS) >> 3
            # TODO: Handle Starting Inventory
            item_bytes = item_upper << 16 | item_byte_1 << 8 | item_id
            item_bytes = int.to_bytes(item_bytes, length=4, byteorder="little")
            logging.info("Received %s from %s (%s) (%d/%d in list)" % (
                color(ctx.item_names.lookup_in_game(item.item), "red", "bold"),
                color(ctx.player_names[item.player], "yellow"),
                ctx.location_names.lookup_in_slot(item.location, item.player), smasw_recv_index,
                len(ctx.items_received)))
            snes_buffered_write(ctx, SMASW_ITEM_HANDLER, item_bytes)
            snes_buffered_write(ctx, SMASW_RECV_INDEX, int.to_bytes(smasw_recv_index, length=2, byteorder="little"))

        ## DEBUG:
        #perf_counter = time.perf_counter() - perf_counter
        #print("Time to do Items Sending:")
        #print(perf_counter)
        #perf_counter = time.perf_counter()

        # Check for collected locations
        # TODO: Process only if there are no items to process (i.e. recv_index == items_received)
        #else:


        ## DEBUG:
        #perf_counter = time.perf_counter() - perf_counter
        #print(perf_counter)

        await snes_flush_writes(ctx)
