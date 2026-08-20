from __future__ import annotations

import os
import pkgutil
import Utils
import hashlib
import settings
import bsdiff4


from typing import TYPE_CHECKING, Sequence, Iterable, Optional

from Utils import snes_to_pc
from worlds.Files import APProcedurePatch, APPatchExtension, APTokenMixin, APTokenTypes
from .gfx_helpers import conv_4bpp_to_1bpp, conv_1bpp_to_4bpp, conv_1bpp_to_buffer, conv_buffer_to_1bpp, yflip_tiles, \
    rotleft_tiles, xflip_tiles

if TYPE_CHECKING:
    from .world import SMASWWorld

# This file is frankensteined from various other SNES APWorlds
# such as Spicy Mycena Waffles, Kirby Super Star, and Tetris Attack
# CVCotM was also referenced here and there

APWORLD_VERS: str = "00.00.01"
APWORLD_BETA: str = "AA"

SMASUHASH = "" #SMAS SNES Cart Hash
SMASRHASH = "" #SMAS Wii Disc Hash
SMASWHASH = "7ecaf3e2e021c8a836041c85886f4594" #SMAS+SMW Hash

# To convert into 4bpp from 2bpp for Title Screen OAM
# Used for the Player Name as well as Seed Number and Version
# Note: The "Star" Icon is offset 0x2A0
title_text_gfx_loc = {
    "A": 0xA0, "B": 0xB0, "C": 0xC0, "D": 0xD0, "E": 0xE0, "F": 0xF0, "G": 0x100, "H": 0x110, "I": 0x120, "J": 0x130,
    "K": 0x140, "L": 0x150, "M": 0x160, "N": 0x170, "O": 0x180, "P": 0x190, "Q": 0x1A0, "R": 0x1B0, "S": 0x1C0, "T": 0x1D0,
    "U": 0x1E0, "V": 0x1F0, "W": 0x200, "X": 0x210, "Y": 0x220, "Z": 0x230,

    "!": 0x260, ".": 0x290, "-": 0x240, "_": 0x240, ",": 0x2B0, "?": 0x2A0, " ": 0x280,

    "0": 0x00, "1": 0x10, "2": 0x20, "3": 0x30, "4": 0x40, "5": 0x50, "6": 0x60, "7": 0x70, "8": 0x80, "9": 0x90,

    "#": 0x250, "(": 0x240, ")": 0x240, "'": 0x250
}

# ROM Writeables, in SNES FastROM Addressing
CHECKS_ITEMS_ROM = 0x968000 # 0xC00 bytes, Store Item IDs here
SMB1LL_TRACKER = 0x9EB000 # Pause Tracker
SMB2_TRACKER = 0x9EB800 # Pause Tracker
SMB3_TRACKER = 0xB89800 # Pause Tracker
SMAS_PAUSE = 0xB8B000 # Pause Menu for SMB1/LL/3
SMB2_PAUSE = 0x9AE000 # Pause Menu for SMB2
# Output Addresses from Asar
GAME_AVAILABILITY = 0x80FF00 # 1 byte, 000w32lb
GAME_GOAL_SETTINGS = 0x80FF06 # 4 bytes
SMB1_SETTINGS = 0x80FF0A
SMBLL_SETTINGS = 0x80FF0E
SMB2_SETTINGS = 0x80FF12
SMB3_SETTINGS = 0x80FF16
SMW_SETTINGS = 0x80FF1A
GAME_EGG_MAX = 0x80FF1E # Not Implemented Fully
GAME_EGG_REQUIRED = 0x80FF28 # Not Implemented Fully
GAME_BOSS_COINS_REQUIRED = 0x80FF32 # 5 bytes, BCD Format
GAME_CHECKS_MAX = 0x80FF37 # Not Implemented Fully
REMOTE_ITEM_SETTING = 0x80FF4B # Not Implemented
DEATHLINK_SETTING = 0x80FF4C # Not Implemented
PREBUILT_SAVE = 0x80EC00 # 0x400 reserved bytes, 0x3F0 used
# Display Lock Icon, up to 4 entries each
LOCK_X_POS_HIGH = 0x80FD71
LOCK_X_POS_LOW = 0x80FD75
LOCK_GAME_MASK = 0x80FD79 # Note: same order as Game Availability
# prebuilt lock stuff, order is smb1, smbll, smb2, smb3, smw
lock_game_x_low = [0x78, 0xD8, 0x38, 0x98, 0x08]
lock_game_x_high = [0x01, 0x01, 0x00, 0x00, 0x01]
lock_game_mask = [0x01, 0x02, 0x04, 0x08, 0x10]

class RomData:
    def __init__(self, file: bytes, name: str = "") -> None:
        self.file = bytearray(file)
        self.name = name

    def read_byte(self, offset: int) -> int:
        return self.file[offset]

    def read_bytes(self, offset: int, length: int) -> bytearray:
        return self.file[offset:offset + length]

    def write_byte(self, offset: int, value: int) -> None:
        self.file[offset] = value

    def write_bytes(self, offset: int, values: Sequence[int]) -> None:
        self.file[offset:offset + len(values)] = values

    def write_to_file(self, file: str) -> None:
        with open(file, 'wb') as outfile:
            outfile.write(self.file)

    def get_bytes(self) -> bytes:
        return bytes(self.file)


# Grabbed from a Kirby SuperStar
class SMASWPatchExtensions(APPatchExtension):
    game = "Super Mario All-Stars + Super Mario World"
    @staticmethod
    def apply_basepatch(_: APProcedurePatch, rom: bytes):
        return bsdiff4.patch(rom, pkgutil.get_data(__name__, os.path.join("data", "smasw_basepatch.bsdiff4")))

    # back compat, remove in ~3 versions
    @staticmethod
    def apply_bsdiff4(caller: APProcedurePatch, rom: bytes, patch: str) -> bytes:
        return SMASWPatchExtensions.apply_basepatch(caller, rom)

    @staticmethod
    def prepare_gfx_prebasepatch(caller: APProcedurePatch, rom: bytes) -> bytes:
        # This prepares some graphics, usually tracker-related, before we apply our basepatch.
        # We do it this way since these particular edits are usually static and never change afterwards.
        # (It's also just easier this way than to apply various bsdiffs and insert original gfx at particular spots.)
        rom_data = RomData(rom)
        # First off, we modify the SMAS Pause Menu since it's relatively the easiest in terms of understanding.
        # We're not really doing much in here, just creating a new "EXIT TO MAP" option for SMB3 to use.
        # Since most of the Pause Menu here is only ever two colors, that makes text manipulation a little bit easier.
        pause_text_buffer = [0,0,0,0,0,0,0,0]   # initialize buffer
        # Fetch tiles for the "EXIT" Part
        pause_text_gfx_bytes = rom_data.read_bytes(snes_to_pc(SMAS_PAUSE+0x560), length=0x20)
        rom_data.write_bytes(snes_to_pc(SMAS_PAUSE+0x20), bytes(pause_text_gfx_bytes))
        pause_text_gfx_bytes = rom_data.read_bytes(snes_to_pc(0x868000+0x420), length=0x20)
        pause_text_gfx_bytes += rom_data.read_bytes(snes_to_pc(SMAS_PAUSE+0x4C0), length=0x20)
        pause_text_gfx_bytes += rom_data.read_bytes(snes_to_pc(SMAS_PAUSE+0x4E0), length=0x20)
        pause_text_1bpp = conv_4bpp_to_1bpp(pause_text_gfx_bytes)
        pause_text_buffer = conv_1bpp_to_buffer(pause_text_buffer, pause_text_1bpp)
        for x in range(8):
            pause_text_buffer[x] = pause_text_buffer[x]<<1
        pause_text_1bpp = conv_buffer_to_1bpp(pause_text_buffer, pause_text_1bpp)
        pause_text_gfx_bytes = conv_1bpp_to_4bpp(pause_text_1bpp)
        rom_data.write_bytes(snes_to_pc(SMAS_PAUSE+0x40), bytes(pause_text_gfx_bytes))
        # Start next text
        pause_text_buffer = [0,0,0,0,0,0,0,0]   # reinitialize buffer
        # Fetch tiles for the "TO" Part
        pause_text_gfx_bytes = rom_data.read_bytes(snes_to_pc(SMAS_PAUSE+0x2E0), length=0x20)
        pause_text_gfx_bytes += rom_data.read_bytes(snes_to_pc(SMAS_PAUSE+0x2A0), length=0x20)
        pause_text_1bpp = conv_4bpp_to_1bpp(pause_text_gfx_bytes)
        pause_text_buffer = conv_1bpp_to_buffer(pause_text_buffer, pause_text_1bpp)
        for x in range(8):
            pause_text_buffer[x] = pause_text_buffer[x]<<1
        pause_text_1bpp = conv_buffer_to_1bpp(pause_text_buffer, pause_text_1bpp)
        pause_text_gfx_bytes = conv_1bpp_to_4bpp(pause_text_1bpp)
        rom_data.write_bytes(snes_to_pc(SMAS_PAUSE+0xA0), bytes(pause_text_gfx_bytes))
        # Start next text
        pause_text_buffer = [0,0,0,0,0,0,0,0]   # reinitialize buffer
        # Fetch tiles for the " MAP" Part
        pause_text_gfx_bytes = rom_data.read_bytes(snes_to_pc(SMAS_PAUSE+0x440), length=0x20)
        pause_text_gfx_bytes += rom_data.read_bytes(snes_to_pc(0x868000+0x2C0), length=0x20)
        pause_text_gfx_bytes += rom_data.read_bytes(snes_to_pc(SMAS_PAUSE+0x520), length=0x20)
        pause_text_gfx_bytes += rom_data.read_bytes(snes_to_pc(0x868000+0x320), length=0x20)
        pause_text_1bpp = conv_4bpp_to_1bpp(pause_text_gfx_bytes)
        # Slightly modify "M" to be more symmetrical (just adds a vertical line)
        for x in range(6):
            pause_text_1bpp[x+1+8] = pause_text_1bpp[x+1+8]+0x80
        pause_text_buffer = conv_1bpp_to_buffer(pause_text_buffer, pause_text_1bpp)
        for x in range(8):
            pause_text_buffer[x] = pause_text_buffer[x]<<4
        pause_text_1bpp = conv_buffer_to_1bpp(pause_text_buffer, pause_text_1bpp)
        pause_text_gfx_bytes = conv_1bpp_to_4bpp(pause_text_1bpp)
        rom_data.write_bytes(snes_to_pc(SMAS_PAUSE+0xE0), bytes(pause_text_gfx_bytes))
        # Finish SMAS Pause Menu Stuff, now do SMB2 Pause Menu
        # Relocate "W-" tiles to a different area
        pause_text_gfx_bytes = rom_data.read_bytes(snes_to_pc(SMB2_PAUSE+0x260), length=0x20)
        pause_text_gfx_bytes += rom_data.read_bytes(snes_to_pc(SMB2_PAUSE+0x160), length=0x20)
        rom_data.write_bytes(0xCEC00, bytes(pause_text_gfx_bytes))
        # Relocate pause cursor tile to a different area
        pause_text_gfx_bytes = rom_data.read_bytes(snes_to_pc(SMB2_PAUSE+0x4C0), length=0x20)
        rom_data.write_bytes(snes_to_pc(SMB2_PAUSE+0x600), bytes(pause_text_gfx_bytes))
        # Relocate tiles for the "AVE&" part of "SAVE&****"
        pause_text_gfx_bytes = rom_data.read_bytes(snes_to_pc(SMB2_PAUSE+0x780), length=0x20)
        pause_text_gfx_bytes += rom_data.read_bytes(snes_to_pc(SMB2_PAUSE+0x7A0), length=0x20)
        pause_text_gfx_bytes += rom_data.read_bytes(snes_to_pc(SMB2_PAUSE+0x7C0), length=0x20)
        pause_text_gfx_bytes += rom_data.read_bytes(snes_to_pc(SMB2_PAUSE+0x5E0), length=0x20)
        rom_data.write_bytes(snes_to_pc(SMB2_PAUSE+0x180), bytes(pause_text_gfx_bytes))
        # Relocate tiles for "QUIT"
        pause_text_gfx_bytes = rom_data.read_bytes(snes_to_pc(SMB2_PAUSE+0x660), length=0x20)
        pause_text_gfx_bytes += rom_data.read_bytes(snes_to_pc(SMB2_PAUSE+0x680), length=0x20)
        pause_text_gfx_bytes += rom_data.read_bytes(snes_to_pc(SMB2_PAUSE+0x6A0), length=0x20)
        pause_text_gfx_bytes += rom_data.read_bytes(snes_to_pc(SMB2_PAUSE+0x6C0), length=0x20)
        rom_data.write_bytes(snes_to_pc(SMB2_PAUSE+0x460), bytes(pause_text_gfx_bytes))
        # Copy the "A" text from "SAVE" to another spot for "TO CHAR. SEL." option
        pause_text_gfx_bytes = rom_data.read_bytes(snes_to_pc(SMB2_PAUSE+0x780), length=0x20)
        pause_text_gfx_bytes = yflip_tiles(pause_text_gfx_bytes)
        rom_data.write_bytes(snes_to_pc(SMB2_PAUSE+0x640), bytes(pause_text_gfx_bytes))
        # Construct an "H" for "TO CHAR. SEL." option out of existing tiles, "U" + "A"
        pause_text_gfx_bytes = rom_data.read_bytes(snes_to_pc(SMB2_PAUSE+0x680), length=0x08)
        pause_text_gfx_bytes += rom_data.read_bytes(snes_to_pc(SMB2_PAUSE+0x788), length=0x08)
        pause_text_gfx_bytes += rom_data.read_bytes(snes_to_pc(SMB2_PAUSE+0x690), length=0x08)
        pause_text_gfx_bytes += rom_data.read_bytes(snes_to_pc(SMB2_PAUSE+0x798), length=0x08)
        rom_data.write_bytes(snes_to_pc(SMB2_PAUSE+0x620), bytes(pause_text_gfx_bytes))
        # Relocate tiles for "QUIT"
        pause_text_gfx_bytes = rom_data.read_bytes(snes_to_pc(SMB2_PAUSE+0x660), length=0x20)
        pause_text_gfx_bytes += rom_data.read_bytes(snes_to_pc(SMB2_PAUSE+0x680), length=0x20)
        pause_text_gfx_bytes += rom_data.read_bytes(snes_to_pc(SMB2_PAUSE+0x6A0), length=0x20)
        pause_text_gfx_bytes += rom_data.read_bytes(snes_to_pc(SMB2_PAUSE+0x6C0), length=0x20)
        rom_data.write_bytes(snes_to_pc(SMB2_PAUSE+0x460), bytes(pause_text_gfx_bytes))
        # Construct a dot "." out of pre-existing tiles, blank + "E"
        pause_text_gfx_bytes = rom_data.read_bytes(snes_to_pc(SMB2_PAUSE+0x700), length=0x0A)
        pause_text_gfx_bytes += rom_data.read_bytes(snes_to_pc(SMB2_PAUSE+0x7C8), length=0x04)
        pause_text_gfx_bytes += rom_data.read_bytes(snes_to_pc(SMB2_PAUSE+0x700), length=0x02)
        pause_text_gfx_bytes += rom_data.read_bytes(snes_to_pc(SMB2_PAUSE+0x710), length=0x0A)
        pause_text_gfx_bytes += rom_data.read_bytes(snes_to_pc(SMB2_PAUSE+0x7D8), length=0x04)
        pause_text_gfx_bytes += rom_data.read_bytes(snes_to_pc(SMB2_PAUSE+0x710), length=0x02)
        rom_data.write_bytes(snes_to_pc(SMB2_PAUSE+0x5E0), bytes(pause_text_gfx_bytes))
        # Construct an "R" from pre-existing tiles, blank + "E" + "U"
        pause_text_gfx_bytes = rom_data.read_bytes(snes_to_pc(SMB2_PAUSE+0x700), length=0x02)
        pause_text_gfx_bytes += rom_data.read_bytes(snes_to_pc(SMB2_PAUSE+0x7C2), length=0x02)
        pause_text_gfx_bytes += rom_data.read_bytes(snes_to_pc(SMB2_PAUSE+0x682), length=0x04)
        pause_text_gfx_bytes += rom_data.read_bytes(snes_to_pc(SMB2_PAUSE+0x7C2), length=0x02)
        pause_text_gfx_bytes += rom_data.read_bytes(snes_to_pc(SMB2_PAUSE+0x682), length=0x04)
        pause_text_gfx_bytes += rom_data.read_bytes(snes_to_pc(SMB2_PAUSE+0x700), length=0x02)
        pause_text_gfx_bytes += rom_data.read_bytes(snes_to_pc(SMB2_PAUSE+0x710), length=0x02)
        pause_text_gfx_bytes += rom_data.read_bytes(snes_to_pc(SMB2_PAUSE+0x7D2), length=0x02)
        pause_text_gfx_bytes += rom_data.read_bytes(snes_to_pc(SMB2_PAUSE+0x692), length=0x04)
        pause_text_gfx_bytes += rom_data.read_bytes(snes_to_pc(SMB2_PAUSE+0x7D2), length=0x02)
        pause_text_gfx_bytes += rom_data.read_bytes(snes_to_pc(SMB2_PAUSE+0x692), length=0x04)
        pause_text_gfx_bytes += rom_data.read_bytes(snes_to_pc(SMB2_PAUSE+0x710), length=0x02)
        rom_data.write_bytes(snes_to_pc(SMB2_PAUSE+0x7E0), bytes(pause_text_gfx_bytes))
        # Construct a new "L." tile from pre-existing tiles, "T" + "E"
        # Overwrites the original "E" tile
        pause_text_gfx_bytes = rom_data.read_bytes(snes_to_pc(SMB2_PAUSE+0x540), length=0x04)
        pause_text_gfx_bytes += rom_data.read_bytes(snes_to_pc(SMB2_PAUSE+0x7C6), length=0x02)
        pause_text_gfx_bytes += rom_data.read_bytes(snes_to_pc(SMB2_PAUSE+0x544), length=0x08)
        pause_text_gfx_bytes += rom_data.read_bytes(snes_to_pc(SMB2_PAUSE+0x700), length=0x02)
        pause_text_gfx_bytes += rom_data.read_bytes(snes_to_pc(SMB2_PAUSE+0x550), length=0x04)
        pause_text_gfx_bytes += rom_data.read_bytes(snes_to_pc(SMB2_PAUSE+0x7D6), length=0x02)
        pause_text_gfx_bytes += rom_data.read_bytes(snes_to_pc(SMB2_PAUSE+0x554), length=0x08)
        pause_text_gfx_bytes += rom_data.read_bytes(snes_to_pc(SMB2_PAUSE+0x710), length=0x02)
        pause_text_gfx_bytes = rotleft_tiles(pause_text_gfx_bytes, 3)
        pause_text_gfx_bytes = yflip_tiles(pause_text_gfx_bytes)
        rom_data.write_bytes(snes_to_pc(SMB2_PAUSE+0x7C0), bytes(pause_text_gfx_bytes))
        # Blank out some now-unused tiles and fill for 16x16 sprites
        # Some of these tiles get overwritten with original tiles from the basepatch
        pause_text_gfx_bytes = rom_data.read_bytes(snes_to_pc(SMB2_PAUSE+0x700), length=0x20)
        pause_text_gfx_bytes += rom_data.read_bytes(snes_to_pc(SMB2_PAUSE+0x700), length=0x20)
        rom_data.write_bytes(snes_to_pc(SMB2_PAUSE+0x260), bytes(pause_text_gfx_bytes))
        rom_data.write_bytes(snes_to_pc(SMB2_PAUSE+0x2A0), bytes(pause_text_gfx_bytes))
        rom_data.write_bytes(snes_to_pc(SMB2_PAUSE+0x340), bytes(pause_text_gfx_bytes))
        rom_data.write_bytes(snes_to_pc(SMB2_PAUSE+0x380), bytes(pause_text_gfx_bytes))
        rom_data.write_bytes(snes_to_pc(SMB2_PAUSE+0x660), bytes(pause_text_gfx_bytes))
        rom_data.write_bytes(snes_to_pc(SMB2_PAUSE+0x6A0), bytes(pause_text_gfx_bytes))
        rom_data.write_bytes(snes_to_pc(SMB2_PAUSE+0x780), bytes(pause_text_gfx_bytes))
        rom_data.write_bytes(0xCEE00, bytes(pause_text_gfx_bytes)) # Technically a full blank, but w/e
        pause_text_gfx_bytes = rom_data.read_bytes(snes_to_pc(SMB2_PAUSE+0x700), length=0x20)
        rom_data.write_bytes(snes_to_pc(SMB2_PAUSE+0x2E0), bytes(pause_text_gfx_bytes))
        rom_data.write_bytes(snes_to_pc(SMB2_PAUSE+0x160), bytes(pause_text_gfx_bytes))
        # Finished with SMB2 Pause stuff, now doing SMB2 Tracker
        # Copy tiles from Pause Menu
        buffer_gfx_bytes = rom_data.read_bytes(snes_to_pc(SMB2_PAUSE), length=0x60)
        rom_data.write_bytes(snes_to_pc(SMB2_TRACKER), bytes(buffer_gfx_bytes))
        buffer_gfx_bytes = rom_data.read_bytes(snes_to_pc(SMB2_PAUSE+0x200), length=0x60)
        rom_data.write_bytes(snes_to_pc(SMB2_TRACKER+0x200), bytes(buffer_gfx_bytes))
        buffer_gfx_bytes = rom_data.read_bytes(snes_to_pc(SMB2_PAUSE+0x400), length=0x60)
        rom_data.write_bytes(snes_to_pc(SMB2_TRACKER+0x400), bytes(buffer_gfx_bytes))
        buffer_gfx_bytes = rom_data.read_bytes(snes_to_pc(SMB2_PAUSE+0x080), length=0x20)
        rom_data.write_bytes(snes_to_pc(SMB2_TRACKER+0x060), bytes(buffer_gfx_bytes))
        buffer_gfx_bytes = rom_data.read_bytes(snes_to_pc(SMB2_PAUSE+0x0A0), length=0x20)
        rom_data.write_bytes(snes_to_pc(SMB2_TRACKER+0x260), bytes(buffer_gfx_bytes))
        buffer_gfx_bytes = rom_data.read_bytes(snes_to_pc(SMB2_PAUSE+0x0C0), length=0x20)
        rom_data.write_bytes(snes_to_pc(SMB2_TRACKER+0x460), bytes(buffer_gfx_bytes))
        buffer_gfx_bytes = rom_data.read_bytes(snes_to_pc(SMB2_PAUSE+0x0E0), length=0x80)
        rom_data.write_bytes(snes_to_pc(SMB2_TRACKER+0x600), bytes(buffer_gfx_bytes))
        # Handle Abilities, Real File Offsets since it's easier to see what's going on
        # Starting off with Small Mario Walk, for Dash Ability
        buffer_gfx_bytes = rom_data.read_bytes(0x178A0A, 0x06)
        buffer_gfx_bytes += rom_data.read_bytes(0x178840, 0x0A)
        buffer_gfx_bytes += rom_data.read_bytes(0x178A1A, 0x06)
        buffer_gfx_bytes += rom_data.read_bytes(0x178850, 0x0A)
        buffer_gfx_bytes += rom_data.read_bytes(0x178A2A, 0x06)
        buffer_gfx_bytes += rom_data.read_bytes(0x178860, 0x0A)
        buffer_gfx_bytes += rom_data.read_bytes(0x178A3A, 0x06)
        buffer_gfx_bytes += rom_data.read_bytes(0x178870, 0x0A)
        # Write Top Half
        rom_data.write_bytes(snes_to_pc(SMB2_TRACKER+0x080), bytes(buffer_gfx_bytes))
        rom_data.write_bytes(snes_to_pc(SMB2_TRACKER+0x0C0), bytes(buffer_gfx_bytes))
        # Get data for Bottom Half
        buffer_gfx_bytes = rom_data.read_bytes(0x17884A, 0x06)
        buffer_gfx_bytes += rom_data.read_bytes(0x178A40, 0x0A)
        buffer_gfx_bytes += rom_data.read_bytes(0x17885A, 0x06)
        buffer_gfx_bytes += rom_data.read_bytes(0x178A50, 0x0A)
        buffer_gfx_bytes += rom_data.read_bytes(0x17886A, 0x06)
        buffer_gfx_bytes += rom_data.read_bytes(0x178A60, 0x0A)
        buffer_gfx_bytes += rom_data.read_bytes(0x17887A, 0x06)
        buffer_gfx_bytes += rom_data.read_bytes(0x178A70, 0x0A)
        # Write Bottom Half
        rom_data.write_bytes(snes_to_pc(SMB2_TRACKER+0x280), bytes(buffer_gfx_bytes))
        rom_data.write_bytes(snes_to_pc(SMB2_TRACKER+0x2C0), bytes(buffer_gfx_bytes))
        # Get tiles of Small Mario Carrying, for Grab Ability
        buffer_gfx_bytes = rom_data.read_bytes(0x178A0A+0xC0, 0x06)
        buffer_gfx_bytes += rom_data.read_bytes(0x178840+0x100, 0x0A)
        buffer_gfx_bytes += rom_data.read_bytes(0x178A1A+0xC0, 0x06)
        buffer_gfx_bytes += rom_data.read_bytes(0x178850+0x100, 0x0A)
        buffer_gfx_bytes += rom_data.read_bytes(0x178A2A+0xC0, 0x06)
        buffer_gfx_bytes += rom_data.read_bytes(0x178860+0x100, 0x0A)
        buffer_gfx_bytes += rom_data.read_bytes(0x178A3A+0xC0, 0x06)
        buffer_gfx_bytes += rom_data.read_bytes(0x178870+0x100, 0x0A)
        # Write Top Half
        rom_data.write_bytes(snes_to_pc(SMB2_TRACKER+0x480), bytes(buffer_gfx_bytes))
        rom_data.write_bytes(snes_to_pc(SMB2_TRACKER+0x4C0), bytes(buffer_gfx_bytes))
        # Get data for Bottom Half
        buffer_gfx_bytes = rom_data.read_bytes(0x17884A+0x100, 0x06)
        buffer_gfx_bytes += rom_data.read_bytes(0x178A40+0x100, 0x0A)
        buffer_gfx_bytes += rom_data.read_bytes(0x17885A+0x100, 0x06)
        buffer_gfx_bytes += rom_data.read_bytes(0x178A50+0x100, 0x0A)
        buffer_gfx_bytes += rom_data.read_bytes(0x17886A+0x100, 0x06)
        buffer_gfx_bytes += rom_data.read_bytes(0x178A60+0x100, 0x0A)
        buffer_gfx_bytes += rom_data.read_bytes(0x17887A+0x100, 0x06)
        buffer_gfx_bytes += rom_data.read_bytes(0x178A70+0x100, 0x0A)
        # Write Bottom Half
        rom_data.write_bytes(snes_to_pc(SMB2_TRACKER+0x680), bytes(buffer_gfx_bytes))
        rom_data.write_bytes(snes_to_pc(SMB2_TRACKER+0x6C0), bytes(buffer_gfx_bytes))
        # Get tiles of Small Mario Climb, for Climb Ability
        buffer_gfx_bytes = rom_data.read_bytes(0x178B84, 0x0C)
        buffer_gfx_bytes += rom_data.read_bytes(0x1789C0, 0x04)
        buffer_gfx_bytes += rom_data.read_bytes(0x178B94, 0x0C)
        buffer_gfx_bytes += rom_data.read_bytes(0x1789D0, 0x04)
        buffer_gfx_bytes += rom_data.read_bytes(0x178BA4, 0x0C)
        buffer_gfx_bytes += rom_data.read_bytes(0x1789E0, 0x04)
        buffer_gfx_bytes += rom_data.read_bytes(0x178BB4, 0x0C)
        buffer_gfx_bytes += rom_data.read_bytes(0x1789F0, 0x04)
        # Write Top Half
        rom_data.write_bytes(0x0CED80, bytes(buffer_gfx_bytes))
        rom_data.write_bytes(0x0CEDC0, bytes(buffer_gfx_bytes))
        # Get data for Bottom Half
        buffer_gfx_bytes = rom_data.read_bytes(0x1789C4, 0x0C)
        buffer_gfx_bytes += rom_data.read_bytes(0x178BC0, 0x04)
        buffer_gfx_bytes += rom_data.read_bytes(0x1789D4, 0x0C)
        buffer_gfx_bytes += rom_data.read_bytes(0x178BD0, 0x04)
        buffer_gfx_bytes += rom_data.read_bytes(0x1789E4, 0x0C)
        buffer_gfx_bytes += rom_data.read_bytes(0x178BE0, 0x04)
        buffer_gfx_bytes += rom_data.read_bytes(0x1789F4, 0x0C)
        buffer_gfx_bytes += rom_data.read_bytes(0x178BF0, 0x04)
        # Write Bottom Half
        rom_data.write_bytes(0x0CEF80, bytes(buffer_gfx_bytes))
        rom_data.write_bytes(0x0CEFC0, bytes(buffer_gfx_bytes))
        # Character Unlocks stuff here, starting with Mario
        buffer_gfx_bytes = rom_data.read_bytes(0x0BC144, 0x0C)
        buffer_gfx_bytes += rom_data.read_bytes(0x0BC340, 0x04)
        buffer_gfx_bytes += rom_data.read_bytes(0x0BC154, 0x0C)
        buffer_gfx_bytes += rom_data.read_bytes(0x0BC350, 0x04)
        buffer_gfx_bytes += rom_data.read_bytes(0x0BC164, 0x0C)
        buffer_gfx_bytes += rom_data.read_bytes(0x0BC360, 0x04)
        buffer_gfx_bytes += rom_data.read_bytes(0x0BC174, 0x0C)
        buffer_gfx_bytes += rom_data.read_bytes(0x0BC370, 0x04)
        # Write Top Half
        rom_data.write_bytes(snes_to_pc(SMB2_TRACKER+0x140), bytes(buffer_gfx_bytes))
        # Get data for Bottom Half
        buffer_gfx_bytes = rom_data.read_bytes(0x0BC344, 0x0C)
        buffer_gfx_bytes += rom_data.read_bytes(0x0BC180, 0x04)
        buffer_gfx_bytes += rom_data.read_bytes(0x0BC354, 0x0C)
        buffer_gfx_bytes += rom_data.read_bytes(0x0BC190, 0x04)
        buffer_gfx_bytes += rom_data.read_bytes(0x0BC364, 0x0C)
        buffer_gfx_bytes += rom_data.read_bytes(0x0BC1A0, 0x04)
        buffer_gfx_bytes += rom_data.read_bytes(0x0BC374, 0x0C)
        buffer_gfx_bytes += rom_data.read_bytes(0x0BC1B0, 0x04)
        # Write Bottom Half
        rom_data.write_bytes(snes_to_pc(SMB2_TRACKER+0x340), bytes(buffer_gfx_bytes))
        # Handle "Locked" Mario
        buffer_gfx_bytes = rom_data.read_bytes(snes_to_pc(SMB2_TRACKER+0x140), 0x20)
        rom_data.write_bytes(snes_to_pc(SMB2_TRACKER+0x100), bytes(buffer_gfx_bytes))
        buffer_gfx_bytes = xflip_tiles(buffer_gfx_bytes)
        rom_data.write_bytes(snes_to_pc(SMB2_TRACKER+0x120), bytes(buffer_gfx_bytes))
        buffer_gfx_bytes = rom_data.read_bytes(snes_to_pc(SMB2_TRACKER+0x340), 0x20)
        rom_data.write_bytes(snes_to_pc(SMB2_TRACKER+0x300), bytes(buffer_gfx_bytes))
        buffer_gfx_bytes = xflip_tiles(buffer_gfx_bytes)
        rom_data.write_bytes(snes_to_pc(SMB2_TRACKER+0x320), bytes(buffer_gfx_bytes))
        # Luigi Character Unlocks
        buffer_gfx_bytes = rom_data.read_bytes(0x0BC1C0, 0x40)
        # Write Top Half
        rom_data.write_bytes(snes_to_pc(SMB2_TRACKER+0x540), bytes(buffer_gfx_bytes))
        # Get data for Bottom Half
        buffer_gfx_bytes = rom_data.read_bytes(0x0BC3C0, 0x40)
        # Write Bottom Half
        rom_data.write_bytes(snes_to_pc(SMB2_TRACKER+0x740), bytes(buffer_gfx_bytes))
        # Handle "Locked" Luigi
        buffer_gfx_bytes = rom_data.read_bytes(snes_to_pc(SMB2_TRACKER+0x540), 0x20)
        rom_data.write_bytes(snes_to_pc(SMB2_TRACKER+0x500), bytes(buffer_gfx_bytes))
        buffer_gfx_bytes = xflip_tiles(buffer_gfx_bytes)
        rom_data.write_bytes(snes_to_pc(SMB2_TRACKER+0x520), bytes(buffer_gfx_bytes))
        buffer_gfx_bytes = rom_data.read_bytes(snes_to_pc(SMB2_TRACKER+0x740), 0x20)
        rom_data.write_bytes(snes_to_pc(SMB2_TRACKER+0x700), bytes(buffer_gfx_bytes))
        buffer_gfx_bytes = xflip_tiles(buffer_gfx_bytes)
        rom_data.write_bytes(snes_to_pc(SMB2_TRACKER+0x720), bytes(buffer_gfx_bytes))
        # Toad Character Unlocks
        buffer_gfx_bytes = rom_data.read_bytes(0x0BBF80, 0x40)
        # Write Top Half
        rom_data.write_bytes(snes_to_pc(SMB2_TRACKER+0x1C0), bytes(buffer_gfx_bytes))
        # Get data for Bottom Half
        buffer_gfx_bytes = rom_data.read_bytes(0x0BBDC0, 0x40)
        # Write Bottom Half
        rom_data.write_bytes(snes_to_pc(SMB2_TRACKER+0x3C0), bytes(buffer_gfx_bytes))
        # Handle "Locked" Toad
        buffer_gfx_bytes = rom_data.read_bytes(snes_to_pc(SMB2_TRACKER+0x1C0), 0x20)
        rom_data.write_bytes(snes_to_pc(SMB2_TRACKER+0x180), bytes(buffer_gfx_bytes))
        buffer_gfx_bytes = xflip_tiles(buffer_gfx_bytes)
        rom_data.write_bytes(snes_to_pc(SMB2_TRACKER+0x1A0), bytes(buffer_gfx_bytes))
        buffer_gfx_bytes = rom_data.read_bytes(snes_to_pc(SMB2_TRACKER+0x3C0), 0x20)
        rom_data.write_bytes(snes_to_pc(SMB2_TRACKER+0x380), bytes(buffer_gfx_bytes))
        buffer_gfx_bytes = xflip_tiles(buffer_gfx_bytes)
        rom_data.write_bytes(snes_to_pc(SMB2_TRACKER+0x3A0), bytes(buffer_gfx_bytes))
        # Peach Character Unlocks
        buffer_gfx_bytes = rom_data.read_bytes(0x0BC440, 0x40)
        # Write Top Half
        rom_data.write_bytes(snes_to_pc(SMB2_TRACKER+0x5C0), bytes(buffer_gfx_bytes))
        # Get data for Bottom Half
        buffer_gfx_bytes = rom_data.read_bytes(0x0BC640, 0x40)
        # Write Bottom Half
        rom_data.write_bytes(snes_to_pc(SMB2_TRACKER+0x7C0), bytes(buffer_gfx_bytes))
        # Handle "Locked" Peach
        buffer_gfx_bytes = rom_data.read_bytes(snes_to_pc(SMB2_TRACKER+0x5C0), 0x20)
        rom_data.write_bytes(snes_to_pc(SMB2_TRACKER+0x580), bytes(buffer_gfx_bytes))
        buffer_gfx_bytes = xflip_tiles(buffer_gfx_bytes)
        rom_data.write_bytes(snes_to_pc(SMB2_TRACKER+0x5A0), bytes(buffer_gfx_bytes))
        buffer_gfx_bytes = rom_data.read_bytes(snes_to_pc(SMB2_TRACKER+0x7C0), 0x20)
        rom_data.write_bytes(snes_to_pc(SMB2_TRACKER+0x780), bytes(buffer_gfx_bytes))
        buffer_gfx_bytes = xflip_tiles(buffer_gfx_bytes)
        rom_data.write_bytes(snes_to_pc(SMB2_TRACKER+0x7A0), bytes(buffer_gfx_bytes))
        # Finished with Character Unlocks, handle Starman/Clock/Potion
        # Starman
        buffer_gfx_bytes = rom_data.read_bytes(0x0B5540, 0x40)
        rom_data.write_bytes(0x17D000, bytes(buffer_gfx_bytes))
        rom_data.write_bytes(0x0CE140, bytes(buffer_gfx_bytes))
        buffer_gfx_bytes = rom_data.read_bytes(0x0B5740, 0x40)
        rom_data.write_bytes(0x17F000, bytes(buffer_gfx_bytes))
        rom_data.write_bytes(0x0CE340, bytes(buffer_gfx_bytes))
        # Potion
        buffer_gfx_bytes = rom_data.read_bytes(0x0B6080, 0x40)
        rom_data.write_bytes(0x17D040, bytes(buffer_gfx_bytes))
        rom_data.write_bytes(0x0CE1C0, bytes(buffer_gfx_bytes))
        buffer_gfx_bytes = rom_data.read_bytes(0x0B6680, 0x40)
        rom_data.write_bytes(0x17F040, bytes(buffer_gfx_bytes))
        rom_data.write_bytes(0x0CE3C0, bytes(buffer_gfx_bytes))
        # Clock
        buffer_gfx_bytes = rom_data.read_bytes(0x0B4540, 0x40)
        rom_data.write_bytes(0x0CE180, bytes(buffer_gfx_bytes))
        buffer_gfx_bytes = rom_data.read_bytes(0x0B4740, 0x40)
        rom_data.write_bytes(0x0CE380, bytes(buffer_gfx_bytes))
        # Finished SMB2 Pause Tracker, now handle the other Pause Trackers
        # Border and Fill tiles
        buffer_gfx_bytes = rom_data.read_bytes(snes_to_pc(SMAS_PAUSE+0x220), 0x60)
        buffer_gfx_bytes += rom_data.read_bytes(snes_to_pc(SMAS_PAUSE+0x3A0), 0x20)
        rom_data.write_bytes(snes_to_pc(SMB1LL_TRACKER), bytes(buffer_gfx_bytes))
        buffer_gfx_bytes = rom_data.read_bytes(snes_to_pc(SMAS_PAUSE+0x420), 0x60)
        buffer_gfx_bytes += rom_data.read_bytes(snes_to_pc(SMAS_PAUSE+0x3A0), 0x20)
        rom_data.write_bytes(snes_to_pc(SMB1LL_TRACKER+0x200), bytes(buffer_gfx_bytes))
        rom_data.write_bytes(snes_to_pc(SMB1LL_TRACKER+0x400), bytes(buffer_gfx_bytes))
        buffer_gfx_bytes = rom_data.read_bytes(snes_to_pc(SMAS_PAUSE+0x3A0), 0x40)
        buffer_gfx_bytes += rom_data.read_bytes(snes_to_pc(SMAS_PAUSE+0x3A0), 0x40)
        rom_data.write_bytes(snes_to_pc(SMB1LL_TRACKER+0x600), bytes(buffer_gfx_bytes))
        # Get Power-Up Tiles (SMB1LL)
        # Mushroom
        buffer_gfx_bytes = rom_data.read_bytes(0x039D20, 0x40)
        rom_data.write_bytes(snes_to_pc(SMB1LL_TRACKER+0x080), bytes(buffer_gfx_bytes))
        rom_data.write_bytes(snes_to_pc(SMB1LL_TRACKER+0x0C0), bytes(buffer_gfx_bytes))
        buffer_gfx_bytes = rom_data.read_bytes(0x038F00, 0x40)
        rom_data.write_bytes(snes_to_pc(SMB1LL_TRACKER+0x280), bytes(buffer_gfx_bytes))
        rom_data.write_bytes(snes_to_pc(SMB1LL_TRACKER+0x2C0), bytes(buffer_gfx_bytes))
        # Fire Flower
        buffer_gfx_bytes = rom_data.read_bytes(0x039AC0, 0x20)
        rom_data.write_bytes(snes_to_pc(SMB1LL_TRACKER+0x480), bytes(buffer_gfx_bytes))
        rom_data.write_bytes(snes_to_pc(SMB1LL_TRACKER+0x4C0), bytes(buffer_gfx_bytes))
        buffer_gfx_bytes = xflip_tiles(buffer_gfx_bytes)
        rom_data.write_bytes(snes_to_pc(SMB1LL_TRACKER+0x4A0), bytes(buffer_gfx_bytes))
        rom_data.write_bytes(snes_to_pc(SMB1LL_TRACKER+0x4E0), bytes(buffer_gfx_bytes))
        buffer_gfx_bytes = rom_data.read_bytes(0x039B20, 0x20)
        rom_data.write_bytes(snes_to_pc(SMB1LL_TRACKER+0x680), bytes(buffer_gfx_bytes))
        rom_data.write_bytes(snes_to_pc(SMB1LL_TRACKER+0x6C0), bytes(buffer_gfx_bytes))
        buffer_gfx_bytes = xflip_tiles(buffer_gfx_bytes)
        rom_data.write_bytes(snes_to_pc(SMB1LL_TRACKER+0x6A0), bytes(buffer_gfx_bytes))
        rom_data.write_bytes(snes_to_pc(SMB1LL_TRACKER+0x6E0), bytes(buffer_gfx_bytes))
        # Starman
        buffer_gfx_bytes = rom_data.read_bytes(0x0391A0, 0x20)
        rom_data.write_bytes(snes_to_pc(SMB1LL_TRACKER+0x500), bytes(buffer_gfx_bytes))
        rom_data.write_bytes(snes_to_pc(SMB1LL_TRACKER+0x540), bytes(buffer_gfx_bytes))
        buffer_gfx_bytes = xflip_tiles(buffer_gfx_bytes)
        rom_data.write_bytes(snes_to_pc(SMB1LL_TRACKER+0x520), bytes(buffer_gfx_bytes))
        rom_data.write_bytes(snes_to_pc(SMB1LL_TRACKER+0x560), bytes(buffer_gfx_bytes))
        buffer_gfx_bytes = rom_data.read_bytes(0x039C80, 0x20)
        rom_data.write_bytes(snes_to_pc(SMB1LL_TRACKER+0x700), bytes(buffer_gfx_bytes))
        rom_data.write_bytes(snes_to_pc(SMB1LL_TRACKER+0x740), bytes(buffer_gfx_bytes))
        buffer_gfx_bytes = xflip_tiles(buffer_gfx_bytes)
        rom_data.write_bytes(snes_to_pc(SMB1LL_TRACKER+0x720), bytes(buffer_gfx_bytes))
        rom_data.write_bytes(snes_to_pc(SMB1LL_TRACKER+0x760), bytes(buffer_gfx_bytes))
        # Small Mario Climb
        buffer_gfx_bytes = rom_data.read_bytes(0x051480, 0x40)
        rom_data.write_bytes(snes_to_pc(SMB1LL_TRACKER+0x100), bytes(buffer_gfx_bytes))
        rom_data.write_bytes(snes_to_pc(SMB1LL_TRACKER+0x140), bytes(buffer_gfx_bytes))
        buffer_gfx_bytes = rom_data.read_bytes(0x0514C0, 0x40)
        rom_data.write_bytes(snes_to_pc(SMB1LL_TRACKER+0x300), bytes(buffer_gfx_bytes))
        rom_data.write_bytes(snes_to_pc(SMB1LL_TRACKER+0x340), bytes(buffer_gfx_bytes))
        # Small Mario Walk (Dash)
        buffer_gfx_bytes = rom_data.read_bytes(0x050D80, 0x40)
        rom_data.write_bytes(snes_to_pc(SMB1LL_TRACKER+0x180), bytes(buffer_gfx_bytes))
        rom_data.write_bytes(snes_to_pc(SMB1LL_TRACKER+0x1C0), bytes(buffer_gfx_bytes))
        buffer_gfx_bytes = rom_data.read_bytes(0x050DC0, 0x40)
        rom_data.write_bytes(snes_to_pc(SMB1LL_TRACKER+0x380), bytes(buffer_gfx_bytes))
        rom_data.write_bytes(snes_to_pc(SMB1LL_TRACKER+0x3C0), bytes(buffer_gfx_bytes))
        # Small Mario Swim
        buffer_gfx_bytes = rom_data.read_bytes(0x051380, 0x40)
        rom_data.write_bytes(snes_to_pc(SMB1LL_TRACKER+0x580), bytes(buffer_gfx_bytes))
        rom_data.write_bytes(snes_to_pc(SMB1LL_TRACKER+0x5C0), bytes(buffer_gfx_bytes))
        buffer_gfx_bytes = rom_data.read_bytes(0x0513C0, 0x40)
        rom_data.write_bytes(snes_to_pc(SMB1LL_TRACKER+0x780), bytes(buffer_gfx_bytes))
        rom_data.write_bytes(snes_to_pc(SMB1LL_TRACKER+0x7C0), bytes(buffer_gfx_bytes))
        # Finished SMB1LL Pause Tracker, now handle the SMB3 Pause Tracker
        # Fill Tile
        buffer_gfx_bytes = rom_data.read_bytes(snes_to_pc(SMAS_PAUSE+0x3A0), 0x40)
        rom_data.write_bytes(snes_to_pc(SMB3_TRACKER+0x5C0), bytes(buffer_gfx_bytes))
        rom_data.write_bytes(snes_to_pc(SMB3_TRACKER+0x7C0), bytes(buffer_gfx_bytes))
        # Get Power-Up Tiles (SMB3), most are conveniently placed from Inventory
        # Mushroom, Flower, Leaf, and Suits (+ Cloud as filler-buffer)
        buffer_gfx_bytes = rom_data.read_bytes(0x1C7840, 0x1C0)
        rom_data.write_bytes(snes_to_pc(SMB3_TRACKER+0x000), bytes(buffer_gfx_bytes))
        buffer_gfx_bytes = rom_data.read_bytes(0x1C7A40, 0x1C0)
        rom_data.write_bytes(snes_to_pc(SMB3_TRACKER+0x200), bytes(buffer_gfx_bytes))
        # Starman
        buffer_gfx_bytes = rom_data.read_bytes(0x1C7C40, 0x40)
        rom_data.write_bytes(snes_to_pc(SMB3_TRACKER+0x1C0), bytes(buffer_gfx_bytes))
        buffer_gfx_bytes = rom_data.read_bytes(0x1C7E40, 0x40)
        rom_data.write_bytes(snes_to_pc(SMB3_TRACKER+0x3C0), bytes(buffer_gfx_bytes))
        # P-Wing
        buffer_gfx_bytes = rom_data.read_bytes(0x1C7C00, 0x40)
        rom_data.write_bytes(snes_to_pc(SMB3_TRACKER+0x580), bytes(buffer_gfx_bytes))
        buffer_gfx_bytes = rom_data.read_bytes(0x1C7E00, 0x40)
        rom_data.write_bytes(snes_to_pc(SMB3_TRACKER+0x780), bytes(buffer_gfx_bytes))
        # Kuribo Shoe
        buffer_gfx_bytes = rom_data.read_bytes(0x205D00, 0x20)
        buffer_gfx_bytes += rom_data.read_bytes(0x205D80, 0x20)
        rom_data.write_bytes(snes_to_pc(SMB3_TRACKER+0x540), bytes(buffer_gfx_bytes))
        buffer_gfx_bytes = rom_data.read_bytes(0x205D20, 0x20)
        buffer_gfx_bytes += rom_data.read_bytes(0x205DA0, 0x20)
        rom_data.write_bytes(snes_to_pc(SMB3_TRACKER+0x740), bytes(buffer_gfx_bytes))
        # P-Switch
        buffer_gfx_bytes = rom_data.read_bytes(0x231C00, 0x20)
        buffer_gfx_bytes += rom_data.read_bytes(0x231C40, 0x20)
        rom_data.write_bytes(snes_to_pc(SMB3_TRACKER+0x500), bytes(buffer_gfx_bytes))
        buffer_gfx_bytes = rom_data.read_bytes(0x231C20, 0x20)
        buffer_gfx_bytes += rom_data.read_bytes(0x231C60, 0x20)
        rom_data.write_bytes(snes_to_pc(SMB3_TRACKER+0x700), bytes(buffer_gfx_bytes))
        # Small Mario Sprint (Dash)
        buffer_gfx_bytes = rom_data.read_bytes(0x1F7E00, 0x20)
        buffer_gfx_bytes += rom_data.read_bytes(0x1F7E40, 0x20)
        rom_data.write_bytes(snes_to_pc(SMB3_TRACKER+0x400), bytes(buffer_gfx_bytes))
        buffer_gfx_bytes = rom_data.read_bytes(0x1F7E20, 0x20)
        buffer_gfx_bytes += rom_data.read_bytes(0x1F7E60, 0x20)
        rom_data.write_bytes(snes_to_pc(SMB3_TRACKER+0x600), bytes(buffer_gfx_bytes))
        # Small Mario Climb
        buffer_gfx_bytes = rom_data.read_bytes(0x1F7900, 0x20)
        buffer_gfx_bytes += rom_data.read_bytes(0x1F7940, 0x20)
        rom_data.write_bytes(snes_to_pc(SMB3_TRACKER+0x440), bytes(buffer_gfx_bytes))
        buffer_gfx_bytes = rom_data.read_bytes(0x1F7920, 0x20)
        buffer_gfx_bytes += rom_data.read_bytes(0x1F7960, 0x20)
        rom_data.write_bytes(snes_to_pc(SMB3_TRACKER+0x640), bytes(buffer_gfx_bytes))
        # Small Mario Carry (Grab)
        buffer_gfx_bytes = rom_data.read_bytes(0x1F7680, 0x20)
        buffer_gfx_bytes += rom_data.read_bytes(0x1F76C0, 0x20)
        rom_data.write_bytes(snes_to_pc(SMB3_TRACKER+0x4C0), bytes(buffer_gfx_bytes))
        buffer_gfx_bytes = rom_data.read_bytes(0x1F76A0, 0x20)
        buffer_gfx_bytes += rom_data.read_bytes(0x1F76E0, 0x20)
        rom_data.write_bytes(snes_to_pc(SMB3_TRACKER+0x6C0), bytes(buffer_gfx_bytes))
        # Small Mario Swim
        buffer_gfx_bytes = rom_data.read_bytes(0x1F7D00, 0x20)
        buffer_gfx_bytes += rom_data.read_bytes(0x1F7DC0, 0x20)
        rom_data.write_bytes(snes_to_pc(SMB3_TRACKER+0x480), bytes(buffer_gfx_bytes))
        buffer_gfx_bytes = rom_data.read_bytes(0x1F7D20, 0x20)
        buffer_gfx_bytes += rom_data.read_bytes(0x1F7DE0, 0x20)
        rom_data.write_bytes(snes_to_pc(SMB3_TRACKER+0x680), bytes(buffer_gfx_bytes))
        # Finished SMB3 Pause Tracker, now handle the other GFX changes
        # Game Select Area Select stuff
        # Star relocated
        buffer_gfx_bytes = rom_data.read_bytes(0x24F6C0, 0x40)
        rom_data.write_bytes(0x24E740, bytes(buffer_gfx_bytes))
        # Dash copied
        buffer_gfx_bytes = rom_data.read_bytes(0x24BBC0, 0x40)
        rom_data.write_bytes(0x24E6C0, bytes(buffer_gfx_bytes))
        rom_data.write_bytes(0x24E700, bytes(buffer_gfx_bytes))
        rom_data.write_bytes(0x24E780, bytes(buffer_gfx_bytes))
        rom_data.write_bytes(0x24E7C0, bytes(buffer_gfx_bytes))
        # Copy into SMW's Star Identifier
        rom_data.write_bytes(0x24F6C0, bytes(buffer_gfx_bytes))
        # Finished Everything at let the basepatch do its thing
        return rom_data.get_bytes()

    @staticmethod
    def relocate_copy_data(caller: APProcedurePatch, rom: bytes) -> bytes:
        # This mainly copies and relocates various bits of data around after the basepatch has been applied.
        # A lot of this is static data that is pre-determined such as levels and maps, so we handle it here.
        # We also do some code-copies in this step since future basepatches will incorporate FastROM Addressing.
        rom_data = RomData(rom)
        # A lot of the code in here is semi-generated with the help of using Asar's Macros to insert "Copy-Points"
        #  while we write the ASM Code.
        # This makes it a lot easier to compile into Python-specific Code as-needed whenever we may need to create
        #  a new basepatch and testing Debug Game.
        # Some manual code adjustments are needed as they come by, such as Level Data stuff.
        
        #Something about World-Level Table Select: 0x80ADFD
        copy_buffer = rom_data.read_bytes(snes_to_pc(0x80ae0b), length=6)
        rom_data.write_bytes(snes_to_pc(0x80ADFD), bytes(copy_buffer))

        #BufferSaveLevelFix: 0x80AE79
        copy_buffer = rom_data.read_bytes(snes_to_pc(0x80ae3a), length=2)
        rom_data.write_bytes(snes_to_pc(0x80AE7E), bytes(copy_buffer))

        #LevelDisplayHax_InitIndices: 0x80E751
        copy_buffer = rom_data.read_bytes(snes_to_pc(0x80b1c0), length=10)
        rom_data.write_bytes(snes_to_pc(0x80E752), bytes(copy_buffer))

        #LevelDisplayHax_LevelTable: 0x80E766
        copy_buffer = rom_data.read_bytes(snes_to_pc(0x80b1ed), length=5)
        rom_data.write_bytes(snes_to_pc(0x80E766), bytes(copy_buffer))

        #AreaMappingSMB1_Level: 0x88ED40
        copy_buffer = rom_data.read_bytes(snes_to_pc(0x85d272), length=32)
        for x in range(8):
            copy_buffer[(x*4)+1] = 1
        rom_data.write_bytes(snes_to_pc(0x88ED40), bytes(copy_buffer))
        copy_buffer = rom_data.read_bytes(snes_to_pc(0x85d272), length=32)
        for x in range(8):
            copy_buffer[(x*4)+1] = 1
        rom_data.write_bytes(snes_to_pc(0x88ED60), bytes(copy_buffer))

        #AreaMappingSMB1_LevelSelect: 0x88E840
        copy_buffer = rom_data.read_bytes(snes_to_pc(0x85d272), length=32)
        rom_data.write_bytes(snes_to_pc(0x88E840), bytes(copy_buffer))
        copy_buffer = rom_data.read_bytes(snes_to_pc(0x85d272), length=32)
        rom_data.write_bytes(snes_to_pc(0x88E860), bytes(copy_buffer))

        #SMB1 Pause Ending Cutscene Fix: 0x838AE6
        copy_buffer = rom_data.read_bytes(snes_to_pc(0x8d8862), length=6)
        rom_data.write_bytes(snes_to_pc(0x838AE6), bytes(copy_buffer))

        #SMB1NewLvlIDRelPtrs: 0x84BE90
        copy_buffer = rom_data.read_bytes(snes_to_pc(0x84c11c), length=8)
        rom_data.write_bytes(snes_to_pc(0x84BE90), bytes(copy_buffer))
        copy_buffer = rom_data.read_bytes(snes_to_pc(0x84c11c), length=8)
        for x in range(8):
            copy_buffer[x] = copy_buffer[x]+0x24
        rom_data.write_bytes(snes_to_pc(0x84BE98), bytes(copy_buffer))

        #SMB1NewLvlIDsTilesets: 0x84BEA0
        copy_buffer = rom_data.read_bytes(snes_to_pc(0x84c124), length=36)
        rom_data.write_bytes(snes_to_pc(0x84BEA0), bytes(copy_buffer))
        copy_buffer = rom_data.read_bytes(snes_to_pc(0x84c124), length=36)
        rom_data.write_bytes(snes_to_pc(0x84BEC4), bytes(copy_buffer))

        #SMB1NewLvlSprRelPtrs: 0x84BEE8
        copy_buffer = rom_data.read_bytes(snes_to_pc(0x84c148), length=4)
        for x in range(3):
            copy_buffer[x] = copy_buffer[x]+1
        rom_data.write_bytes(snes_to_pc(0x84BEE8), bytes(copy_buffer))

        #SMB1NewLvlSprDataPtrs_lo: 0x84BEEC
        copy_buffer = rom_data.read_bytes(snes_to_pc(0x84c14c), length=6)
        rom_data.write_bytes(snes_to_pc(0x84BEEC), bytes(copy_buffer))

        #SMB1NewLvlSprDataPtrs_lo2: 0x84BEF3
        copy_buffer = rom_data.read_bytes(snes_to_pc(0x84c152), length=28)
        rom_data.write_bytes(snes_to_pc(0x84BEF3), bytes(copy_buffer))

        #SMB1NewLvlSprDataPtrs_hi: 0x84BF10
        copy_buffer = rom_data.read_bytes(snes_to_pc(0x84c16e), length=6)
        rom_data.write_bytes(snes_to_pc(0x84BF10), bytes(copy_buffer))

        #SMB1NewLvlSprDataPtrs_hi2: 0x84BF17
        copy_buffer = rom_data.read_bytes(snes_to_pc(0x84c174), length=28)
        rom_data.write_bytes(snes_to_pc(0x84BF17), bytes(copy_buffer))

        #SMB1NewLvlBlkRelPtrs: 0x84BF34
        copy_buffer = rom_data.read_bytes(snes_to_pc(0x84c190), length=4)
        for x in range(3):
            copy_buffer[x+1] = copy_buffer[x+1]+1
        rom_data.write_bytes(snes_to_pc(0x84BF34), bytes(copy_buffer))

        #SMB1NewLvlBlkDataPtrs_lo: 0x84BF38
        copy_buffer = rom_data.read_bytes(snes_to_pc(0x84c194), length=3)
        rom_data.write_bytes(snes_to_pc(0x84BF38), bytes(copy_buffer))

        #SMB1NewLvlBlkDataPtrs_lo2: 0x84BF3B
        copy_buffer = rom_data.read_bytes(snes_to_pc(0x84c196), length=32)
        rom_data.write_bytes(snes_to_pc(0x84BF3B), bytes(copy_buffer))

        #SMB1NewLvlBlkDataPtrs_hi: 0x84BF5C
        copy_buffer = rom_data.read_bytes(snes_to_pc(0x84c1b6), length=3)
        rom_data.write_bytes(snes_to_pc(0x84BF5C), bytes(copy_buffer))

        #SMB1NewLvlBlkDataPtrs_hi2: 0x84BF5F
        copy_buffer = rom_data.read_bytes(snes_to_pc(0x84c1b8), length=32)
        rom_data.write_bytes(snes_to_pc(0x84BF5F), bytes(copy_buffer))

        #NewW8WaterSpriteData: 0x84FE90
        copy_buffer = rom_data.read_bytes(snes_to_pc(0x84c603), length=0x11)
        rom_data.write_bytes(snes_to_pc(0x84FE90), bytes(copy_buffer))

        #NewW8WaterSpriteData_0: 0x84FEA2
        copy_buffer = rom_data.read_bytes(snes_to_pc(0x84c615), length=2)
        rom_data.write_bytes(snes_to_pc(0x84FEA2), bytes(copy_buffer))

        #NewW8CastleLevelData: 0x84FEA4
        copy_buffer = rom_data.read_bytes(snes_to_pc(0x84cb01), length=0xff)
        rom_data.write_bytes(snes_to_pc(0x84FEA4), bytes(copy_buffer))

        #NewW8CastleLevelData_0: 0x84FFA3
        copy_buffer = rom_data.read_bytes(snes_to_pc(0x84caf0), length=0x11)
        rom_data.write_bytes(snes_to_pc(0x84FFA3), bytes(copy_buffer))

        #NewW8CastleSpriteData: 0x84FFB4
        copy_buffer = rom_data.read_bytes(snes_to_pc(0x84c287), length=0x28)
        for x in range(len(copy_buffer)):
            if copy_buffer[x] == 0x65:
                copy_buffer[x] = 0x66
            elif copy_buffer[x] == 0xe5:
                copy_buffer[x] = 0xe6
        rom_data.write_bytes(snes_to_pc(0x84FFB4), bytes(copy_buffer))

        #NewW8CastleSpriteData_0: 0x84FFDD
        copy_buffer = rom_data.read_bytes(snes_to_pc(0x84c2b0), length=0x0e)
        for x in range(len(copy_buffer)):
            if copy_buffer[x] == 0x65:
                copy_buffer[x] = 0x66
            elif copy_buffer[x] == 0xe5:
                copy_buffer[x] = 0xe6
        rom_data.write_bytes(snes_to_pc(0x84FFDD), bytes(copy_buffer))

        #NewW8CastleSpriteData_1: 0x84FFEB
        copy_buffer = rom_data.read_bytes(snes_to_pc(0x84c284), length=3)
        rom_data.write_bytes(snes_to_pc(0x84FFEB), bytes(copy_buffer))

        #AreaMappingSMBLL_Level: 0x88FD40
        copy_buffer = rom_data.read_bytes(snes_to_pc(0x8fe06d), length=52)
        for x in range(13):
            copy_buffer[(x*4)+1] = 1
        rom_data.write_bytes(snes_to_pc(0x88FD40), bytes(copy_buffer))

        #NewW8CastleSpriteDataL: 0x8EF900
        copy_buffer = rom_data.read_bytes(snes_to_pc(0x8ed438), length=61)
        rom_data.write_bytes(snes_to_pc(0x8EF900), bytes(copy_buffer))

        #NewW8CastleSpriteDataL_0: 0x8EF93D
        copy_buffer = rom_data.read_bytes(snes_to_pc(0x8ed435), length=3)
        rom_data.write_bytes(snes_to_pc(0x8EF93D), bytes(copy_buffer))

        #NewW8CastleLevelDataL: 0x8EF940
        copy_buffer = rom_data.read_bytes(snes_to_pc(0x8eda8f), length=0x16c)
        rom_data.write_bytes(snes_to_pc(0x8EF940), bytes(copy_buffer))

        #NewW8CastleLevelDataL_0: 0x8EFAAC
        copy_buffer = rom_data.read_bytes(snes_to_pc(0x8eda7e), length=0x11)
        rom_data.write_bytes(snes_to_pc(0x8EFAAC), bytes(copy_buffer))

        #NewWDCastleSpriteDataL: 0x8EFABD
        copy_buffer = rom_data.read_bytes(snes_to_pc(0x8ee6f7), length=44)
        rom_data.write_bytes(snes_to_pc(0x8EFABD), bytes(copy_buffer))

        #NewWDCastleSpriteDataL_0: 0x8EFAE9
        copy_buffer = rom_data.read_bytes(snes_to_pc(0x8ee6f4), length=3)
        rom_data.write_bytes(snes_to_pc(0x8EFAE9), bytes(copy_buffer))

        #NewWDCastleLevelDataL: 0x8EFAEC
        copy_buffer = rom_data.read_bytes(snes_to_pc(0x8eed15), length=0x100)
        rom_data.write_bytes(snes_to_pc(0x8EFAEC), bytes(copy_buffer))

        #NewWDCastleLevelDataL_0: 0x8EFBEC
        copy_buffer = rom_data.read_bytes(snes_to_pc(0x8eed04), length=0x11)
        rom_data.write_bytes(snes_to_pc(0x8EFBEC), bytes(copy_buffer))

        #Inventory Size Adjust (MiniChest/CardFlip): 0xA0F63E

        #Inventory Size Adjust (Toadhouse): 0xA7A8F3

        #Inventory Size Adjust (PeachLetter): 0xA9C42A

        #Inventory Size Adjust (Use Item): 0xA9DCF5

        #START SMB1/SMBLL Global Palettes
        copy_buffer = rom_data.read_bytes(snes_to_pc(0x8499fd), length=32)
        rom_data.write_bytes(snes_to_pc(0x84B023), bytes(copy_buffer))
        copy_buffer = rom_data.read_bytes(snes_to_pc(0x8499fd), length=32)
        rom_data.write_bytes(snes_to_pc(0x8EAE87), bytes(copy_buffer))

        #END SMB1/SMBLL Global Palettes

        #START SMB2 Ending Pause (Border)
        copy_buffer = rom_data.read_bytes(snes_to_pc(0x94c435), length=0x78)
        rom_data.write_bytes(snes_to_pc(0x94C00F), bytes(copy_buffer))

        #END SMB2 Ending Pause (Border)

        #START SMB2 Ending Pause (Fill)
        copy_buffer = rom_data.read_bytes(snes_to_pc(0x94c4ee), length=0x69)
        rom_data.write_bytes(snes_to_pc(0x94C11D), bytes(copy_buffer))

        #END SMB2 Ending Pause (Fill)

        #START SMB2 Options Pointers
        copy_buffer = rom_data.read_bytes(snes_to_pc(0x94dafc), length=6)
        rom_data.write_bytes(snes_to_pc(0x94FDEE), bytes(copy_buffer))
        copy_buffer = rom_data.read_bytes(snes_to_pc(0x94dbf1), length=2)
        rom_data.write_bytes(snes_to_pc(0x94FDF6), bytes(copy_buffer))
        copy_buffer = rom_data.read_bytes(snes_to_pc(0x94dbf3), length=2)
        rom_data.write_bytes(snes_to_pc(0x94FDFA), bytes(copy_buffer))

        #END SMB2 Options Pointers

        #START SMB2 Ending Save
        copy_buffer = rom_data.read_bytes(snes_to_pc(0x94db29), length=6)
        rom_data.write_bytes(snes_to_pc(0x94FE04), bytes(copy_buffer))

        #END SMB2 Ending Save

        #START SMB2 Reset (RAM Clear)
        copy_buffer = rom_data.read_bytes(snes_to_pc(0x8081ba), length=16)
        rom_data.write_bytes(snes_to_pc(0x94FE2F), bytes(copy_buffer))
        copy_buffer = rom_data.read_bytes(snes_to_pc(0x8081e9), length=30)
        rom_data.write_bytes(snes_to_pc(0x94FE3F), bytes(copy_buffer))

        #END SMB2 Reset (RAM Clear)

        #START SMB2 Tracker (Border)
        copy_buffer = rom_data.read_bytes(snes_to_pc(0x94c250), length=0x8c)
        rom_data.write_bytes(snes_to_pc(0x95D446), bytes(copy_buffer))

        #END SMB2 Tracker (Border)

        #START SMB2 Tracker (Fill)
        copy_buffer = rom_data.read_bytes(snes_to_pc(0x94c37c), length=0xaf)
        rom_data.write_bytes(snes_to_pc(0x95D4D2), bytes(copy_buffer))

        #END SMB2 Tracker (Fill)

        #START SMB3 Reset (RAM Clear)
        copy_buffer = rom_data.read_bytes(snes_to_pc(0x8081ba), length=16)
        rom_data.write_bytes(snes_to_pc(0xA9F1D0), bytes(copy_buffer))
        copy_buffer = rom_data.read_bytes(snes_to_pc(0x8081e9), length=30)
        rom_data.write_bytes(snes_to_pc(0xA9F1E0), bytes(copy_buffer))

        #END SMB3 Reset (RAM Clear)

        #START SMB3 Level Pause
        copy_buffer = rom_data.read_bytes(snes_to_pc(0xa9ef15), length=65)
        rom_data.write_bytes(snes_to_pc(0xA9EF64), bytes(copy_buffer))

        #END SMB3 Level Pause

        #NewSMB1BGsIndex: 0x85C637
        copy_buffer = rom_data.read_bytes(snes_to_pc(0x859122), length=6)
        rom_data.write_bytes(snes_to_pc(0x85C637), bytes(copy_buffer))
        copy_buffer = rom_data.read_bytes(snes_to_pc(0x859126), length=64)
        rom_data.write_bytes(snes_to_pc(0x85C63D), bytes(copy_buffer))
        copy_buffer = rom_data.read_bytes(snes_to_pc(0x859164), length=2)
        rom_data.write_bytes(snes_to_pc(0x85C67D), bytes(copy_buffer))

        #NewSMB1BGsBuffer: 0x85C67F
        copy_buffer = rom_data.read_bytes(snes_to_pc(0x8580e1), length=6)
        rom_data.write_bytes(snes_to_pc(0x85C67F), bytes(copy_buffer))
        copy_buffer = rom_data.read_bytes(snes_to_pc(0x8580e5), length=64)
        rom_data.write_bytes(snes_to_pc(0x85C685), bytes(copy_buffer))
        copy_buffer = rom_data.read_bytes(snes_to_pc(0x858123), length=2)
        rom_data.write_bytes(snes_to_pc(0x85C6C5), bytes(copy_buffer))

        #NewSMB1BGsRelative: 0x85C6C7
        copy_buffer = rom_data.read_bytes(snes_to_pc(0x85ad04), length=6)
        rom_data.write_bytes(snes_to_pc(0x85C6C7), bytes(copy_buffer))
        copy_buffer = rom_data.read_bytes(snes_to_pc(0x85ad08), length=64)
        rom_data.write_bytes(snes_to_pc(0x85C6CD), bytes(copy_buffer))
        copy_buffer = rom_data.read_bytes(snes_to_pc(0x85ad46), length=2)
        rom_data.write_bytes(snes_to_pc(0x85C70D), bytes(copy_buffer))

        #CopyData for SMB3 Map Tile VRAM Change:
        copy_buffer = rom_data.read_bytes(snes_to_pc(0xa9b049), length=3)
        rom_data.write_bytes(snes_to_pc(0x88FB53), bytes(copy_buffer))
        copy_buffer = rom_data.read_bytes(snes_to_pc(0xa9b04f), length=3)
        rom_data.write_bytes(snes_to_pc(0x88FB59), bytes(copy_buffer))
        copy_buffer = rom_data.read_bytes(snes_to_pc(0xa9b055), length=3)
        rom_data.write_bytes(snes_to_pc(0x88FB5F), bytes(copy_buffer))
        copy_buffer = rom_data.read_bytes(snes_to_pc(0xa9b05b), length=3)
        rom_data.write_bytes(snes_to_pc(0x88FB65), bytes(copy_buffer))

        #END for SMB3 Map Tile VRAM Change

        #START SMB3 Map Metatile Handling
        # Starting at Tile 16
        copy_buffer = rom_data.read_bytes(snes_to_pc(0xa1cf56+0x730), length=0x08)
        for x in range(4):
            copy_buffer[(x*2)+1] = copy_buffer[(x*2)+1]&0xe3
        rom_data.write_bytes(snes_to_pc(0xA1D006), bytes(copy_buffer)) # Handtrap Clear
        copy_buffer = rom_data.read_bytes(snes_to_pc(0xa1cf56+0x300), length=0x08)
        rom_data.write_bytes(snes_to_pc(0xA1D00E), bytes(copy_buffer)) # Fortress Clear
        copy_buffer = rom_data.read_bytes(snes_to_pc(0xa1cf56+0x340), length=0x18)
        for x in range(8):
            copy_buffer[(x*2)+1] = copy_buffer[(x*2)+1]&0xfb
        rom_data.write_bytes(snes_to_pc(0xA1D016), bytes(copy_buffer)) # Sandy Clears
        copy_buffer = rom_data.read_bytes(snes_to_pc(0xa1cf56+0x718), length=0x08)
        rom_data.write_bytes(snes_to_pc(0xA1D02E), bytes(copy_buffer)) # Alt Fort Clear
        # Tile 20
        copy_buffer = rom_data.read_bytes(snes_to_pc(0xa1cf56+0x280), length=0x08)
        rom_data.write_bytes(snes_to_pc(0xA1D056), bytes(copy_buffer)) # Yellow Mushroom House
        copy_buffer = rom_data.read_bytes(snes_to_pc(0xa1cf56+0x700), length=0x08)
        rom_data.write_bytes(snes_to_pc(0xA1D05E), bytes(copy_buffer)) # Red Mushroom House
        # Tile 23
        copy_buffer = rom_data.read_bytes(snes_to_pc(0xa1cf56+0x018), length=0x98)
        rom_data.write_bytes(snes_to_pc(0xA1D06E), bytes(copy_buffer)) # Normal Level Panels
        for x in range(len(copy_buffer)):
            if x&1 == 1:
                copy_buffer[x] = copy_buffer[x]&0xe3
        rom_data.write_bytes(snes_to_pc(0xa1cf56+0x018), bytes(copy_buffer)) # Normal Level Panels, Cleared
        # Tile 36
        copy_buffer = rom_data.read_bytes(snes_to_pc(0xa1cf56+0x730), length=0x08)
        rom_data.write_bytes(snes_to_pc(0xA1D106), bytes(copy_buffer)) # Handtrap
        copy_buffer = rom_data.read_bytes(snes_to_pc(0xa1cf56+0x338), length=0x20)
        rom_data.write_bytes(snes_to_pc(0xA1D10E), bytes(copy_buffer)) # Fortress & Sandy
        copy_buffer = rom_data.read_bytes(snes_to_pc(0xa1cf56+0x758), length=0x08)
        rom_data.write_bytes(snes_to_pc(0xA1D12E), bytes(copy_buffer)) # Alt Fortress

        #END SMB3 Map Metatile Handling

        # Finished Everything, return
        return rom_data.get_bytes()

    @staticmethod
    def postcopy_fixes(caller: APProcedurePatch, rom: bytes) -> bytes:
        # This step basically just fixes a few other things after we have copied and moved various data around.
        # Primarily, the SMB2 Pause Menu and SMB3's Map Tilemaps; the former since we added a new option and
        #  included additional counters, the latter due to remapping the MetaTiles.
        rom_data = RomData(rom)
        #SMB2 WORLD-LEVEL:
        rom_data.write_byte(snes_to_pc(0x94C200), 0x50)
        rom_data.write_byte(snes_to_pc(0x94C205), 0x60)

        #SMB2 LIVES COUNT:
        rom_data.write_byte(snes_to_pc(0x94C20B), 0x40)
        rom_data.write_byte(snes_to_pc(0x94C210), 0x40)

        #SMB2 PAUSE CURSORS 1-3:
        rom_data.write_byte(snes_to_pc(0x94C215), 0x58)
        rom_data.write_byte(snes_to_pc(0x94C216), 0x30)
        rom_data.write_byte(snes_to_pc(0x94C21A), 0x68)
        rom_data.write_byte(snes_to_pc(0x94C21F), 0x78)

        #SMB2 PAUSE CURSOR 4:
        rom_data.write_byte(snes_to_pc(0x94C224), 0x88)
        rom_data.write_byte(snes_to_pc(0x94C225), 0x11)
        rom_data.write_byte(snes_to_pc(0x94C226), 0x35)

        #SMB2 EGGCOUNT Y-POS:
        rom_data.write_byte(snes_to_pc(0x94C229), 0x40)
        rom_data.write_byte(snes_to_pc(0x94C22E), 0x40)
        rom_data.write_byte(snes_to_pc(0x94C233), 0x40)
        rom_data.write_byte(snes_to_pc(0x94C238), 0x40)

        #SMB2 EGGCOUNT X-POS:
        rom_data.write_byte(snes_to_pc(0x94C228), 0x78)
        rom_data.write_byte(snes_to_pc(0x94C22D), 0x80)
        rom_data.write_byte(snes_to_pc(0x94C232), 0x88)
        rom_data.write_byte(snes_to_pc(0x94C237), 0x90)

        #SMB2 EGGCOUNT PROPS:
        rom_data.write_byte(snes_to_pc(0x94C22B), 0x35)
        rom_data.write_byte(snes_to_pc(0x94C230), 0x35)
        rom_data.write_byte(snes_to_pc(0x94C235), 0x35)
        rom_data.write_byte(snes_to_pc(0x94C23A), 0x35)

        #SMB2 EGGCOUNT TILES:
        rom_data.write_byte(snes_to_pc(0x94C22A), 0x03)
        rom_data.write_byte(snes_to_pc(0x94C22F), 0x03)
        rom_data.write_byte(snes_to_pc(0x94C234), 0x03)
        rom_data.write_byte(snes_to_pc(0x94C239), 0x03)

        #SMB2 BOSS COINS COUNT:
        rom_data.write_byte(snes_to_pc(0x94C23E), 0x03)
        rom_data.write_byte(snes_to_pc(0x94C243), 0x03)
        rom_data.write_byte(snes_to_pc(0x94C23D), 0x48)
        rom_data.write_byte(snes_to_pc(0x94C242), 0x48)
        rom_data.write_byte(snes_to_pc(0x94C23C), 0xa8)
        rom_data.write_byte(snes_to_pc(0x94C241), 0xb0)

        #SMB2 PAUSE RED COINS:
        rom_data.write_byte(snes_to_pc(0x94C246), 0xa8)
        rom_data.write_byte(snes_to_pc(0x94C24B), 0xb0)
        rom_data.write_byte(snes_to_pc(0x94C248), 0x0b)
        rom_data.write_byte(snes_to_pc(0x94C24D), 0x03)
        rom_data.write_byte(snes_to_pc(0x94C249), 0x33)
        rom_data.write_byte(snes_to_pc(0x94C24E), 0x35)

        #SMB2 PAUSE WORLD-LEVEL MARKERS:
        rom_data.write_byte(snes_to_pc(0x94C2DC), 0x48)
        rom_data.write_byte(snes_to_pc(0x94C2DD), 0x40)
        rom_data.write_byte(snes_to_pc(0x94C2DE), 0x60)
        rom_data.write_byte(snes_to_pc(0x94C2DF), 0x34)
        rom_data.write_byte(snes_to_pc(0x94C2F5), 0x58)
        rom_data.write_byte(snes_to_pc(0x94C2F6), 0x40)
        rom_data.write_byte(snes_to_pc(0x94C2F7), 0x61)
        rom_data.write_byte(snes_to_pc(0x94C2F8), 0x34)

        #SMB2 PAUSE EGG ICON:
        rom_data.write_byte(snes_to_pc(0x94C2E1), 0x70)
        rom_data.write_byte(snes_to_pc(0x94C2E2), 0x40)
        rom_data.write_byte(snes_to_pc(0x94C2E3), 0x1a)
        rom_data.write_byte(snes_to_pc(0x94C2E4), 0x39)

        #SMB2 PAUSE BOSS COIN ICON:
        rom_data.write_byte(snes_to_pc(0x94C2E6), 0xa0)
        rom_data.write_byte(snes_to_pc(0x94C2E7), 0x48)
        rom_data.write_byte(snes_to_pc(0x94C2E8), 0x1b)
        rom_data.write_byte(snes_to_pc(0x94C2E9), 0x37)

        #SMB2 PAUSE LIFE ICON:
        rom_data.write_byte(snes_to_pc(0x94C2EB), 0xa0)
        rom_data.write_byte(snes_to_pc(0x94C2EC), 0x40)
        rom_data.write_byte(snes_to_pc(0x94C2ED), 0x17)
        rom_data.write_byte(snes_to_pc(0x94C2EE), 0x33)

        #'T' of 'TO CHAR. SEL.'
        rom_data.write_byte(snes_to_pc(0x94C2F0), 0x50)
        rom_data.write_byte(snes_to_pc(0x94C2F1), 0x88)
        rom_data.write_byte(snes_to_pc(0x94C2F2), 0x2a)

        #y-pos of 'CONTINUE'
        rom_data.write_byte(snes_to_pc(0x94C2FB), 0x58)
        rom_data.write_byte(snes_to_pc(0x94C300), 0x58)
        rom_data.write_byte(snes_to_pc(0x94C305), 0x58)
        rom_data.write_byte(snes_to_pc(0x94C314), 0x58)

        #'NUE' part of 'CONTINUE'
        rom_data.write_byte(snes_to_pc(0x94C30A), 0x58)
        rom_data.write_byte(snes_to_pc(0x94C30D), 0x02)

        #'O' of 'TO CHAR. SEL.'
        rom_data.write_byte(snes_to_pc(0x94C30E), 0x58)
        rom_data.write_byte(snes_to_pc(0x94C30F), 0x88)
        rom_data.write_byte(snes_to_pc(0x94C310), 0x28)

        #'S' of 'SAVE&CONTINUE'
        rom_data.write_byte(snes_to_pc(0x94C319), 0x68)

        #'AV' part of 'SAVE&CONTINUE'
        rom_data.write_byte(snes_to_pc(0x94C31E), 0x68)
        rom_data.write_byte(snes_to_pc(0x94C31F), 0x0c)
        rom_data.write_byte(snes_to_pc(0x94C321), 0x02)

        #'C' of 'TO CHAR. SEL.'
        rom_data.write_byte(snes_to_pc(0x94C322), 0x64)
        rom_data.write_byte(snes_to_pc(0x94C323), 0x88)
        rom_data.write_byte(snes_to_pc(0x94C324), 0x27)

        #'E&' part of 'SAVE&CONTINUE'
        rom_data.write_byte(snes_to_pc(0x94C328), 0x68)
        rom_data.write_byte(snes_to_pc(0x94C329), 0x0e)
        rom_data.write_byte(snes_to_pc(0x94C32B), 0x02)

        #'HA' of 'TO CHAR. SEL.'
        rom_data.write_byte(snes_to_pc(0x94C32C), 0x6c)
        rom_data.write_byte(snes_to_pc(0x94C32D), 0x88)
        rom_data.write_byte(snes_to_pc(0x94C32E), 0x21)
        rom_data.write_byte(snes_to_pc(0x94C32F), 0xb5)
        rom_data.write_byte(snes_to_pc(0x94C330), 0x02)

        #y-pos of 'CONTINUE' in 'SAVE&CONTINUE'
        rom_data.write_byte(snes_to_pc(0x94C332), 0x68)
        rom_data.write_byte(snes_to_pc(0x94C337), 0x68)
        rom_data.write_byte(snes_to_pc(0x94C33C), 0x68)
        rom_data.write_byte(snes_to_pc(0x94C34B), 0x68)

        #'NUE' part of 'CONTINUE' in 'SAVE&CONTINUE'
        rom_data.write_byte(snes_to_pc(0x94C341), 0x68)
        rom_data.write_byte(snes_to_pc(0x94C344), 0x02)

        #'R' of 'TO CHAR. SEL.'
        rom_data.write_byte(snes_to_pc(0x94C345), 0x7c)
        rom_data.write_byte(snes_to_pc(0x94C346), 0x88)
        rom_data.write_byte(snes_to_pc(0x94C347), 0x3f)

        #'S' of 'SAVE&QUIT'
        rom_data.write_byte(snes_to_pc(0x94C350), 0x78)

        #'AV' part of 'SAVE&QUIT'
        rom_data.write_byte(snes_to_pc(0x94C355), 0x78)
        rom_data.write_byte(snes_to_pc(0x94C356), 0x0c)
        rom_data.write_byte(snes_to_pc(0x94C358), 0x02)

        #first '.' of 'TO CHAR. SEL.'
        rom_data.write_byte(snes_to_pc(0x94C359), 0x84)
        rom_data.write_byte(snes_to_pc(0x94C35A), 0x88)
        rom_data.write_byte(snes_to_pc(0x94C35B), 0x2f)

        #'E&' part of 'SAVE&QUIT'
        rom_data.write_byte(snes_to_pc(0x94C35F), 0x78)
        rom_data.write_byte(snes_to_pc(0x94C360), 0x0e)
        rom_data.write_byte(snes_to_pc(0x94C362), 0x02)

        #'S' of 'TO CHAR. SEL.'
        rom_data.write_byte(snes_to_pc(0x94C363), 0x8c)
        rom_data.write_byte(snes_to_pc(0x94C364), 0x88)
        rom_data.write_byte(snes_to_pc(0x94C365), 0x37)

        #'QU' part of 'SAVE&QUIT'
        rom_data.write_byte(snes_to_pc(0x94C369), 0x78)
        rom_data.write_byte(snes_to_pc(0x94C36A), 0x23)
        rom_data.write_byte(snes_to_pc(0x94C36C), 0x02)

        #'E' of 'TO CHAR. SEL.'
        rom_data.write_byte(snes_to_pc(0x94C36D), 0x94)
        rom_data.write_byte(snes_to_pc(0x94C36E), 0x88)
        rom_data.write_byte(snes_to_pc(0x94C36F), 0x0e)

        #'IT' part of 'SAVE&QUIT'
        rom_data.write_byte(snes_to_pc(0x94C373), 0x78)
        rom_data.write_byte(snes_to_pc(0x94C374), 0x25)
        rom_data.write_byte(snes_to_pc(0x94C376), 0x02)

        #'L.' of 'TO CHAR. SEL.'
        rom_data.write_byte(snes_to_pc(0x94C377), 0x9c)
        rom_data.write_byte(snes_to_pc(0x94C378), 0x88)
        rom_data.write_byte(snes_to_pc(0x94C379), 0x3e)

        # SMB3 Map Tilemapping
        endpoint = 0xaaedb0-0xaae268
        tilemap_buffer = rom_data.read_bytes(snes_to_pc(0xaae268), length=endpoint)
        for i in range(len(tilemap_buffer)):
            #if tilemap_buffer[i] == 0x02: # blank tile
            #    tilemap_buffer[i] = 0x1f
            if tilemap_buffer[i] == 0x02: # tile used in World 8
                tilemap_buffer[i] = 0x02
            elif tilemap_buffer[i] == 0x01: # another tile in World 8
                tilemap_buffer[i] = 0x01
            elif tilemap_buffer[i] == 0x00: # Same as above
                tilemap_buffer[i] = 0x00
            elif tilemap_buffer[i] < 0x1f: # normal level panels
                tilemap_buffer[i] = tilemap_buffer[i]|0x20
            elif tilemap_buffer[i] == 0xe6: # handtrap tile
                tilemap_buffer[i] = 0x36
            elif tilemap_buffer[i] == 0x67: # fortress tile
                tilemap_buffer[i] = 0x37
            elif tilemap_buffer[i] == 0xeb: # alt fort tile
                tilemap_buffer[i] = 0x3b
            elif tilemap_buffer[i] == 0x68: # sand tile
                tilemap_buffer[i] = 0x38
            elif tilemap_buffer[i] == 0x69: # pyramid tile
                tilemap_buffer[i] = 0x39
            elif tilemap_buffer[i] == 0x6a: # unused tile
                tilemap_buffer[i] = 0x3a
        rom_data.write_bytes(snes_to_pc(0xaae268), bytes(tilemap_buffer))
        # Handle World 8's weird Tiles after the fact
        #rom_data.write_byte(snes_to_pc(0xaaeb27),0xd5) # Upward Path, from Navy
        #rom_data.write_byte(snes_to_pc(0xaaeb36),0xd6) # Rightward Path, to Navy
        #rom_data.write_byte(snes_to_pc(0xaaeb37),0xc1) # Standing Tile of Navy

        # Finished Everything, return
        return rom_data.get_bytes()

class SMASWProcedurePatch(APProcedurePatch, APTokenMixin):
    hash = [SMASWHASH]
    game = "Super Mario All-Stars + Super Mario World"
    patch_file_ending = ".apsmasw"
    result_file_ending = ".sfc"
    name: bytearray
    procedure = [
        ("prepare_gfx_prebasepatch", []),
        ("apply_basepatch", []),
        ("relocate_copy_data", []),
        ("postcopy_fixes", []),
        ("apply_tokens", ["token_patch.bin"]),
        ("calc_snes_crc", [])
    ]

    @classmethod
    def get_source_data(cls) -> bytes:
        return get_base_rom_bytes()

    def write_byte(self, offset: int, value: int) -> None:
        self.write_token(APTokenTypes.WRITE, offset, value.to_bytes(1, "little"))

    def write_bytes(self, offset: int, value: Iterable[int]) -> None:
        self.write_token(APTokenTypes.WRITE, offset, bytes(value))

    def copy_bytes(self, source: int, amount: int, destination: int) -> None:
        self.write_token(APTokenTypes.COPY, destination, (amount, source))



def patch_rom(world: "SMASWWorld", patch: SMASWProcedurePatch) -> None:
    # TODO: Tokens

    # Prepare Starting Inventory Stuff

    starting_items_smb1 = [0,0,0,0]
    for item in world.multiworld.precollected_items[world.player]:
        from .names import item_name
        from .items import world_keys, abilities, power_ups
        if item.name == item_name.key_prog_smb1:
            starting_items_smb1[0] = 1
        elif item.name == item_name.powerup_prog_smb1:
            starting_items_smb1[3] = 1
        elif item.name in world_keys and " (SMB1)" in item.name:
            if "World X" not in item.name:
                starting_items_smb1[0] |= 1<<(world_keys[item.name].idcode&7)
            else:
                if item.name in {item_name.key_world_x5_smb1,item_name.key_world_x6_smb1,item_name.key_world_x7_smb1,item_name.key_world_x8_smb1}:
                    starting_items_smb1[1] |= 1<<((world_keys[item.name].idcode&3)+4)
                else:
                    starting_items_smb1[1] |= 1<<(world_keys[item.name].idcode&3)
        elif item.name in abilities and " (SMB1)" in item.name:
            starting_items_smb1[2] |= 1<<(abilities[item.name].idcode&7)
        elif item.name in power_ups and " (SMB1)" in item.name:
            starting_items_smb1[3] |= 1<<(power_ups[item.name].idcode&7)

    starting_items_smbll = [0,0,0,0]
    for item in world.multiworld.precollected_items[world.player]:
        from .names import item_name
        from .items import world_keys, abilities, power_ups
        if item.name == item_name.key_prog_smbll:
            starting_items_smbll[0] = 1
        elif item.name == item_name.powerup_prog_smbll:
            starting_items_smbll[3] = 1
        elif item.name in world_keys and " (SMBLL)" in item.name:
            if item.name in {item_name.key_world_fantasy,item_name.key_world_a_smbll,item_name.key_world_b_smbll,item_name.key_world_c_smbll,item_name.key_world_d_smbll}:
                starting_items_smbll[1] |= 1<<(world_keys[item.name].idcode&7)
            else:
                starting_items_smbll[0] |= 1<<(world_keys[item.name].idcode&7)
        elif item.name in abilities and " (SMBLL)" in item.name:
            starting_items_smbll[2] |= 1<<(abilities[item.name].idcode&7)
        elif item.name in power_ups and " (SMBLL)" in item.name:
            starting_items_smbll[3] |= 1<<(power_ups[item.name].idcode&7)

    starting_items_smb2 = [0,0,0,0]
    for item in world.multiworld.precollected_items[world.player]:
        from .names import item_name
        from .items import world_keys, char_unlocks, abilities
        if item.name == item_name.key_prog_smb2:
            starting_items_smb2[0] = 1
        elif item.name in world_keys and " (SMB2)" in item.name:
            starting_items_smb2[0] |= 1<<(world_keys[item.name].idcode&7)
        elif item.name in abilities and " (SMB2)" in item.name:
            starting_items_smb2[2] |= 1<<(abilities[item.name].idcode&7)
        elif item.name in char_unlocks:
            starting_items_smb2[1] |= 1<<(char_unlocks[item.name].idcode&3)

    starting_items_smb3 = [0,0,0,0]
    for item in world.multiworld.precollected_items[world.player]:
        from .names import item_name
        from .items import world_keys, abilities, power_ups
        if item.name == item_name.key_prog_smb3:
            starting_items_smb3[0] = 1
        elif item.name in world_keys and " (SMB3)" in item.name:
            starting_items_smb3[0] |= 1<<(world_keys[item.name].idcode&7)
        elif item.name in abilities and " (SMB3)" in item.name:
            starting_items_smb3[2] |= 1<<(abilities[item].idcode&7)
        elif item.name in power_ups and " (SMB3)" in item.name:
            starting_items_smb3[3] |= 1<<(power_ups[item.name].idcode&7)

    # Preparing Prebuilt Save File since the game internally uses it to initialize SRAM
    prebuilt_saves = bytearray([0x00 for _ in range(0x400)])
    # Initialize "Current Selected World" for each Subgame
    prebuilt_saves[0x000+0x00] = 0xFF
    prebuilt_saves[0x01F+0x00] = 0xFF
    prebuilt_saves[0x03E+0x00] = 0xFF
    prebuilt_saves[0x05B+0x00] = 0xFF
    prebuilt_saves[0x361+0x79] = 0xFF
    # Initialize SMB3's "Outgoing World" Value
    prebuilt_saves[0x05B+0x7C] = 0x70
    # Handle Unlocks
    # SMB1
    prebuilt_saves[0x000+0x19] = starting_items_smb1[0]
    prebuilt_saves[0x000+0x1A] = starting_items_smb1[1]
    prebuilt_saves[0x000+0x1B] = starting_items_smb1[2]
    prebuilt_saves[0x000+0x1C] = starting_items_smb1[3]
    # SMBLL
    prebuilt_saves[0x01F+0x19] = starting_items_smbll[0]
    prebuilt_saves[0x01F+0x1A] = starting_items_smbll[1]
    prebuilt_saves[0x01F+0x1B] = starting_items_smbll[2]
    prebuilt_saves[0x01F+0x1C] = starting_items_smbll[3]
    # SMB2
    prebuilt_saves[0x03E+0x17] = starting_items_smb2[0]
    prebuilt_saves[0x03E+0x18] = starting_items_smb2[1]
    prebuilt_saves[0x03E+0x19] = starting_items_smb2[2]
    prebuilt_saves[0x03E+0x1A] = starting_items_smb2[3]
    # SMB3
    prebuilt_saves[0x05B+0x80] = starting_items_smb3[0]
    prebuilt_saves[0x05B+0x81] = starting_items_smb3[1]
    prebuilt_saves[0x05B+0x82] = starting_items_smb3[2]
    prebuilt_saves[0x05B+0x83] = starting_items_smb3[3]
    # SMW, not current implemented, so forced to 0
    prebuilt_saves[0x361+0x85] = 0x00
    prebuilt_saves[0x361+0x86] = 0x00
    prebuilt_saves[0x361+0x87] = 0x00
    prebuilt_saves[0x361+0x88] = 0x00
    # Handle SMB2's Starting Health
    for i in range(7):
        prebuilt_saves[0x03E+0x0C+i] = world.options.start_health_smb2.value
    # Handle Each Subgame's "Currently Unlocked Levels" except SMB3 and SMW
    # SMB1
    for i in range(16):
        prebuilt_saves[0x00+0x06+i] = 1
    # SMBLL
    for i in range(13):
        prebuilt_saves[0x1F+0x06+i] = 1
    # SMB2
    for i in range(7):
        prebuilt_saves[0x3E+0x04+i] = 1
    # Handle Starting Lives
    prebuilt_saves[0x000+0x03] = world.options.starting_lives_smb1.value-1
    prebuilt_saves[0x01F+0x03] = world.options.starting_lives_smbll.value-1
    prebuilt_saves[0x03E+0x02] = world.options.starting_lives_smb2.value
    prebuilt_saves[0x05B+0x02] = world.options.starting_lives_smb3.value-1
    #prebuilt_saves[0x361+0x00] = 0xFF

    patch.write_bytes(snes_to_pc(PREBUILT_SAVE),prebuilt_saves)

    # Write Lives Count to other areas (Saving Game, Game Over)
    patch.write_byte(snes_to_pc(0x808FA0),world.options.starting_lives_smb1.value-1)
    patch.write_byte(snes_to_pc(0x83A191),world.options.starting_lives_smb1.value-1)
    patch.write_byte(snes_to_pc(0x8090BF),world.options.starting_lives_smbll.value-1)
    patch.write_byte(snes_to_pc(0x8D9A21),world.options.starting_lives_smbll.value-1)
    patch.write_byte(snes_to_pc(0x809182),world.options.starting_lives_smb2.value)
    patch.write_byte(snes_to_pc(0x91816C),world.options.starting_lives_smb2.value)
    patch.write_byte(snes_to_pc(0x809263),world.options.starting_lives_smb3.value-1)
    patch.write_byte(snes_to_pc(0xA0945C),world.options.starting_lives_smb3.value-1)

    # Populate the Game's Item Tables
    items_in_locs = bytearray([0xFF for _ in range(0xC00)]) # Normal Locations
    for location in world.multiworld.get_locations(world.player):
        from .locations import BASE_OFFSET_NORMAL as LOC_DEX
        from .items import BASE_OFFSET as ITEM_ID_OFFSET
        if location.address is None:
            # There shouldn't be Event Locations in here, but who knows
            continue
        if location.item.player == location.player:
            # Inject our own Item into the Game
            items_in_locs[location.address-LOC_DEX] = location.item.code-ITEM_ID_OFFSET
        else:
            # Check if other Player's Item has certain Item Flags
            # The order this is checked in is important
            if location.item.advancement:
                item_id_this = 0xFD # Progression
            elif location.item.useful:
                item_id_this = 0xFE # Useful
            else:
                item_id_this = 0xFF # Anything Else
            items_in_locs[location.address-LOC_DEX] = item_id_this
    patch.write_bytes(snes_to_pc(CHECKS_ITEMS_ROM),items_in_locs)

    # Seed-Specific SMB1/SMBLL Final Level Stuff
    # SMB1, Level ID
    if world.options.goal_smb1.value == 1:
        patch.write_byte(snes_to_pc(0x84bee7),0x66)
    elif world.options.goal_smb1.value == 2:
        patch.write_byte(snes_to_pc(0x84bec3),0x66)
    # SMBLL, Level Data Pointers
    if world.options.goal_smbll.value == 0x08:
        # Note: World D Castle
        # Sprite Data
        patch.write_byte(snes_to_pc(0x8ec4f7+6),0xbd)
        patch.write_byte(snes_to_pc(0x8ec53e+6),0xfa)
        # Level Data
        patch.write_byte(snes_to_pc(0x8ec589+6),0xec)
        patch.write_byte(snes_to_pc(0x8ec5d0+6),0xfa)
    elif world.options.goal_smbll.value == 0x10:
        # Note: World 8 Castle
        # Sprite Data
        patch.write_byte(snes_to_pc(0x8ec4f7),0x00)
        patch.write_byte(snes_to_pc(0x8ec53e),0xf9)
        # Level Data
        patch.write_byte(snes_to_pc(0x8ec589),0x40)
        patch.write_byte(snes_to_pc(0x8ec5d0),0xf9)

    # Handle Subgame Locks
    # TODO: See if there is a better way to do this...
    currently_placed_locks = 0
    locks_mask_buffer = [0,0,0,0]
    locks_xlow_buffer = [0,0,0,0]
    locks_xhigh_buffer = [0,0,0,0]
    for lock_dex in range(4):
        for subgame_dex in range(5):
            if subgame_dex == 0 and currently_placed_locks&1 != 1:
                if world.options.unlocked_smb1.value == 0:
                    locks_mask_buffer[lock_dex] = lock_game_mask[subgame_dex]
                    locks_xlow_buffer[lock_dex] = lock_game_x_low[subgame_dex]
                    locks_xhigh_buffer[lock_dex] = lock_game_x_high[subgame_dex]
                    currently_placed_locks |= 1<<subgame_dex
                    break
            elif subgame_dex == 1 and currently_placed_locks&2 != 2:
                if world.options.unlocked_smbll.value == 0:
                    locks_mask_buffer[lock_dex] = lock_game_mask[subgame_dex]
                    locks_xlow_buffer[lock_dex] = lock_game_x_low[subgame_dex]
                    locks_xhigh_buffer[lock_dex] = lock_game_x_high[subgame_dex]
                    currently_placed_locks |= 1<<subgame_dex
                    break
            elif subgame_dex == 2 and currently_placed_locks&4 != 4:
                if world.options.unlocked_smb2.value == 0:
                    locks_mask_buffer[lock_dex] = lock_game_mask[subgame_dex]
                    locks_xlow_buffer[lock_dex] = lock_game_x_low[subgame_dex]
                    locks_xhigh_buffer[lock_dex] = lock_game_x_high[subgame_dex]
                    currently_placed_locks |= 1<<subgame_dex
                    break
            elif subgame_dex == 3 and currently_placed_locks&8 != 8:
                if world.options.unlocked_smb3.value == 0:
                    locks_mask_buffer[lock_dex] = lock_game_mask[subgame_dex]
                    locks_xlow_buffer[lock_dex] = lock_game_x_low[subgame_dex]
                    locks_xhigh_buffer[lock_dex] = lock_game_x_high[subgame_dex]
                    currently_placed_locks |= 1<<subgame_dex
                    break
            elif subgame_dex == 4 and currently_placed_locks&16 != 16:
                if world.options.unlocked_smw.value == 0:
                    locks_mask_buffer[lock_dex] = lock_game_mask[subgame_dex]
                    locks_xlow_buffer[lock_dex] = lock_game_x_low[subgame_dex]
                    locks_xhigh_buffer[lock_dex] = lock_game_x_high[subgame_dex]
                    currently_placed_locks |= 1<<subgame_dex
                    break
        #continue
    # Another For Loop, to catch unplaced areas
    for lock_dex in range(4):
        if locks_mask_buffer[lock_dex] == 0:
            if lock_dex == 0: # All games are available and unlocked, place dummy
                locks_mask_buffer[0] = lock_game_mask[5]
                locks_xlow_buffer[0] = lock_game_x_low[5]
                locks_xhigh_buffer[0] = lock_game_x_high[5]
            else:
                locks_mask_buffer[lock_dex] = locks_mask_buffer[lock_dex-1]
                locks_xlow_buffer[lock_dex] = locks_xlow_buffer[lock_dex-1]
                locks_xhigh_buffer[lock_dex] = locks_xhigh_buffer[lock_dex-1]
    patch.write_bytes(snes_to_pc(LOCK_GAME_MASK),locks_mask_buffer)
    patch.write_bytes(snes_to_pc(LOCK_X_POS_LOW),locks_xlow_buffer)
    patch.write_bytes(snes_to_pc(LOCK_X_POS_HIGH),locks_xhigh_buffer)

    # Per-Game Options
    subgames_available = (world.options.available_smb1 + world.options.available_smbll + world.options.available_smb2 + world.options.available_smb3 + world.options.available_smw)&0xFF
    patch.write_byte(snes_to_pc(GAME_AVAILABILITY),subgames_available)
    subgames_goals = world.options.goal_smb1 + world.options.goal_smbll + world.options.goal_smb2 + world.options.goal_smb3 + world.options.goal_smw
    patch.write_byte(snes_to_pc(GAME_GOAL_SETTINGS),subgames_goals&0xFF)
    patch.write_byte(snes_to_pc(GAME_GOAL_SETTINGS+1),(subgames_goals>>8)&0xFF)
    subgames_required = (world.options.required_smb1 + world.options.required_smbll + world.options.required_smb2 + world.options.required_smb3 + world.options.required_smw)&0xFF
    patch.write_byte(snes_to_pc(GAME_GOAL_SETTINGS+2),subgames_required)
    patch.write_byte(snes_to_pc(GAME_GOAL_SETTINGS+3),world.options.goal_smasw_count.value)
    subgame_settings_buffer = [0,0,0,0]
    # SMB1
    subgame_settings_buffer[0] |= world.options.prog_powerups_smb1.value
    subgame_settings_buffer[0] |= world.options.prog_keys_smb1.value<<1
    subgame_settings_buffer[0] |= world.options.hard_worlds_smb1.value<<2
    # TODO: Area Shuffles into Byte 0
    subgame_settings_buffer[1] |= world.options.dupeswap_keys_smb1.value
    # TODO: Warpzone and Enemy Difficulty in Byte 1
    # TODO: Other Logic Settings in Byte 2
    subgame_settings_buffer[3] |= world.options.save_lives_smb1.value<<5
    subgame_settings_buffer[3] |= world.options.save_coins_smb1.value<<6
    subgame_settings_buffer[3] |= world.options.save_powers_smb1.value<<7
    # TODO: Other QOL Settings in Byte 3
    patch.write_bytes(snes_to_pc(SMB1_SETTINGS),subgame_settings_buffer)
    subgame_settings_buffer = [0,0,0,0]
    # SMBLL
    subgame_settings_buffer[0] |= world.options.prog_powerups_smbll.value
    subgame_settings_buffer[0] |= world.options.prog_keys_smbll.value<<1
    subgame_settings_buffer[0] |= world.options.bonus_worlds_smbll.value<<2
    subgame_settings_buffer[0] |= world.options.fantasy_world_smbll.value<<4
    # TODO: Area Shuffles into Byte 0
    # TODO: Warpzone and Enemy Difficulty in Byte 1
    # TODO: Other Logic Settings in Byte 2
    subgame_settings_buffer[3] |= world.options.save_lives_smbll.value<<5
    subgame_settings_buffer[3] |= world.options.save_coins_smbll.value<<6
    subgame_settings_buffer[3] |= world.options.save_powers_smbll.value<<7
    # TODO: Other QOL Settings in Byte 3
    patch.write_bytes(snes_to_pc(SMBLL_SETTINGS),subgame_settings_buffer)
    subgame_settings_buffer = [0,0,0,0]
    # SMB2
    subgame_settings_buffer[0] |= world.options.prog_health_smb2.value
    subgame_settings_buffer[0] |= world.options.prog_keys_smb2.value<<1
    subgame_settings_buffer[0] |= (world.options.max_health_smb2.value-1)<<2
    # TODO: Area Shuffles into Byte 0
    subgame_settings_buffer[1] |= world.options.char_select_checks_smb2.value
    subgame_settings_buffer[1] |= (world.options.grab_behavior_smb2.value&1)<<3
    # TODO: Warpzone in Byte 1
    # TODO: Other Logic Settings in Byte 2 (Sanities, Extra Mushrooms)
    subgame_settings_buffer[3] |= world.options.save_lives_smb2.value<<5
    subgame_settings_buffer[3] |= world.options.save_coins_smb2.value<<6
    # TODO: Other QOL Settings in Byte 3? Can't really think of any
    patch.write_bytes(snes_to_pc(SMB2_SETTINGS),subgame_settings_buffer)
    subgame_settings_buffer = [0,0,0,0]
    # SMB3
    subgame_settings_buffer[0] |= world.options.prog_keys_smb3.value<<1
    # TODO: Other Logic Settings in Byte 0 (Power-Up Requirements, Power-Down?)
    # TODO: Area Shuffles into Byte 0
    # TODO: Warpzone in Byte 1
    # TODO: Other Logic Settings in Byte 2 (Sanities, Mostly)
    subgame_settings_buffer[3] |= world.options.save_lives_smb3.value<<5
    subgame_settings_buffer[3] |= world.options.save_coins_smb3.value<<6
    subgame_settings_buffer[3] |= world.options.save_powers_smb3.value<<7
    # TODO: Other QOL Settings in Byte 3 (inventory type, mostly)
    patch.write_bytes(snes_to_pc(SMB3_SETTINGS),subgame_settings_buffer)
    subgame_settings_buffer = [0,0,0,0]
    # SMW, not currently implemented, forced to zero
    #subgame_settings_buffer[0] |= world.options.prog_powerups_smb1.value
    #subgame_settings_buffer[0] |= world.options.prog_keys_smb1.value<<1
    #subgame_settings_buffer[0] |= world.options.hard_worlds_smb1.value<<2
    ## TODO: Area Shuffles into Byte 0
    #subgame_settings_buffer[1] |= world.options.dupeswap_keys_smb1.value
    ## TODO: Other Logic Settings in Byte 2
    #subgame_settings_buffer[3] |= world.options.save_lives_smw.value<<5
    #subgame_settings_buffer[3] |= world.options.save_coins_smw.value<<6
    #subgame_settings_buffer[3] |= world.options.save_powers_smw.value<<7
    ## TODO: Other QOL Settings in Byte 3
    patch.write_bytes(snes_to_pc(SMW_SETTINGS),subgame_settings_buffer)
    # Eggs, not currently implemented, so all Zeroes
    subgame_egghunt_buffer = [0,0]
    patch.write_bytes(snes_to_pc(GAME_EGG_MAX+0),subgame_egghunt_buffer)
    patch.write_bytes(snes_to_pc(GAME_EGG_MAX+2),subgame_egghunt_buffer)
    patch.write_bytes(snes_to_pc(GAME_EGG_MAX+4),subgame_egghunt_buffer)
    patch.write_bytes(snes_to_pc(GAME_EGG_MAX+6),subgame_egghunt_buffer)
    patch.write_bytes(snes_to_pc(GAME_EGG_MAX+8),subgame_egghunt_buffer)
    subgame_egghunt_buffer = [0,0]
    patch.write_bytes(snes_to_pc(GAME_EGG_REQUIRED+0),subgame_egghunt_buffer)
    patch.write_bytes(snes_to_pc(GAME_EGG_REQUIRED+2),subgame_egghunt_buffer)
    patch.write_bytes(snes_to_pc(GAME_EGG_REQUIRED+4),subgame_egghunt_buffer)
    patch.write_bytes(snes_to_pc(GAME_EGG_REQUIRED+6),subgame_egghunt_buffer)
    patch.write_bytes(snes_to_pc(GAME_EGG_REQUIRED+8),subgame_egghunt_buffer)
    # Boss Coins Required, converted into Binary-Coded-Decimal Format
    subgame_bosscoin_buffer = world.options.bosscoin_smb1.value % 10
    subgame_bosscoin_buffer |= (world.options.bosscoin_smb1.value // 10)<<4
    patch.write_byte(snes_to_pc(GAME_BOSS_COINS_REQUIRED+0),subgame_bosscoin_buffer)
    subgame_bosscoin_buffer = world.options.bosscoin_smbll.value % 10
    subgame_bosscoin_buffer |= (world.options.bosscoin_smbll.value // 10)<<4
    patch.write_byte(snes_to_pc(GAME_BOSS_COINS_REQUIRED+1),subgame_bosscoin_buffer)
    subgame_bosscoin_buffer = world.options.bosscoin_smb2.value % 10
    subgame_bosscoin_buffer |= (world.options.bosscoin_smb2.value // 10)<<4
    patch.write_byte(snes_to_pc(GAME_BOSS_COINS_REQUIRED+2),subgame_bosscoin_buffer)
    subgame_bosscoin_buffer = world.options.bosscoin_smb3.value % 10
    subgame_bosscoin_buffer |= (world.options.bosscoin_smb3.value // 10)<<4
    patch.write_byte(snes_to_pc(GAME_BOSS_COINS_REQUIRED+3),subgame_bosscoin_buffer)
    #subgame_bosscoin_buffer = world.options.bosscoin_smw.value % 10
    #subgame_bosscoin_buffer |= (world.options.bosscoin_smw.value // 10)<<4
    subgame_bosscoin_buffer = 0 # SMW is not currently implemented
    patch.write_byte(snes_to_pc(GAME_BOSS_COINS_REQUIRED+4),subgame_bosscoin_buffer)
    # Maximum Number of Checks, per Subgame, in BCD; not currently implemented yet
    subgame_checks_count = [0,0,0,0]
    patch.write_bytes(snes_to_pc(GAME_CHECKS_MAX+0),subgame_checks_count)
    patch.write_bytes(snes_to_pc(GAME_CHECKS_MAX+4),subgame_checks_count)
    patch.write_bytes(snes_to_pc(GAME_CHECKS_MAX+8),subgame_checks_count)
    patch.write_bytes(snes_to_pc(GAME_CHECKS_MAX+12),subgame_checks_count)
    patch.write_bytes(snes_to_pc(GAME_CHECKS_MAX+16),subgame_checks_count)
    # Handle "Remote Item" Settings, not currently implemented yet, so just 0
    patch.write_byte(snes_to_pc(REMOTE_ITEM_SETTING),0)
    # Handle Deathlink Settings, not currently implemented yet
    patch.write_byte(snes_to_pc(DEATHLINK_SETTING+0),0)
    patch.write_byte(snes_to_pc(DEATHLINK_SETTING+1),0)
    patch.write_byte(snes_to_pc(DEATHLINK_SETTING+2),0)
    patch.write_byte(snes_to_pc(DEATHLINK_SETTING+3),0) # just an alignment byte, may become DamageLink Setting

    from Utils import __version__
    patch.name = bytearray(f'SMASW{__version__.replace(".", "")[0:3]}_{world.player}_{world.multiworld.seed:13}\0', 'utf8')[:21]
    patch.name.extend([0] * (21 - len(patch.name)))
    patch.write_bytes(0x7FC0, patch.name)

    # Handle writing stuff for the Title Screen Display

    # Write Seed (multiworld.seed_name)
    local_seed_name = world.multiworld.seed_name
    local_seed_name = local_seed_name.strip('W')
    if len(world.multiworld.seed_name) > 20:
        patch.copy_bytes(snes_to_pc(0x0CF800+0x200),0x10,0xD7200+0x480)
        patch.copy_bytes(snes_to_pc(0x0CF800+0x280),0x10,0xD7200+0x490)
    else: # Not Webworld Generation, make this an empty tile
        patch.copy_bytes(snes_to_pc(0x0CF800+0x280),0x10,0xD7200+0x480)
        patch.copy_bytes(snes_to_pc(0x0CF800+0x280),0x10,0xD7200+0x490)

    for i in range(20):
        char = local_seed_name[i]
        tile = i*32
        # Special case if lower two or upper two digits
        if i < 2:
            patch.copy_bytes(snes_to_pc(0x0CF800+title_text_gfx_loc[char]),0x10,0xD7200+0x400+tile)
            patch.copy_bytes(snes_to_pc(0x0CF800+0x280),0x10,0xD7200+0x410+tile)
        elif i >= 18:
            patch.copy_bytes(snes_to_pc(0x0CF800+title_text_gfx_loc[char]),0x10,0xD7200+0x440+tile-0x240)
            patch.copy_bytes(snes_to_pc(0x0CF800+0x280),0x10,0xD7200+0x450+tile-0x240)
        else:
            patch.copy_bytes(snes_to_pc(0x0CF800+title_text_gfx_loc[char]),0x10,0xD7200+0x200+tile-0x40)
            patch.copy_bytes(snes_to_pc(0x0CF800+0x280),0x10,0xD7200+0x210+tile-0x40)

    # Write Player Name
    local_slot_name = world.multiworld.get_player_name(world.player)
    local_slot_name = local_slot_name.upper()
    local_slot_name = local_slot_name.encode("ascii","replace")
    local_slot_name = local_slot_name.decode("utf-8","replace")

    for i in range(16):
        if i < len(local_slot_name):
            char = local_slot_name[i]
        else:
            char = " "
        tile = i*32
        if char not in title_text_gfx_loc:
            patch.copy_bytes(snes_to_pc(0x0CF800+0x2A0),0x10,0xD7200+tile)
            patch.copy_bytes(snes_to_pc(0x0CF800+0x280),0x10,0xD7200+0x10+tile)
        else:
            patch.copy_bytes(snes_to_pc(0x0CF800+title_text_gfx_loc[char]),0x10,0xD7200+tile)
            patch.copy_bytes(snes_to_pc(0x0CF800+0x280),0x10,0xD7200+0x10+tile)

    # Write the "SEED" and "SLOT" tiles, these are static
    patch.copy_bytes(snes_to_pc(0x0CF800+title_text_gfx_loc["S"]),0x10,0xD7800)
    patch.copy_bytes(snes_to_pc(0x0CF800+0x280),0x10,0xD7810)
    patch.copy_bytes(snes_to_pc(0x0CF800+title_text_gfx_loc["L"]),0x10,0xD7820)
    patch.copy_bytes(snes_to_pc(0x0CF800+0x280),0x10,0xD7830)
    patch.copy_bytes(snes_to_pc(0x0CF800+title_text_gfx_loc["O"]),0x10,0xD7840)
    patch.copy_bytes(snes_to_pc(0x0CF800+0x280),0x10,0xD7850)
    patch.copy_bytes(snes_to_pc(0x0CF800+title_text_gfx_loc["T"]),0x10,0xD7860)
    patch.copy_bytes(snes_to_pc(0x0CF800+0x280),0x10,0xD7870)
    patch.copy_bytes(snes_to_pc(0x0CF800+title_text_gfx_loc["S"]),0x10,0xD7A00)
    patch.copy_bytes(snes_to_pc(0x0CF800+0x280),0x10,0xD7A10)
    patch.copy_bytes(snes_to_pc(0x0CF800+title_text_gfx_loc["E"]),0x10,0xD7A20)
    patch.copy_bytes(snes_to_pc(0x0CF800+0x280),0x10,0xD7A30)
    patch.copy_bytes(snes_to_pc(0x0CF800+title_text_gfx_loc["E"]),0x10,0xD7A40)
    patch.copy_bytes(snes_to_pc(0x0CF800+0x280),0x10,0xD7A50)
    patch.copy_bytes(snes_to_pc(0x0CF800+title_text_gfx_loc["D"]),0x10,0xD7A60)
    patch.copy_bytes(snes_to_pc(0x0CF800+0x280),0x10,0xD7A70)

    # Writing the Version stuff
    patch.copy_bytes(snes_to_pc(0x0CF800+title_text_gfx_loc["V"]),0x10,0xD7880)
    patch.copy_bytes(snes_to_pc(0x0CF800+0x280),0x10,0xD7890)
    # Write Beta Version Identifier
    if len(APWORLD_BETA) > 0:
        for i in range(2):
            if i < len(APWORLD_BETA):
                char = APWORLD_BETA[i]
            else:
                char = " "
            tile = i*32
            patch.copy_bytes(snes_to_pc(0x0CF800+title_text_gfx_loc[char]),0x10,0xD7940+tile)
            patch.copy_bytes(snes_to_pc(0x0CF800+0x280),0x10,0xD7940+0x10+tile)
    # Write Normal Version Identifier
    for i in range(8):
        char = APWORLD_VERS[i]
        tile = i*32
        patch.copy_bytes(snes_to_pc(0x0CF800+title_text_gfx_loc[char]),0x10,0xD7A80+tile)
        patch.copy_bytes(snes_to_pc(0x0CF800+0x280),0x10,0xD7A80+0x10+tile)


    patch.write_file("token_patch.bin", patch.get_token_binary())


def get_base_rom_bytes(file_name: str = "") -> bytes:
    base_rom_bytes = getattr(get_base_rom_bytes, "base_rom_bytes", None)
    if not base_rom_bytes:
        file_name = get_base_rom_path(file_name)
        base_rom_bytes = bytes(Utils.read_snes_rom(open(file_name, "rb")))

        basemd5 = hashlib.md5()
        basemd5.update(base_rom_bytes)
        print(basemd5.hexdigest())
        #if basemd5.hexdigest() not in {SMASWHASH}: #TODO: Expand when we incorporate more game versions
        if SMASWHASH != basemd5.hexdigest(): #TODO: Expand when we incorporate more game versions
            raise Exception("Supplied Base Rom does not match known MD5 for US release. "
                                "Get the correct game and version, then dump it")
        get_base_rom_bytes.base_rom_bytes = base_rom_bytes
    return base_rom_bytes

def get_base_rom_path(file_name: str = "") -> str:
    options: settings.Settings = settings.get_settings()
    if not file_name:
        file_name = options["smasw_options"]["rom_file"]
    if not os.path.exists(file_name):
        file_name = Utils.user_path(file_name)
    return file_name