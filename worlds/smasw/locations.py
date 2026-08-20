from __future__ import annotations

import typing
from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from . import items
from .names import location_name as loc_name
from .names import item_name
from .options import GoalSmb1, GoalSmbll

if TYPE_CHECKING:
    from .world import SMASWWorld

## Every location must have a unique integer ID associated with it.
## We will have a lookup from location name to ID here that, in world.py, we will import and bind to the world class.
## Even if a location doesn't exist on specific options, it must be present in this lookup.
#LOCATION_NAME_TO_ID = {
#    "Top Left Room Chest": 1,
#    "Top Middle Chest": 2,
#    "Bottom Left Chest": 3,
#    "Bottom Left Extra Chest": 4,
#    "Bottom Right Room Left Chest": 5,
#    "Bottom Right Room Right Chest": 6,
#    # Location IDs don't need to be sequential, as long as they're unique and greater than 0.
#    "Right Room Enemy Drop": 10,
#}

# TODO: Thing
#class LocData(typing.NamedTuple):
#    idcode: typing.Optional[int]
#    group: typing.Optional[str]


# Each Location instance must correctly report the "game" it belongs to.
# To make this simple, it is common practice to subclass the basic Location class and override the "game" field.
class SMASWLocation(Location):
    game = "Super Mario All-Stars + Super Mario World"

# Some Offsets
# These are based on SRAM Addresses, each byte has 8 bits
BASE_OFFSET_SRAM = 0xF00000<<3
BASE_OFFSET_NORMAL = 0xF01000<<3
GAME_OFFSET_SMB1_NORMAL = 0x000<<3
GAME_OFFSET_SMBLL_NORMAL = 0x020<<3
GAME_OFFSET_SMB2_NORMAL = 0x040<<3
GAME_OFFSET_SMB3_NORMAL = 0x080<<3
GAME_OFFSET_SMW_NORMAL = 0x100<<3


# SMB1 Locations
# Level Clears are on Even Numbers (Zero Included), Reds are Odds
normal_loc_smb1_reg_world = {
    loc_name.loc_world_1_1_smb1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB1_NORMAL + 0x00,
    loc_name.loc_world_1_2_smb1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB1_NORMAL + 0x02,
    loc_name.loc_world_1_3_smb1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB1_NORMAL + 0x04,
    loc_name.loc_world_1_4_smb1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB1_NORMAL + 0x06,
    loc_name.loc_world_2_1_smb1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB1_NORMAL + 0x08,
    loc_name.loc_world_2_2_smb1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB1_NORMAL + 0x0a,
    loc_name.loc_world_2_3_smb1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB1_NORMAL + 0x0c,
    loc_name.loc_world_2_4_smb1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB1_NORMAL + 0x0e,
    loc_name.loc_world_3_1_smb1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB1_NORMAL + 0x10,
    loc_name.loc_world_3_2_smb1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB1_NORMAL + 0x12,
    loc_name.loc_world_3_3_smb1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB1_NORMAL + 0x14,
    loc_name.loc_world_3_4_smb1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB1_NORMAL + 0x16,
    loc_name.loc_world_4_1_smb1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB1_NORMAL + 0x18,
    loc_name.loc_world_4_2_smb1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB1_NORMAL + 0x1a,
    loc_name.loc_world_4_3_smb1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB1_NORMAL + 0x1c,
    loc_name.loc_world_4_4_smb1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB1_NORMAL + 0x1e,
    loc_name.loc_world_5_1_smb1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB1_NORMAL + 0x20,
    loc_name.loc_world_5_2_smb1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB1_NORMAL + 0x22,
    loc_name.loc_world_5_3_smb1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB1_NORMAL + 0x24,
    loc_name.loc_world_5_4_smb1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB1_NORMAL + 0x26,
    loc_name.loc_world_6_1_smb1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB1_NORMAL + 0x28,
    loc_name.loc_world_6_2_smb1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB1_NORMAL + 0x2a,
    loc_name.loc_world_6_3_smb1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB1_NORMAL + 0x2c,
    loc_name.loc_world_6_4_smb1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB1_NORMAL + 0x2e,
    loc_name.loc_world_7_1_smb1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB1_NORMAL + 0x30,
    loc_name.loc_world_7_2_smb1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB1_NORMAL + 0x32,
    loc_name.loc_world_7_3_smb1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB1_NORMAL + 0x34,
    loc_name.loc_world_7_4_smb1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB1_NORMAL + 0x36,
    loc_name.loc_world_8_1_smb1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB1_NORMAL + 0x38,
    loc_name.loc_world_8_2_smb1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB1_NORMAL + 0x3a,
    loc_name.loc_world_8_3_smb1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB1_NORMAL + 0x3c,
    loc_name.loc_world_8_4_smb1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB1_NORMAL + 0x3e,
}
normal_loc_smb1_hard_world = {
    loc_name.loc_world_1x1_smb1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB1_NORMAL + 0x40,
    loc_name.loc_world_1x2_smb1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB1_NORMAL + 0x42,
    loc_name.loc_world_1x3_smb1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB1_NORMAL + 0x44,
    loc_name.loc_world_1x4_smb1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB1_NORMAL + 0x46,
    loc_name.loc_world_2x1_smb1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB1_NORMAL + 0x48,
    loc_name.loc_world_2x2_smb1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB1_NORMAL + 0x4a,
    loc_name.loc_world_2x3_smb1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB1_NORMAL + 0x4c,
    loc_name.loc_world_2x4_smb1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB1_NORMAL + 0x4e,
    loc_name.loc_world_3x1_smb1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB1_NORMAL + 0x50,
    loc_name.loc_world_3x2_smb1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB1_NORMAL + 0x52,
    loc_name.loc_world_3x3_smb1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB1_NORMAL + 0x54,
    loc_name.loc_world_3x4_smb1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB1_NORMAL + 0x56,
    loc_name.loc_world_4x1_smb1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB1_NORMAL + 0x58,
    loc_name.loc_world_4x2_smb1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB1_NORMAL + 0x5a,
    loc_name.loc_world_4x3_smb1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB1_NORMAL + 0x5c,
    loc_name.loc_world_4x4_smb1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB1_NORMAL + 0x5e,
    loc_name.loc_world_5x1_smb1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB1_NORMAL + 0x60,
    loc_name.loc_world_5x2_smb1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB1_NORMAL + 0x62,
    loc_name.loc_world_5x3_smb1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB1_NORMAL + 0x64,
    loc_name.loc_world_5x4_smb1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB1_NORMAL + 0x66,
    loc_name.loc_world_6x1_smb1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB1_NORMAL + 0x68,
    loc_name.loc_world_6x2_smb1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB1_NORMAL + 0x6a,
    loc_name.loc_world_6x3_smb1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB1_NORMAL + 0x6c,
    loc_name.loc_world_6x4_smb1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB1_NORMAL + 0x6e,
    loc_name.loc_world_7x1_smb1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB1_NORMAL + 0x70,
    loc_name.loc_world_7x2_smb1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB1_NORMAL + 0x72,
    loc_name.loc_world_7x3_smb1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB1_NORMAL + 0x74,
    loc_name.loc_world_7x4_smb1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB1_NORMAL + 0x76,
    loc_name.loc_world_8x1_smb1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB1_NORMAL + 0x78,
    loc_name.loc_world_8x2_smb1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB1_NORMAL + 0x7a,
    loc_name.loc_world_8x3_smb1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB1_NORMAL + 0x7c,
    loc_name.loc_world_8x4_smb1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB1_NORMAL + 0x7e,
}

# SMBLL Locations
# Level Clears are on Even Numbers (Zero Included), Reds are Odds
normal_loc_smbll_reg_world = {
    loc_name.loc_world_1_1_smbll: BASE_OFFSET_NORMAL + GAME_OFFSET_SMBLL_NORMAL + 0x00,
    loc_name.loc_world_1_2_smbll: BASE_OFFSET_NORMAL + GAME_OFFSET_SMBLL_NORMAL + 0x02,
    loc_name.loc_world_1_3_smbll: BASE_OFFSET_NORMAL + GAME_OFFSET_SMBLL_NORMAL + 0x04,
    loc_name.loc_world_1_4_smbll: BASE_OFFSET_NORMAL + GAME_OFFSET_SMBLL_NORMAL + 0x06,
    loc_name.loc_world_2_1_smbll: BASE_OFFSET_NORMAL + GAME_OFFSET_SMBLL_NORMAL + 0x08,
    loc_name.loc_world_2_2_smbll: BASE_OFFSET_NORMAL + GAME_OFFSET_SMBLL_NORMAL + 0x0a,
    loc_name.loc_world_2_3_smbll: BASE_OFFSET_NORMAL + GAME_OFFSET_SMBLL_NORMAL + 0x0c,
    loc_name.loc_world_2_4_smbll: BASE_OFFSET_NORMAL + GAME_OFFSET_SMBLL_NORMAL + 0x0e,
    loc_name.loc_world_3_1_smbll: BASE_OFFSET_NORMAL + GAME_OFFSET_SMBLL_NORMAL + 0x10,
    loc_name.loc_world_3_2_smbll: BASE_OFFSET_NORMAL + GAME_OFFSET_SMBLL_NORMAL + 0x12,
    loc_name.loc_world_3_3_smbll: BASE_OFFSET_NORMAL + GAME_OFFSET_SMBLL_NORMAL + 0x14,
    loc_name.loc_world_3_4_smbll: BASE_OFFSET_NORMAL + GAME_OFFSET_SMBLL_NORMAL + 0x16,
    loc_name.loc_world_4_1_smbll: BASE_OFFSET_NORMAL + GAME_OFFSET_SMBLL_NORMAL + 0x18,
    loc_name.loc_world_4_2_smbll: BASE_OFFSET_NORMAL + GAME_OFFSET_SMBLL_NORMAL + 0x1a,
    loc_name.loc_world_4_3_smbll: BASE_OFFSET_NORMAL + GAME_OFFSET_SMBLL_NORMAL + 0x1c,
    loc_name.loc_world_4_4_smbll: BASE_OFFSET_NORMAL + GAME_OFFSET_SMBLL_NORMAL + 0x1e,
    loc_name.loc_world_5_1_smbll: BASE_OFFSET_NORMAL + GAME_OFFSET_SMBLL_NORMAL + 0x20,
    loc_name.loc_world_5_2_smbll: BASE_OFFSET_NORMAL + GAME_OFFSET_SMBLL_NORMAL + 0x22,
    loc_name.loc_world_5_3_smbll: BASE_OFFSET_NORMAL + GAME_OFFSET_SMBLL_NORMAL + 0x24,
    loc_name.loc_world_5_4_smbll: BASE_OFFSET_NORMAL + GAME_OFFSET_SMBLL_NORMAL + 0x26,
    loc_name.loc_world_6_1_smbll: BASE_OFFSET_NORMAL + GAME_OFFSET_SMBLL_NORMAL + 0x28,
    loc_name.loc_world_6_2_smbll: BASE_OFFSET_NORMAL + GAME_OFFSET_SMBLL_NORMAL + 0x2a,
    loc_name.loc_world_6_3_smbll: BASE_OFFSET_NORMAL + GAME_OFFSET_SMBLL_NORMAL + 0x2c,
    loc_name.loc_world_6_4_smbll: BASE_OFFSET_NORMAL + GAME_OFFSET_SMBLL_NORMAL + 0x2e,
    loc_name.loc_world_7_1_smbll: BASE_OFFSET_NORMAL + GAME_OFFSET_SMBLL_NORMAL + 0x30,
    loc_name.loc_world_7_2_smbll: BASE_OFFSET_NORMAL + GAME_OFFSET_SMBLL_NORMAL + 0x32,
    loc_name.loc_world_7_3_smbll: BASE_OFFSET_NORMAL + GAME_OFFSET_SMBLL_NORMAL + 0x34,
    loc_name.loc_world_7_4_smbll: BASE_OFFSET_NORMAL + GAME_OFFSET_SMBLL_NORMAL + 0x36,
    loc_name.loc_world_8_1_smbll: BASE_OFFSET_NORMAL + GAME_OFFSET_SMBLL_NORMAL + 0x38,
    loc_name.loc_world_8_2_smbll: BASE_OFFSET_NORMAL + GAME_OFFSET_SMBLL_NORMAL + 0x3a,
    loc_name.loc_world_8_3_smbll: BASE_OFFSET_NORMAL + GAME_OFFSET_SMBLL_NORMAL + 0x3c,
    loc_name.loc_world_8_4_smbll: BASE_OFFSET_NORMAL + GAME_OFFSET_SMBLL_NORMAL + 0x3e,
}
normal_loc_smbll_fantasy_world = {
    loc_name.loc_world_fantasy_1_smbll: BASE_OFFSET_NORMAL + GAME_OFFSET_SMBLL_NORMAL + 0x40,
    loc_name.loc_world_fantasy_2_smbll: BASE_OFFSET_NORMAL + GAME_OFFSET_SMBLL_NORMAL + 0x42,
    loc_name.loc_world_fantasy_3_smbll: BASE_OFFSET_NORMAL + GAME_OFFSET_SMBLL_NORMAL + 0x44,
    loc_name.loc_world_fantasy_4_smbll: BASE_OFFSET_NORMAL + GAME_OFFSET_SMBLL_NORMAL + 0x46,
}
normal_loc_smbll_bonus_world = {
    loc_name.loc_world_a_1_smbll: BASE_OFFSET_NORMAL + GAME_OFFSET_SMBLL_NORMAL + 0x48,
    loc_name.loc_world_a_2_smbll: BASE_OFFSET_NORMAL + GAME_OFFSET_SMBLL_NORMAL + 0x4a,
    loc_name.loc_world_a_3_smbll: BASE_OFFSET_NORMAL + GAME_OFFSET_SMBLL_NORMAL + 0x4c,
    loc_name.loc_world_a_4_smbll: BASE_OFFSET_NORMAL + GAME_OFFSET_SMBLL_NORMAL + 0x4e,
    loc_name.loc_world_b_1_smbll: BASE_OFFSET_NORMAL + GAME_OFFSET_SMBLL_NORMAL + 0x50,
    loc_name.loc_world_b_2_smbll: BASE_OFFSET_NORMAL + GAME_OFFSET_SMBLL_NORMAL + 0x52,
    loc_name.loc_world_b_3_smbll: BASE_OFFSET_NORMAL + GAME_OFFSET_SMBLL_NORMAL + 0x54,
    loc_name.loc_world_b_4_smbll: BASE_OFFSET_NORMAL + GAME_OFFSET_SMBLL_NORMAL + 0x56,
    loc_name.loc_world_c_1_smbll: BASE_OFFSET_NORMAL + GAME_OFFSET_SMBLL_NORMAL + 0x58,
    loc_name.loc_world_c_2_smbll: BASE_OFFSET_NORMAL + GAME_OFFSET_SMBLL_NORMAL + 0x5a,
    loc_name.loc_world_c_3_smbll: BASE_OFFSET_NORMAL + GAME_OFFSET_SMBLL_NORMAL + 0x5c,
    loc_name.loc_world_c_4_smbll: BASE_OFFSET_NORMAL + GAME_OFFSET_SMBLL_NORMAL + 0x5e,
    loc_name.loc_world_d_1_smbll: BASE_OFFSET_NORMAL + GAME_OFFSET_SMBLL_NORMAL + 0x60,
    loc_name.loc_world_d_2_smbll: BASE_OFFSET_NORMAL + GAME_OFFSET_SMBLL_NORMAL + 0x62,
    loc_name.loc_world_d_3_smbll: BASE_OFFSET_NORMAL + GAME_OFFSET_SMBLL_NORMAL + 0x64,
    loc_name.loc_world_d_4_smbll: BASE_OFFSET_NORMAL + GAME_OFFSET_SMBLL_NORMAL + 0x66,
}

# SMB2 Locations
# Character Select Locations
normal_loc_smb2_selected_char = {
    loc_name.loc_char_pick_mario_smb2: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0xf8,
    loc_name.loc_char_pick_peach_smb2: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0xf9,
    loc_name.loc_char_pick_toad_smb2: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0xfa,
    loc_name.loc_char_pick_luigi_smb2: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0xfb,
}
normal_loc_smb2_highlighted_char = {
    loc_name.loc_char_view_mario_smb2: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0xfc,
    loc_name.loc_char_view_peach_smb2: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0xfd,
    loc_name.loc_char_view_toad_smb2: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0xfe,
    loc_name.loc_char_view_luigi_smb2: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0xff,
}
# Each Level gets its own byte, Bit Zero is Level Clear
# Bits 1, 2, and 3 are Mushrooms (Base Game 2-1 & 6-2 having only 1 w/ rest 2)
# Bit 4 is the Red Coins
# Bits 5-7 are reserved for potential SlotSanity Checks.
normal_loc_smb2_world = {
    loc_name.loc_world_1_1_smb2: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x00,
    loc_name.loc_world_1_1_smb2_mush_1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x01,
    loc_name.loc_world_1_1_smb2_mush_2: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x02,
    loc_name.loc_world_1_2_smb2: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x08,
    loc_name.loc_world_1_2_smb2_mush_1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x09,
    loc_name.loc_world_1_2_smb2_mush_2: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x0a,
    loc_name.loc_world_1_3_smb2: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x10,
    loc_name.loc_world_1_3_smb2_mush_1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x11,
    loc_name.loc_world_1_3_smb2_mush_2: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x12,
    loc_name.loc_world_2_1_smb2: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x18,
    loc_name.loc_world_2_1_smb2_mush_1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x19,
    loc_name.loc_world_2_2_smb2: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x20,
    loc_name.loc_world_2_2_smb2_mush_1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x21,
    loc_name.loc_world_2_2_smb2_mush_2: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x22,
    loc_name.loc_world_2_3_smb2: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x28,
    loc_name.loc_world_2_3_smb2_mush_1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x29,
    loc_name.loc_world_2_3_smb2_mush_2: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x2a,
    loc_name.loc_world_3_1_smb2: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x30,
    loc_name.loc_world_3_1_smb2_mush_1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x31,
    loc_name.loc_world_3_1_smb2_mush_2: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x32,
    loc_name.loc_world_3_2_smb2: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x38,
    loc_name.loc_world_3_2_smb2_mush_1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x39,
    loc_name.loc_world_3_2_smb2_mush_2: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x3a,
    loc_name.loc_world_3_3_smb2: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x40,
    loc_name.loc_world_3_3_smb2_mush_1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x41,
    loc_name.loc_world_3_3_smb2_mush_2: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x42,
    loc_name.loc_world_4_1_smb2: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x48,
    loc_name.loc_world_4_1_smb2_mush_1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x49,
    loc_name.loc_world_4_1_smb2_mush_2: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x4a,
    loc_name.loc_world_4_2_smb2: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x50,
    loc_name.loc_world_4_2_smb2_mush_1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x51,
    loc_name.loc_world_4_2_smb2_mush_2: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x52,
    loc_name.loc_world_4_3_smb2: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x58,
    loc_name.loc_world_4_3_smb2_mush_1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x59,
    loc_name.loc_world_4_3_smb2_mush_2: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x5a,
    loc_name.loc_world_5_1_smb2: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x60,
    loc_name.loc_world_5_1_smb2_mush_1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x61,
    loc_name.loc_world_5_1_smb2_mush_2: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x62,
    loc_name.loc_world_5_2_smb2: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x68,
    loc_name.loc_world_5_2_smb2_mush_1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x69,
    loc_name.loc_world_5_2_smb2_mush_2: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x6a,
    loc_name.loc_world_5_3_smb2: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x70,
    loc_name.loc_world_5_3_smb2_mush_1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x71,
    loc_name.loc_world_5_3_smb2_mush_2: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x72,
    loc_name.loc_world_6_1_smb2: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x78,
    loc_name.loc_world_6_1_smb2_mush_1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x79,
    loc_name.loc_world_6_1_smb2_mush_2: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x7a,
    loc_name.loc_world_6_2_smb2: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x80,
    loc_name.loc_world_6_2_smb2_mush_1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x81,
    loc_name.loc_world_6_3_smb2: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x88,
    loc_name.loc_world_6_3_smb2_mush_1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x89,
    loc_name.loc_world_6_3_smb2_mush_2: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x8a,
    loc_name.loc_world_7_1_smb2: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x90,
    loc_name.loc_world_7_1_smb2_mush_1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x91,
    loc_name.loc_world_7_1_smb2_mush_2: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x92,
    loc_name.loc_world_7_2_smb2: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x98,
    loc_name.loc_world_7_2_smb2_mush_1: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x99,
    loc_name.loc_world_7_2_smb2_mush_2: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x9a,
}
normal_loc_smb2_extra_mushrooms = {
    loc_name.loc_world_1_1_smb2_mush_3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x03,
    loc_name.loc_world_1_2_smb2_mush_3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x0b,
    loc_name.loc_world_1_3_smb2_mush_3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x13,
    loc_name.loc_world_2_1_smb2_mush_2: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x1a,
    loc_name.loc_world_2_1_smb2_mush_3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x1b,
    loc_name.loc_world_2_2_smb2_mush_3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x23,
    loc_name.loc_world_2_3_smb2_mush_3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x2b,
    loc_name.loc_world_3_1_smb2_mush_3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x33,
    loc_name.loc_world_3_2_smb2_mush_3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x3b,
    loc_name.loc_world_3_3_smb2_mush_3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x43,
    loc_name.loc_world_4_1_smb2_mush_3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x4b,
    loc_name.loc_world_4_2_smb2_mush_3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x53,
    loc_name.loc_world_4_3_smb2_mush_3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x5b,
    loc_name.loc_world_5_1_smb2_mush_3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x63,
    loc_name.loc_world_5_2_smb2_mush_3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x6b,
    loc_name.loc_world_5_3_smb2_mush_3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x73,
    loc_name.loc_world_6_1_smb2_mush_3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x7b,
    loc_name.loc_world_6_2_smb2_mush_2: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x82,
    loc_name.loc_world_6_2_smb2_mush_3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x83,
    loc_name.loc_world_6_3_smb2_mush_3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x8b,
    loc_name.loc_world_7_1_smb2_mush_3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x93,
    loc_name.loc_world_7_2_smb2_mush_3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB2_NORMAL + 0x9b,
}

# SMB3 Locations
# TODO: Other Catergories
# Level Clears Only
normal_loc_smb3_world = {
    # World 1
    loc_name.loc_world_1_1_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x00 * 8),
    loc_name.loc_world_1_2_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x01 * 8),
    loc_name.loc_world_1_3_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x02 * 8),
    loc_name.loc_world_1_4_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x03 * 8),
    loc_name.loc_world_1_fort_1_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x04 * 8),
    loc_name.loc_world_1_5_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x05 * 8),
    loc_name.loc_world_1_6_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x06 * 8),
    loc_name.loc_world_1_castle_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x07 * 8),
    # World 2
    loc_name.loc_world_2_1_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x08 * 8),
    loc_name.loc_world_2_2_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x09 * 8),
    loc_name.loc_world_2_fort_1_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x0a * 8),
    loc_name.loc_world_2_3_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x0b * 8),
    loc_name.loc_world_2_sand_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x0d * 8),
    loc_name.loc_world_2_4_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x0c * 8),
    loc_name.loc_world_2_5_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x0e * 8),
    loc_name.loc_world_2_pyramid_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x0f * 8),
    loc_name.loc_world_2_castle_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x10 * 8),
    # World 3
    loc_name.loc_world_3_1_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x11 * 8),
    loc_name.loc_world_3_2_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x12 * 8),
    loc_name.loc_world_3_3_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x13 * 8),
    loc_name.loc_world_3_fort_1_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x14 * 8),
    loc_name.loc_world_3_4_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x15 * 8),
    loc_name.loc_world_3_5_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x16 * 8),
    loc_name.loc_world_3_6_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x17 * 8),
    loc_name.loc_world_3_7_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x18 * 8),
    loc_name.loc_world_3_fort_2_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x19 * 8),
    loc_name.loc_world_3_8_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x1a * 8),
    loc_name.loc_world_3_9_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x1b * 8),
    loc_name.loc_world_3_castle_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x1c * 8),
    # World 4
    loc_name.loc_world_4_1_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x1d * 8),
    loc_name.loc_world_4_2_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x1e * 8),
    loc_name.loc_world_4_3_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x1f * 8),
    loc_name.loc_world_4_fort_1_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x20 * 8),
    loc_name.loc_world_4_4_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x21 * 8),
    loc_name.loc_world_4_5_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x22 * 8),
    loc_name.loc_world_4_6_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x23 * 8),
    loc_name.loc_world_4_fort_2_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x24 * 8),
    loc_name.loc_world_4_castle_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x25 * 8),
    # World 5
    loc_name.loc_world_5_1_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x26 * 8),
    loc_name.loc_world_5_2_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x27 * 8),
    loc_name.loc_world_5_fort_1_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x29 * 8),
    loc_name.loc_world_5_3_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x28 * 8),
    loc_name.loc_world_5_4_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x2a * 8),
    loc_name.loc_world_5_5_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x2b * 8),
    loc_name.loc_world_5_6_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x2c * 8),
    loc_name.loc_world_5_7_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x2d * 8),
    loc_name.loc_world_5_fort_2_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x2e * 8),
    loc_name.loc_world_5_8_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x2f * 8),
    loc_name.loc_world_5_9_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x30 * 8),
    loc_name.loc_world_5_castle_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x31 * 8),
    # World 6, also known as Hell-Data
    loc_name.loc_world_6_1_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x32 * 8),
    loc_name.loc_world_6_2_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x33 * 8),
    loc_name.loc_world_6_3_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x34 * 8),
    loc_name.loc_world_6_fort_1_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x35 * 8),
    loc_name.loc_world_6_4_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x36 * 8),
    loc_name.loc_world_6_5_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x37 * 8),
    loc_name.loc_world_6_6_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x38 * 8),
    loc_name.loc_world_6_7_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x39 * 8),
    loc_name.loc_world_6_fort_2_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x3a * 8),
    loc_name.loc_world_6_8_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x3b * 8),
    loc_name.loc_world_6_9_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x3c * 8),
    loc_name.loc_world_6_10_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x3d * 8),
    loc_name.loc_world_6_fort_3_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x3e * 8),
    loc_name.loc_world_6_castle_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x3f * 8),
    # World 7
    loc_name.loc_world_7_1_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x40 * 8),
    loc_name.loc_world_7_2_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x41 * 8),
    loc_name.loc_world_7_3_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x42 * 8),
    loc_name.loc_world_7_4_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x43 * 8),
    loc_name.loc_world_7_5_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x44 * 8),
    loc_name.loc_world_7_munch_1_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x4b * 8),
    loc_name.loc_world_7_fort_1_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x45 * 8),
    loc_name.loc_world_7_6_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x46 * 8),
    loc_name.loc_world_7_7_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x47 * 8),
    loc_name.loc_world_7_8_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x48 * 8),
    loc_name.loc_world_7_9_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x49 * 8),
    loc_name.loc_world_7_fort_2_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x4a * 8),
    loc_name.loc_world_7_munch_2_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x4c * 8),
    loc_name.loc_world_7_castle_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x4d * 8),
    # World 8
    loc_name.loc_world_8_tank_1_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x4e * 8),
    loc_name.loc_world_8_navy_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x4f * 8),
    loc_name.loc_world_8_airship_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x50 * 8),
    loc_name.loc_world_8_hand_1_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x55 * 8),
    loc_name.loc_world_8_hand_2_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x56 * 8),
    loc_name.loc_world_8_hand_3_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x57 * 8),
    loc_name.loc_world_8_1_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x51 * 8),
    loc_name.loc_world_8_2_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x52 * 8),
    loc_name.loc_world_8_fort_1_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x53 * 8),
    loc_name.loc_world_8_tank_2_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x54 * 8),
    loc_name.loc_world_8_castle_smb3: BASE_OFFSET_NORMAL + GAME_OFFSET_SMB3_NORMAL + (0x5e * 8),
}

# All Locations
all_locations = {
    **normal_loc_smb1_reg_world,
    **normal_loc_smb1_hard_world,
    **normal_loc_smbll_reg_world,
    **normal_loc_smbll_fantasy_world,
    **normal_loc_smbll_bonus_world,
    **normal_loc_smb2_selected_char,
    **normal_loc_smb2_highlighted_char,
    **normal_loc_smb2_world,
    **normal_loc_smb2_extra_mushrooms,
    **normal_loc_smb3_world,
}

# Lookup ID to Name, not sure if needed? Just grabbed from other Worlds
lookup_id_to_name: typing.Dict[int, str] = {id: name for name, _ in all_locations.items()}

# Current Locations Available
location_table = {}

# TODO: Location Groups

# Let's make one more helper method before we begin actually creating locations.
# Later on in the code, we'll want specific subsections of LOCATION_NAME_TO_ID.
# To reduce the chance of copy-paste errors writing something like {"Chest": LOCATION_NAME_TO_ID["Chest"]},
# let's make a helper method that takes a list of location names and returns them as a dict with their IDs.
# Note: There is a minor typing quirk here. Some functions want location addresses to be an "int | None",
# so while our function here only ever returns dict[str, int], we annotate it as dict[str, int | None].
def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {loc_getter: all_locations[loc_getter] for loc_getter in location_names}


def create_all_locations(world: SMASWWorld) -> None:
    create_regular_locations(world)
    create_events(world)


def create_regular_locations(world: SMASWWorld) -> None:
    ## Finally, we need to put the Locations ("checks") into their regions.
    ## Once again, before we do anything, we can grab our regions we created by using world.get_region()
    #overworld = world.get_region("Overworld")
    #top_left_room = world.get_region("Top Left Room")
    #bottom_right_room = world.get_region("Bottom Right Room")
    #right_room = world.get_region("Right Room")
    #
    ## One way to create locations is by just creating them directly via their constructor.
    #bottom_left_chest = SMASWLocation(
    #    world.player, "Bottom Left Chest", world.location_name_to_id["Bottom Left Chest"], overworld
    #)
    #
    ## You can then add them to the region.
    #overworld.locations.append(bottom_left_chest)
    #
    ## A simpler way to do this is by using the region.add_locations helper.
    ## For this, you need to have a dict of location names to their IDs (i.e. a subset of location_name_to_id)
    ## Aha! So that's why we made that "get_location_names_with_ids" helper method earlier.
    ## You also need to pass your overridden Location class.
    #bottom_right_room_locations = get_location_names_with_ids(
    #    ["Bottom Right Room Left Chest", "Bottom Right Room Right Chest"]
    #)
    #bottom_right_room.add_locations(bottom_right_room_locations, SMASWLocation)
    #
    #top_left_room_locations = get_location_names_with_ids(["Top Left Room Chest"])
    #top_left_room.add_locations(top_left_room_locations, SMASWLocation)
    #
    #right_room_locations = get_location_names_with_ids(["Right Room Enemy Drop"])
    #right_room.add_locations(right_room_locations, SMASWLocation)
    #
    ## Locations may be in different regions depending on the player's options.
    ## In our case, the hammer option puts the Top Middle Chest into its own room called Top Middle Room.
    #top_middle_room_locations = get_location_names_with_ids(["Top Middle Chest"])
    #if world.options.hammer:
    #    top_middle_room = world.get_region("Top Middle Room")
    #    top_middle_room.add_locations(top_middle_room_locations, SMASWLocation)
    #else:
    #    overworld.add_locations(top_middle_room_locations, SMASWLocation)
    #
    ## Locations may exist only if the player enables certain options.
    ## In our case, the extra_starting_chest option adds the Bottom Left Extra Chest location.
    #if world.options.extra_starting_chest:
    #    # Once again, it is important to stress that even though the Bottom Left Extra Chest location doesn't always
    #    # exist, it must still always be present in the world's location_name_to_id.
    #    # Whether the location actually exists in the seed is purely determined by whether we create and add it here.
    #    bottom_left_extra_chest = get_location_names_with_ids(["Bottom Left Extra Chest"])
    #    overworld.add_locations(bottom_left_extra_chest, SMASWLocation)
    
    # Fetch all Regions (copy+paste from regions.py), even if we don't need them all
    menu = world.get_region("Game Select")
    smasw_req_goals = world.get_region("Completed Required SubGoals")
    smasw_goals = world.get_region("Completed All SubGoals")

    # SMB1
    if world.options.available_smb1.value != 0:
        reg_game_smb1 = world.get_region("SMB1 Game")
        reg_goal_smb1 = world.get_region("SMB1 Goal")
        # World 1
        reg_world_1_smb1 = world.get_region("World 1 (SMB1)")
        reg_world_1_1_tile_smb1 = world.get_region("World 1-1 Tile (SMB1)")
        reg_level_1_1_smb1 = world.get_region("Level 1-1 (SMB1)")
        reg_world_1_2_tile_smb1 = world.get_region("World 1-2 Tile (SMB1)")
        reg_level_1_2_smb1 = world.get_region("Level 1-2 (SMB1)")
        reg_world_1_3_tile_smb1 = world.get_region("World 1-3 Tile (SMB1)")
        reg_level_1_3_smb1 = world.get_region("Level 1-3 (SMB1)")
        reg_world_1_4_tile_smb1 = world.get_region("World 1-4 Tile (SMB1)")
        reg_level_1_4_smb1 = world.get_region("Level 1-4 (SMB1)")
        # World 2
        reg_world_2_smb1 = world.get_region("World 2 (SMB1)")
        reg_world_2_1_tile_smb1 = world.get_region("World 2-1 Tile (SMB1)")
        reg_level_2_1_smb1 = world.get_region("Level 2-1 (SMB1)")
        reg_world_2_2_tile_smb1 = world.get_region("World 2-2 Tile (SMB1)")
        reg_level_2_2_smb1 = world.get_region("Level 2-2 (SMB1)")
        reg_world_2_3_tile_smb1 = world.get_region("World 2-3 Tile (SMB1)")
        reg_level_2_3_smb1 = world.get_region("Level 2-3 (SMB1)")
        reg_world_2_4_tile_smb1 = world.get_region("World 2-4 Tile (SMB1)")
        reg_level_2_4_smb1 = world.get_region("Level 2-4 (SMB1)")
        # World 3
        reg_world_3_smb1 = world.get_region("World 3 (SMB1)")
        reg_world_3_1_tile_smb1 = world.get_region("World 3-1 Tile (SMB1)")
        reg_level_3_1_smb1 = world.get_region("Level 3-1 (SMB1)")
        reg_world_3_2_tile_smb1 = world.get_region("World 3-2 Tile (SMB1)")
        reg_level_3_2_smb1 = world.get_region("Level 3-2 (SMB1)")
        reg_world_3_3_tile_smb1 = world.get_region("World 3-3 Tile (SMB1)")
        reg_level_3_3_smb1 = world.get_region("Level 3-3 (SMB1)")
        reg_world_3_4_tile_smb1 = world.get_region("World 3-4 Tile (SMB1)")
        reg_level_3_4_smb1 = world.get_region("Level 3-4 (SMB1)")
        # World 4
        reg_world_4_smb1 = world.get_region("World 4 (SMB1)")
        reg_world_4_1_tile_smb1 = world.get_region("World 4-1 Tile (SMB1)")
        reg_level_4_1_smb1 = world.get_region("Level 4-1 (SMB1)")
        reg_world_4_2_tile_smb1 = world.get_region("World 4-2 Tile (SMB1)")
        reg_level_4_2_smb1 = world.get_region("Level 4-2 (SMB1)")
        reg_world_4_3_tile_smb1 = world.get_region("World 4-3 Tile (SMB1)")
        reg_level_4_3_smb1 = world.get_region("Level 4-3 (SMB1)")
        reg_world_4_4_tile_smb1 = world.get_region("World 4-4 Tile (SMB1)")
        reg_level_4_4_smb1 = world.get_region("Level 4-4 (SMB1)")
        # World 5
        reg_world_5_smb1 = world.get_region("World 5 (SMB1)")
        reg_world_5_1_tile_smb1 = world.get_region("World 5-1 Tile (SMB1)")
        reg_level_5_1_smb1 = world.get_region("Level 5-1 (SMB1)")
        reg_world_5_2_tile_smb1 = world.get_region("World 5-2 Tile (SMB1)")
        reg_level_5_2_smb1 = world.get_region("Level 5-2 (SMB1)")
        reg_world_5_3_tile_smb1 = world.get_region("World 5-3 Tile (SMB1)")
        reg_level_5_3_smb1 = world.get_region("Level 5-3 (SMB1)")
        reg_world_5_4_tile_smb1 = world.get_region("World 5-4 Tile (SMB1)")
        reg_level_5_4_smb1 = world.get_region("Level 5-4 (SMB1)")
        # World 6
        reg_world_6_smb1 = world.get_region("World 6 (SMB1)")
        reg_world_6_1_tile_smb1 = world.get_region("World 6-1 Tile (SMB1)")
        reg_level_6_1_smb1 = world.get_region("Level 6-1 (SMB1)")
        reg_world_6_2_tile_smb1 = world.get_region("World 6-2 Tile (SMB1)")
        reg_level_6_2_smb1 = world.get_region("Level 6-2 (SMB1)")
        reg_world_6_3_tile_smb1 = world.get_region("World 6-3 Tile (SMB1)")
        reg_level_6_3_smb1 = world.get_region("Level 6-3 (SMB1)")
        reg_world_6_4_tile_smb1 = world.get_region("World 6-4 Tile (SMB1)")
        reg_level_6_4_smb1 = world.get_region("Level 6-4 (SMB1)")
        # World 7
        reg_world_7_smb1 = world.get_region("World 7 (SMB1)")
        reg_world_7_1_tile_smb1 = world.get_region("World 7-1 Tile (SMB1)")
        reg_level_7_1_smb1 = world.get_region("Level 7-1 (SMB1)")
        reg_world_7_2_tile_smb1 = world.get_region("World 7-2 Tile (SMB1)")
        reg_level_7_2_smb1 = world.get_region("Level 7-2 (SMB1)")
        reg_world_7_3_tile_smb1 = world.get_region("World 7-3 Tile (SMB1)")
        reg_level_7_3_smb1 = world.get_region("Level 7-3 (SMB1)")
        reg_world_7_4_tile_smb1 = world.get_region("World 7-4 Tile (SMB1)")
        reg_level_7_4_smb1 = world.get_region("Level 7-4 (SMB1)")
        # World 8
        reg_world_8_smb1 = world.get_region("World 8 (SMB1)")
        reg_world_8_1_tile_smb1 = world.get_region("World 8-1 Tile (SMB1)")
        reg_level_8_1_smb1 = world.get_region("Level 8-1 (SMB1)")
        reg_world_8_2_tile_smb1 = world.get_region("World 8-2 Tile (SMB1)")
        reg_level_8_2_smb1 = world.get_region("Level 8-2 (SMB1)")
        reg_world_8_3_tile_smb1 = world.get_region("World 8-3 Tile (SMB1)")
        reg_level_8_3_smb1 = world.get_region("Level 8-3 (SMB1)")
        reg_world_8_4_tile_smb1 = world.get_region("World 8-4 Tile (SMB1)")
        reg_level_8_4_smb1 = world.get_region("Level 8-4 (SMB1)")
        # Hardmode Worlds
        if world.options.hard_worlds_smb1.value != 0:
            # World X1
            reg_world_x1_smb1 = world.get_region("World X1 (SMB1)")
            reg_world_1x1_tile_smb1 = world.get_region("World 1x1 Tile (SMB1)")
            reg_level_1x1_smb1 = world.get_region("Level 1x1 (SMB1)")
            reg_world_1x2_tile_smb1 = world.get_region("World 1x2 Tile (SMB1)")
            reg_level_1x2_smb1 = world.get_region("Level 1x2 (SMB1)")
            reg_world_1x3_tile_smb1 = world.get_region("World 1x3 Tile (SMB1)")
            reg_level_1x3_smb1 = world.get_region("Level 1x3 (SMB1)")
            reg_world_1x4_tile_smb1 = world.get_region("World 1x4 Tile (SMB1)")
            reg_level_1x4_smb1 = world.get_region("Level 1x4 (SMB1)")
            # World X2
            reg_world_x2_smb1 = world.get_region("World X2 (SMB1)")
            reg_world_2x1_tile_smb1 = world.get_region("World 2x1 Tile (SMB1)")
            reg_level_2x1_smb1 = world.get_region("Level 2x1 (SMB1)")
            reg_world_2x2_tile_smb1 = world.get_region("World 2x2 Tile (SMB1)")
            reg_level_2x2_smb1 = world.get_region("Level 2x2 (SMB1)")
            reg_world_2x3_tile_smb1 = world.get_region("World 2x3 Tile (SMB1)")
            reg_level_2x3_smb1 = world.get_region("Level 2x3 (SMB1)")
            reg_world_2x4_tile_smb1 = world.get_region("World 2x4 Tile (SMB1)")
            reg_level_2x4_smb1 = world.get_region("Level 2x4 (SMB1)")
            # World X3
            reg_world_x3_smb1 = world.get_region("World X3 (SMB1)")
            reg_world_3x1_tile_smb1 = world.get_region("World 3x1 Tile (SMB1)")
            reg_level_3x1_smb1 = world.get_region("Level 3x1 (SMB1)")
            reg_world_3x2_tile_smb1 = world.get_region("World 3x2 Tile (SMB1)")
            reg_level_3x2_smb1 = world.get_region("Level 3x2 (SMB1)")
            reg_world_3x3_tile_smb1 = world.get_region("World 3x3 Tile (SMB1)")
            reg_level_3x3_smb1 = world.get_region("Level 3x3 (SMB1)")
            reg_world_3x4_tile_smb1 = world.get_region("World 3x4 Tile (SMB1)")
            reg_level_3x4_smb1 = world.get_region("Level 3x4 (SMB1)")
            # World X4
            reg_world_x4_smb1 = world.get_region("World X4 (SMB1)")
            reg_world_4x1_tile_smb1 = world.get_region("World 4x1 Tile (SMB1)")
            reg_level_4x1_smb1 = world.get_region("Level 4x1 (SMB1)")
            reg_world_4x2_tile_smb1 = world.get_region("World 4x2 Tile (SMB1)")
            reg_level_4x2_smb1 = world.get_region("Level 4x2 (SMB1)")
            reg_world_4x3_tile_smb1 = world.get_region("World 4x3 Tile (SMB1)")
            reg_level_4x3_smb1 = world.get_region("Level 4x3 (SMB1)")
            reg_world_4x4_tile_smb1 = world.get_region("World 4x4 Tile (SMB1)")
            reg_level_4x4_smb1 = world.get_region("Level 4x4 (SMB1)")
            # World X5
            reg_world_x5_smb1 = world.get_region("World X5 (SMB1)")
            reg_world_5x1_tile_smb1 = world.get_region("World 5x1 Tile (SMB1)")
            reg_level_5x1_smb1 = world.get_region("Level 5x1 (SMB1)")
            reg_world_5x2_tile_smb1 = world.get_region("World 5x2 Tile (SMB1)")
            reg_level_5x2_smb1 = world.get_region("Level 5x2 (SMB1)")
            reg_world_5x3_tile_smb1 = world.get_region("World 5x3 Tile (SMB1)")
            reg_level_5x3_smb1 = world.get_region("Level 5x3 (SMB1)")
            reg_world_5x4_tile_smb1 = world.get_region("World 5x4 Tile (SMB1)")
            reg_level_5x4_smb1 = world.get_region("Level 5x4 (SMB1)")
            # World X6
            reg_world_x6_smb1 = world.get_region("World X6 (SMB1)")
            reg_world_6x1_tile_smb1 = world.get_region("World 6x1 Tile (SMB1)")
            reg_level_6x1_smb1 = world.get_region("Level 6x1 (SMB1)")
            reg_world_6x2_tile_smb1 = world.get_region("World 6x2 Tile (SMB1)")
            reg_level_6x2_smb1 = world.get_region("Level 6x2 (SMB1)")
            reg_world_6x3_tile_smb1 = world.get_region("World 6x3 Tile (SMB1)")
            reg_level_6x3_smb1 = world.get_region("Level 6x3 (SMB1)")
            reg_world_6x4_tile_smb1 = world.get_region("World 6x4 Tile (SMB1)")
            reg_level_6x4_smb1 = world.get_region("Level 6x4 (SMB1)")
            # World X7
            reg_world_x7_smb1 = world.get_region("World X7 (SMB1)")
            reg_world_7x1_tile_smb1 = world.get_region("World 7x1 Tile (SMB1)")
            reg_level_7x1_smb1 = world.get_region("Level 7x1 (SMB1)")
            reg_world_7x2_tile_smb1 = world.get_region("World 7x2 Tile (SMB1)")
            reg_level_7x2_smb1 = world.get_region("Level 7x2 (SMB1)")
            reg_world_7x3_tile_smb1 = world.get_region("World 7x3 Tile (SMB1)")
            reg_level_7x3_smb1 = world.get_region("Level 7x3 (SMB1)")
            reg_world_7x4_tile_smb1 = world.get_region("World 7x4 Tile (SMB1)")
            reg_level_7x4_smb1 = world.get_region("Level 7x4 (SMB1)")
            # World X8
            reg_world_x8_smb1 = world.get_region("World X8 (SMB1)")
            reg_world_8x1_tile_smb1 = world.get_region("World 8x1 Tile (SMB1)")
            reg_level_8x1_smb1 = world.get_region("Level 8x1 (SMB1)")
            reg_world_8x2_tile_smb1 = world.get_region("World 8x2 Tile (SMB1)")
            reg_level_8x2_smb1 = world.get_region("Level 8x2 (SMB1)")
            reg_world_8x3_tile_smb1 = world.get_region("World 8x3 Tile (SMB1)")
            reg_level_8x3_smb1 = world.get_region("Level 8x3 (SMB1)")
            reg_world_8x4_tile_smb1 = world.get_region("World 8x4 Tile (SMB1)")
            reg_level_8x4_smb1 = world.get_region("Level 8x4 (SMB1)")

    # SMBLL
    if world.options.available_smbll.value != 0:
        reg_game_smbll = world.get_region("SMBLL Game")
        reg_goal_smbll = world.get_region("SMBLL Goal")
        # World 1
        reg_world_1_smbll = world.get_region("World 1 (SMBLL)")
        reg_world_1_1_tile_smbll = world.get_region("World 1-1 Tile (SMBLL)")
        reg_level_1_1_smbll = world.get_region("Level 1-1 (SMBLL)")
        reg_world_1_2_tile_smbll = world.get_region("World 1-2 Tile (SMBLL)")
        reg_level_1_2_smbll = world.get_region("Level 1-2 (SMBLL)")
        reg_world_1_3_tile_smbll = world.get_region("World 1-3 Tile (SMBLL)")
        reg_level_1_3_smbll = world.get_region("Level 1-3 (SMBLL)")
        reg_world_1_4_tile_smbll = world.get_region("World 1-4 Tile (SMBLL)")
        reg_level_1_4_smbll = world.get_region("Level 1-4 (SMBLL)")
        # World 2
        reg_world_2_smbll = world.get_region("World 2 (SMBLL)")
        reg_world_2_1_tile_smbll = world.get_region("World 2-1 Tile (SMBLL)")
        reg_level_2_1_smbll = world.get_region("Level 2-1 (SMBLL)")
        reg_world_2_2_tile_smbll = world.get_region("World 2-2 Tile (SMBLL)")
        reg_level_2_2_smbll = world.get_region("Level 2-2 (SMBLL)")
        reg_world_2_3_tile_smbll = world.get_region("World 2-3 Tile (SMBLL)")
        reg_level_2_3_smbll = world.get_region("Level 2-3 (SMBLL)")
        reg_world_2_4_tile_smbll = world.get_region("World 2-4 Tile (SMBLL)")
        reg_level_2_4_smbll = world.get_region("Level 2-4 (SMBLL)")
        # World 3
        reg_world_3_smbll = world.get_region("World 3 (SMBLL)")
        reg_world_3_1_tile_smbll = world.get_region("World 3-1 Tile (SMBLL)")
        reg_level_3_1_smbll = world.get_region("Level 3-1 (SMBLL)")
        reg_world_3_2_tile_smbll = world.get_region("World 3-2 Tile (SMBLL)")
        reg_level_3_2_smbll = world.get_region("Level 3-2 (SMBLL)")
        reg_world_3_3_tile_smbll = world.get_region("World 3-3 Tile (SMBLL)")
        reg_level_3_3_smbll = world.get_region("Level 3-3 (SMBLL)")
        reg_world_3_4_tile_smbll = world.get_region("World 3-4 Tile (SMBLL)")
        reg_level_3_4_smbll = world.get_region("Level 3-4 (SMBLL)")
        # World 4
        reg_world_4_smbll = world.get_region("World 4 (SMBLL)")
        reg_world_4_1_tile_smbll = world.get_region("World 4-1 Tile (SMBLL)")
        reg_level_4_1_smbll = world.get_region("Level 4-1 (SMBLL)")
        reg_world_4_2_tile_smbll = world.get_region("World 4-2 Tile (SMBLL)")
        reg_level_4_2_smbll = world.get_region("Level 4-2 (SMBLL)")
        reg_world_4_3_tile_smbll = world.get_region("World 4-3 Tile (SMBLL)")
        reg_level_4_3_smbll = world.get_region("Level 4-3 (SMBLL)")
        reg_world_4_4_tile_smbll = world.get_region("World 4-4 Tile (SMBLL)")
        reg_level_4_4_smbll = world.get_region("Level 4-4 (SMBLL)")
        # World 5
        reg_world_5_smbll = world.get_region("World 5 (SMBLL)")
        reg_world_5_1_tile_smbll = world.get_region("World 5-1 Tile (SMBLL)")
        reg_level_5_1_smbll = world.get_region("Level 5-1 (SMBLL)")
        reg_world_5_2_tile_smbll = world.get_region("World 5-2 Tile (SMBLL)")
        reg_level_5_2_smbll = world.get_region("Level 5-2 (SMBLL)")
        reg_world_5_3_tile_smbll = world.get_region("World 5-3 Tile (SMBLL)")
        reg_level_5_3_smbll = world.get_region("Level 5-3 (SMBLL)")
        reg_world_5_4_tile_smbll = world.get_region("World 5-4 Tile (SMBLL)")
        reg_level_5_4_smbll = world.get_region("Level 5-4 (SMBLL)")
        # World 6
        reg_world_6_smbll = world.get_region("World 6 (SMBLL)")
        reg_world_6_1_tile_smbll = world.get_region("World 6-1 Tile (SMBLL)")
        reg_level_6_1_smbll = world.get_region("Level 6-1 (SMBLL)")
        reg_world_6_2_tile_smbll = world.get_region("World 6-2 Tile (SMBLL)")
        reg_level_6_2_smbll = world.get_region("Level 6-2 (SMBLL)")
        reg_world_6_3_tile_smbll = world.get_region("World 6-3 Tile (SMBLL)")
        reg_level_6_3_smbll = world.get_region("Level 6-3 (SMBLL)")
        reg_world_6_4_tile_smbll = world.get_region("World 6-4 Tile (SMBLL)")
        reg_level_6_4_smbll = world.get_region("Level 6-4 (SMBLL)")
        # World 7
        reg_world_7_smbll = world.get_region("World 7 (SMBLL)")
        reg_world_7_1_tile_smbll = world.get_region("World 7-1 Tile (SMBLL)")
        reg_level_7_1_smbll = world.get_region("Level 7-1 (SMBLL)")
        reg_world_7_2_tile_smbll = world.get_region("World 7-2 Tile (SMBLL)")
        reg_level_7_2_smbll = world.get_region("Level 7-2 (SMBLL)")
        reg_world_7_3_tile_smbll = world.get_region("World 7-3 Tile (SMBLL)")
        reg_level_7_3_smbll = world.get_region("Level 7-3 (SMBLL)")
        reg_world_7_4_tile_smbll = world.get_region("World 7-4 Tile (SMBLL)")
        reg_level_7_4_smbll = world.get_region("Level 7-4 (SMBLL)")
        # World 8
        reg_world_8_smbll = world.get_region("World 8 (SMBLL)")
        reg_world_8_1_tile_smbll = world.get_region("World 8-1 Tile (SMBLL)")
        reg_level_8_1_smbll = world.get_region("Level 8-1 (SMBLL)")
        reg_world_8_2_tile_smbll = world.get_region("World 8-2 Tile (SMBLL)")
        reg_level_8_2_smbll = world.get_region("Level 8-2 (SMBLL)")
        reg_world_8_3_tile_smbll = world.get_region("World 8-3 Tile (SMBLL)")
        reg_level_8_3_smbll = world.get_region("Level 8-3 (SMBLL)")
        reg_world_8_4_tile_smbll = world.get_region("World 8-4 Tile (SMBLL)")
        reg_level_8_4_smbll = world.get_region("Level 8-4 (SMBLL)")
        # Fantasy World
        if world.options.fantasy_world_smbll.value != 0:
            # World 9
            reg_world_9_smbll = world.get_region("World 9 (SMBLL)")
            reg_world_9_1_tile_smbll = world.get_region("World 9-1 Tile (SMBLL)")
            reg_level_9_1_smbll = world.get_region("Level 9-1 (SMBLL)")
            reg_world_9_2_tile_smbll = world.get_region("World 9-2 Tile (SMBLL)")
            reg_level_9_2_smbll = world.get_region("Level 9-2 (SMBLL)")
            reg_world_9_3_tile_smbll = world.get_region("World 9-3 Tile (SMBLL)")
            reg_level_9_3_smbll = world.get_region("Level 9-3 (SMBLL)")
            reg_world_9_4_tile_smbll = world.get_region("World 9-4 Tile (SMBLL)")
            reg_level_9_4_smbll = world.get_region("Level 9-4 (SMBLL)")
        # Bonus Worlds
        if world.options.bonus_worlds_smbll.value != 0:
            # World A
            reg_world_a_smbll = world.get_region("World A (SMBLL)")
            reg_world_a_1_tile_smbll = world.get_region("World A-1 Tile (SMBLL)")
            reg_level_a_1_smbll = world.get_region("Level A-1 (SMBLL)")
            reg_world_a_2_tile_smbll = world.get_region("World A-2 Tile (SMBLL)")
            reg_level_a_2_smbll = world.get_region("Level A-2 (SMBLL)")
            reg_world_a_3_tile_smbll = world.get_region("World A-3 Tile (SMBLL)")
            reg_level_a_3_smbll = world.get_region("Level A-3 (SMBLL)")
            reg_world_a_4_tile_smbll = world.get_region("World A-4 Tile (SMBLL)")
            reg_level_a_4_smbll = world.get_region("Level A-4 (SMBLL)")
            # World B
            reg_world_b_smbll = world.get_region("World B (SMBLL)")
            reg_world_b_1_tile_smbll = world.get_region("World B-1 Tile (SMBLL)")
            reg_level_b_1_smbll = world.get_region("Level B-1 (SMBLL)")
            reg_world_b_2_tile_smbll = world.get_region("World B-2 Tile (SMBLL)")
            reg_level_b_2_smbll = world.get_region("Level B-2 (SMBLL)")
            reg_world_b_3_tile_smbll = world.get_region("World B-3 Tile (SMBLL)")
            reg_level_b_3_smbll = world.get_region("Level B-3 (SMBLL)")
            reg_world_b_4_tile_smbll = world.get_region("World B-4 Tile (SMBLL)")
            reg_level_b_4_smbll = world.get_region("Level B-4 (SMBLL)")
            # World C
            reg_world_c_smbll = world.get_region("World C (SMBLL)")
            reg_world_c_1_tile_smbll = world.get_region("World C-1 Tile (SMBLL)")
            reg_level_c_1_smbll = world.get_region("Level C-1 (SMBLL)")
            reg_world_c_2_tile_smbll = world.get_region("World C-2 Tile (SMBLL)")
            reg_level_c_2_smbll = world.get_region("Level C-2 (SMBLL)")
            reg_world_c_3_tile_smbll = world.get_region("World C-3 Tile (SMBLL)")
            reg_level_c_3_smbll = world.get_region("Level C-3 (SMBLL)")
            reg_world_c_4_tile_smbll = world.get_region("World C-4 Tile (SMBLL)")
            reg_level_c_4_smbll = world.get_region("Level C-4 (SMBLL)")
            # World D
            reg_world_d_smbll = world.get_region("World D (SMBLL)")
            reg_world_d_1_tile_smbll = world.get_region("World D-1 Tile (SMBLL)")
            reg_level_d_1_smbll = world.get_region("Level D-1 (SMBLL)")
            reg_world_d_2_tile_smbll = world.get_region("World D-2 Tile (SMBLL)")
            reg_level_d_2_smbll = world.get_region("Level D-2 (SMBLL)")
            reg_world_d_3_tile_smbll = world.get_region("World D-3 Tile (SMBLL)")
            reg_level_d_3_smbll = world.get_region("Level D-3 (SMBLL)")
            reg_world_d_4_tile_smbll = world.get_region("World D-4 Tile (SMBLL)")
            reg_level_d_4_smbll = world.get_region("Level D-4 (SMBLL)")

    # SMB2
    if world.options.available_smb2.value != 0:
        reg_game_smb2 = world.get_region("SMB2 Game")
        char_sel_smb2 = world.get_region("Character Select (SMB2)")
        # World 1
        reg_world_1_smb2 = world.get_region("World 1 (SMB2)")
        reg_world_1_1_tile_smb2 = world.get_region("World 1-1 Tile (SMB2)")
        reg_level_1_1_smb2 = world.get_region("Level 1-1 (SMB2)")
        reg_world_1_2_tile_smb2 = world.get_region("World 1-2 Tile (SMB2)")
        reg_level_1_2_smb2 = world.get_region("Level 1-2 (SMB2)")
        reg_world_1_3_tile_smb2 = world.get_region("World 1-3 Tile (SMB2)")
        reg_level_1_3_smb2 = world.get_region("Level 1-3 (SMB2)")
        # World 2
        reg_world_2_smb2 = world.get_region("World 2 (SMB2)")
        reg_world_2_1_tile_smb2 = world.get_region("World 2-1 Tile (SMB2)")
        reg_level_2_1_smb2 = world.get_region("Level 2-1 (SMB2)")
        reg_world_2_2_tile_smb2 = world.get_region("World 2-2 Tile (SMB2)")
        reg_level_2_2_smb2 = world.get_region("Level 2-2 (SMB2)")
        reg_world_2_3_tile_smb2 = world.get_region("World 2-3 Tile (SMB2)")
        reg_level_2_3_smb2 = world.get_region("Level 2-3 (SMB2)")
        # World 3
        reg_world_3_smb2 = world.get_region("World 3 (SMB2)")
        reg_world_3_1_tile_smb2 = world.get_region("World 3-1 Tile (SMB2)")
        reg_level_3_1_smb2 = world.get_region("Level 3-1 (SMB2)")
        reg_world_3_2_tile_smb2 = world.get_region("World 3-2 Tile (SMB2)")
        reg_level_3_2_smb2 = world.get_region("Level 3-2 (SMB2)")
        reg_world_3_3_tile_smb2 = world.get_region("World 3-3 Tile (SMB2)")
        reg_level_3_3_smb2 = world.get_region("Level 3-3 (SMB2)")
        # World 4
        reg_world_4_smb2 = world.get_region("World 4 (SMB2)")
        reg_world_4_1_tile_smb2 = world.get_region("World 4-1 Tile (SMB2)")
        reg_level_4_1_smb2 = world.get_region("Level 4-1 (SMB2)")
        reg_world_4_2_tile_smb2 = world.get_region("World 4-2 Tile (SMB2)")
        reg_level_4_2_smb2 = world.get_region("Level 4-2 (SMB2)")
        reg_world_4_3_tile_smb2 = world.get_region("World 4-3 Tile (SMB2)")
        reg_level_4_3_smb2 = world.get_region("Level 4-3 (SMB2)")
        # World 5
        reg_world_5_smb2 = world.get_region("World 5 (SMB2)")
        reg_world_5_1_tile_smb2 = world.get_region("World 5-1 Tile (SMB2)")
        reg_level_5_1_smb2 = world.get_region("Level 5-1 (SMB2)")
        reg_world_5_2_tile_smb2 = world.get_region("World 5-2 Tile (SMB2)")
        reg_level_5_2_smb2 = world.get_region("Level 5-2 (SMB2)")
        reg_world_5_3_tile_smb2 = world.get_region("World 5-3 Tile (SMB2)")
        reg_level_5_3_smb2 = world.get_region("Level 5-3 (SMB2)")
        # World 6
        reg_world_6_smb2 = world.get_region("World 6 (SMB2)")
        reg_world_6_1_tile_smb2 = world.get_region("World 6-1 Tile (SMB2)")
        reg_level_6_1_smb2 = world.get_region("Level 6-1 (SMB2)")
        reg_world_6_2_tile_smb2 = world.get_region("World 6-2 Tile (SMB2)")
        reg_level_6_2_smb2 = world.get_region("Level 6-2 (SMB2)")
        reg_world_6_3_tile_smb2 = world.get_region("World 6-3 Tile (SMB2)")
        reg_level_6_3_smb2 = world.get_region("Level 6-3 (SMB2)")
        # World 7
        reg_world_7_smb2 = world.get_region("World 7 (SMB2)")
        reg_world_7_1_tile_smb2 = world.get_region("World 7-1 Tile (SMB2)")
        reg_level_7_1_smb2 = world.get_region("Level 7-1 (SMB2)")
        reg_world_7_2_tile_smb2 = world.get_region("World 7-2 Tile (SMB2)")
        reg_level_7_2_smb2 = world.get_region("Level 7-2 (SMB2)")

    # SMB3
    if world.options.available_smb3.value != 0:
        reg_game_smb3 = world.get_region("SMB3 Game")
        # TODO: Mushroom Houses, Spade Games, Bro Fights, Etc.
        # World 1
        reg_world_1_smb3 = world.get_region("World 1 (SMB3)")
        reg_world_1_1_tile_smb3 = world.get_region("World 1-1 Tile (SMB3)")
        reg_level_1_1_smb3 = world.get_region("Level 1-1 (SMB3)")
        reg_world_1_2_tile_smb3 = world.get_region("World 1-2 Tile (SMB3)")
        reg_level_1_2_smb3 = world.get_region("Level 1-2 (SMB3)")
        reg_world_1_3_tile_smb3 = world.get_region("World 1-3 Tile (SMB3)")
        reg_level_1_3_smb3 = world.get_region("Level 1-3 (SMB3)")
        reg_world_1_4_tile_smb3 = world.get_region("World 1-4 Tile (SMB3)")
        reg_level_1_4_smb3 = world.get_region("Level 1-4 (SMB3)")
        reg_world_1_fort_1_tile_smb3 = world.get_region("World 1-Fort Tile (SMB3)")
        reg_level_1_fort_1_smb3 = world.get_region("Level 1-Fort (SMB3)")
        reg_world_1_5_tile_smb3 = world.get_region("World 1-5 Tile (SMB3)")
        reg_level_1_5_smb3 = world.get_region("Level 1-5 (SMB3)")
        reg_world_1_6_tile_smb3 = world.get_region("World 1-6 Tile (SMB3)")
        reg_level_1_6_smb3 = world.get_region("Level 1-6 (SMB3)")
        reg_world_1_castle_tile_smb3 = world.get_region("World 1-Castle Tile (SMB3)")
        reg_level_1_castle_smb3 = world.get_region("Level 1-Castle (SMB3)")
        # World 2
        reg_world_2_smb3 = world.get_region("World 2 (SMB3)")
        reg_world_2_1_tile_smb3 = world.get_region("World 2-1 Tile (SMB3)")
        reg_level_2_1_smb3 = world.get_region("Level 2-1 (SMB3)")
        reg_world_2_2_tile_smb3 = world.get_region("World 2-2 Tile (SMB3)")
        reg_level_2_2_smb3 = world.get_region("Level 2-2 (SMB3)")
        reg_world_2_fort_1_tile_smb3 = world.get_region("World 2-Fort Tile (SMB3)")
        reg_level_2_fort_1_smb3 = world.get_region("Level 2-Fort (SMB3)")
        reg_world_2_3_tile_smb3 = world.get_region("World 2-3 Tile (SMB3)")
        reg_level_2_3_smb3 = world.get_region("Level 2-3 (SMB3)")
        reg_world_2_sand_tile_smb3 = world.get_region("World 2-Quicksand Tile (SMB3)")
        reg_level_2_sand_smb3 = world.get_region("Level 2-Quicksand (SMB3)")
        reg_world_2_4_tile_smb3 = world.get_region("World 2-4 Tile (SMB3)")
        reg_level_2_4_smb3 = world.get_region("Level 2-4 (SMB3)")
        reg_world_2_5_tile_smb3 = world.get_region("World 2-5 Tile (SMB3)")
        reg_level_2_5_smb3 = world.get_region("Level 2-5 (SMB3)")
        reg_world_2_pyramid_tile_smb3 = world.get_region("World 2-Pyramid Tile (SMB3)")
        reg_level_2_pyramid_smb3 = world.get_region("Level 2-Pyramid (SMB3)")
        reg_world_2_castle_tile_smb3 = world.get_region("World 2-Castle Tile (SMB3)")
        reg_level_2_castle_smb3 = world.get_region("Level 2-Castle (SMB3)")
        # World 3
        reg_world_3_smb3 = world.get_region("World 3 (SMB3)")
        reg_world_3_1_tile_smb3 = world.get_region("World 3-1 Tile (SMB3)")
        reg_level_3_1_smb3 = world.get_region("Level 3-1 (SMB3)")
        reg_world_3_2_tile_smb3 = world.get_region("World 3-2 Tile (SMB3)")
        reg_level_3_2_smb3 = world.get_region("Level 3-2 (SMB3)")
        reg_world_3_3_tile_smb3 = world.get_region("World 3-3 Tile (SMB3)")
        reg_level_3_3_smb3 = world.get_region("Level 3-3 (SMB3)")
        reg_world_3_fort_1_tile_smb3 = world.get_region("World 3-Fort1 Tile (SMB3)")
        reg_level_3_fort_1_smb3 = world.get_region("Level 3-Fort1 (SMB3)")
        reg_world_3_4_tile_smb3 = world.get_region("World 3-4 Tile (SMB3)")
        reg_level_3_4_smb3 = world.get_region("Level 3-4 (SMB3)")
        reg_world_3_5_tile_smb3 = world.get_region("World 3-5 Tile (SMB3)")
        reg_level_3_5_smb3 = world.get_region("Level 3-5 (SMB3)")
        reg_world_3_6_tile_smb3 = world.get_region("World 3-6 Tile (SMB3)")
        reg_level_3_6_smb3 = world.get_region("Level 3-6 (SMB3)")
        reg_world_3_7_tile_smb3 = world.get_region("World 3-7 Tile (SMB3)")
        reg_level_3_7_smb3 = world.get_region("Level 3-7 (SMB3)")
        reg_world_3_fort_2_tile_smb3 = world.get_region("World 3-Fort2 Tile (SMB3)")
        reg_level_3_fort_2_smb3 = world.get_region("Level 3-Fort2 (SMB3)")
        reg_world_3_8_tile_smb3 = world.get_region("World 3-8 Tile (SMB3)")
        reg_level_3_8_smb3 = world.get_region("Level 3-8 (SMB3)")
        reg_world_3_9_tile_smb3 = world.get_region("World 3-9 Tile (SMB3)")
        reg_level_3_9_smb3 = world.get_region("Level 3-9 (SMB3)")
        reg_world_3_castle_tile_smb3 = world.get_region("World 3-Castle Tile (SMB3)")
        reg_level_3_castle_smb3 = world.get_region("Level 3-Castle (SMB3)")
        # World 4
        reg_world_4_smb3 = world.get_region("World 4 (SMB3)")
        reg_world_4_1_tile_smb3 = world.get_region("World 4-1 Tile (SMB3)")
        reg_level_4_1_smb3 = world.get_region("Level 4-1 (SMB3)")
        reg_world_4_2_tile_smb3 = world.get_region("World 4-2 Tile (SMB3)")
        reg_level_4_2_smb3 = world.get_region("Level 4-2 (SMB3)")
        reg_world_4_3_tile_smb3 = world.get_region("World 4-3 Tile (SMB3)")
        reg_level_4_3_smb3 = world.get_region("Level 4-3 (SMB3)")
        reg_world_4_fort_1_tile_smb3 = world.get_region("World 4-Fort1 Tile (SMB3)")
        reg_level_4_fort_1_smb3 = world.get_region("Level 4-Fort1 (SMB3)")
        reg_world_4_4_tile_smb3 = world.get_region("World 4-4 Tile (SMB3)")
        reg_level_4_4_smb3 = world.get_region("Level 4-4 (SMB3)")
        reg_world_4_5_tile_smb3 = world.get_region("World 4-5 Tile (SMB3)")
        reg_level_4_5_smb3 = world.get_region("Level 4-5 (SMB3)")
        reg_world_4_6_tile_smb3 = world.get_region("World 4-6 Tile (SMB3)")
        reg_level_4_6_smb3 = world.get_region("Level 4-6 (SMB3)")
        reg_world_4_fort_2_tile_smb3 = world.get_region("World 4-Fort2 Tile (SMB3)")
        reg_level_4_fort_2_smb3 = world.get_region("Level 4-Fort2 (SMB3)")
        reg_world_4_castle_tile_smb3 = world.get_region("World 4-Castle Tile (SMB3)")
        reg_level_4_castle_smb3 = world.get_region("Level 4-Castle (SMB3)")
        # World 5
        reg_world_5_smb3 = world.get_region("World 5 (SMB3)")
        reg_world_5_1_tile_smb3 = world.get_region("World 5-1 Tile (SMB3)")
        reg_level_5_1_smb3 = world.get_region("Level 5-1 (SMB3)")
        reg_world_5_2_tile_smb3 = world.get_region("World 5-2 Tile (SMB3)")
        reg_level_5_2_smb3 = world.get_region("Level 5-2 (SMB3)")
        reg_world_5_fort_1_tile_smb3 = world.get_region("World 5-Fort1 Tile (SMB3)")
        reg_level_5_fort_1_smb3 = world.get_region("Level 5-Fort1 (SMB3)")
        reg_world_5_3_tile_smb3 = world.get_region("World 5-3 Tile (SMB3)")
        reg_level_5_3_smb3 = world.get_region("Level 5-3 (SMB3)")
        reg_world_5_tower_tile_smb3 = world.get_region("World 5-Tower Tile (SMB3)")
        reg_world_5_4_tile_smb3 = world.get_region("World 5-4 Tile (SMB3)")
        reg_level_5_4_smb3 = world.get_region("Level 5-4 (SMB3)")
        reg_world_5_5_tile_smb3 = world.get_region("World 5-5 Tile (SMB3)")
        reg_level_5_5_smb3 = world.get_region("Level 5-5 (SMB3)")
        reg_world_5_6_tile_smb3 = world.get_region("World 5-6 Tile (SMB3)")
        reg_level_5_6_smb3 = world.get_region("Level 5-6 (SMB3)")
        reg_world_5_7_tile_smb3 = world.get_region("World 5-7 Tile (SMB3)")
        reg_level_5_7_smb3 = world.get_region("Level 5-7 (SMB3)")
        reg_world_5_fort_2_tile_smb3 = world.get_region("World 5-Fort2 Tile (SMB3)")
        reg_level_5_fort_2_smb3 = world.get_region("Level 5-Fort2 (SMB3)")
        reg_world_5_8_tile_smb3 = world.get_region("World 5-8 Tile (SMB3)")
        reg_level_5_8_smb3 = world.get_region("Level 5-8 (SMB3)")
        reg_world_5_9_tile_smb3 = world.get_region("World 5-9 Tile (SMB3)")
        reg_level_5_9_smb3 = world.get_region("Level 5-9 (SMB3)")
        reg_world_5_castle_tile_smb3 = world.get_region("World 5-Castle Tile (SMB3)")
        reg_level_5_castle_smb3 = world.get_region("Level 5-Castle (SMB3)")
        # World 6
        reg_world_6_smb3 = world.get_region("World 6 (SMB3)")
        reg_world_6_1_tile_smb3 = world.get_region("World 6-1 Tile (SMB3)")
        reg_level_6_1_smb3 = world.get_region("Level 6-1 (SMB3)")
        reg_world_6_2_tile_smb3 = world.get_region("World 6-2 Tile (SMB3)")
        reg_level_6_2_smb3 = world.get_region("Level 6-2 (SMB3)")
        reg_world_6_3_tile_smb3 = world.get_region("World 6-3 Tile (SMB3)")
        reg_level_6_3_smb3 = world.get_region("Level 6-3 (SMB3)")
        reg_world_6_fort_1_tile_smb3 = world.get_region("World 6-Fort1 Tile (SMB3)")
        reg_level_6_fort_1_smb3 = world.get_region("Level 6-Fort1 (SMB3)")
        reg_world_6_4_tile_smb3 = world.get_region("World 6-4 Tile (SMB3)")
        reg_level_6_4_smb3 = world.get_region("Level 6-4 (SMB3)")
        reg_world_6_5_tile_smb3 = world.get_region("World 6-5 Tile (SMB3)")
        reg_level_6_5_smb3 = world.get_region("Level 6-5 (SMB3)")
        reg_world_6_6_tile_smb3 = world.get_region("World 6-6 Tile (SMB3)")
        reg_level_6_6_smb3 = world.get_region("Level 6-6 (SMB3)")
        reg_world_6_7_tile_smb3 = world.get_region("World 6-7 Tile (SMB3)")
        reg_level_6_7_smb3 = world.get_region("Level 6-7 (SMB3)")
        reg_world_6_fort_2_tile_smb3 = world.get_region("World 6-Fort2 Tile (SMB3)")
        reg_level_6_fort_2_smb3 = world.get_region("Level 6-Fort2 (SMB3)")
        reg_world_6_8_tile_smb3 = world.get_region("World 6-8 Tile (SMB3)")
        reg_level_6_8_smb3 = world.get_region("Level 6-8 (SMB3)")
        reg_world_6_9_tile_smb3 = world.get_region("World 6-9 Tile (SMB3)")
        reg_level_6_9_smb3 = world.get_region("Level 6-9 (SMB3)")
        reg_world_6_10_tile_smb3 = world.get_region("World 6-10 Tile (SMB3)")
        reg_level_6_10_smb3 = world.get_region("Level 6-10 (SMB3)")
        reg_world_6_fort_3_tile_smb3 = world.get_region("World 6-Fort3 Tile (SMB3)")
        reg_level_6_fort_3_smb3 = world.get_region("Level 6-Fort3 (SMB3)")
        reg_world_6_castle_tile_smb3 = world.get_region("World 6-Castle Tile (SMB3)")
        reg_level_6_castle_smb3 = world.get_region("Level 6-Castle (SMB3)")
        # World 7
        reg_world_7_smb3 = world.get_region("World 7 (SMB3)")
        reg_world_7_1_tile_smb3 = world.get_region("World 7-1 Tile (SMB3)")
        reg_level_7_1_smb3 = world.get_region("Level 7-1 (SMB3)")
        reg_world_7_2_tile_smb3 = world.get_region("World 7-2 Tile (SMB3)")
        reg_level_7_2_smb3 = world.get_region("Level 7-2 (SMB3)")
        reg_world_7_3_tile_smb3 = world.get_region("World 7-3 Tile (SMB3)")
        reg_level_7_3_smb3 = world.get_region("Level 7-3 (SMB3)")
        reg_world_7_4_tile_smb3 = world.get_region("World 7-4 Tile (SMB3)")
        reg_level_7_4_smb3 = world.get_region("Level 7-4 (SMB3)")
        reg_world_7_5_tile_smb3 = world.get_region("World 7-5 Tile (SMB3)")
        reg_level_7_5_smb3 = world.get_region("Level 7-5 (SMB3)")
        reg_world_7_munch_1_tile_smb3 = world.get_region("World 7-Muncher1 Tile (SMB3)")
        reg_level_7_munch_1_smb3 = world.get_region("Level 7-Muncher1 (SMB3)")
        reg_world_7_fort_1_tile_smb3 = world.get_region("World 7-Fort1 Tile (SMB3)")
        reg_level_7_fort_1_smb3 = world.get_region("Level 7-Fort1 (SMB3)")
        reg_world_7_6_tile_smb3 = world.get_region("World 7-6 Tile (SMB3)")
        reg_level_7_6_smb3 = world.get_region("Level 7-6 (SMB3)")
        reg_world_7_7_tile_smb3 = world.get_region("World 7-7 Tile (SMB3)")
        reg_level_7_7_smb3 = world.get_region("Level 7-7 (SMB3)")
        reg_world_7_8_tile_smb3 = world.get_region("World 7-8 Tile (SMB3)")
        reg_level_7_8_smb3 = world.get_region("Level 7-8 (SMB3)")
        reg_world_7_9_tile_smb3 = world.get_region("World 7-9 Tile (SMB3)")
        reg_level_7_9_smb3 = world.get_region("Level 7-9 (SMB3)")
        reg_world_7_fort_2_tile_smb3 = world.get_region("World 7-Fort2 Tile (SMB3)")
        reg_level_7_fort_2_smb3 = world.get_region("Level 7-Fort2 (SMB3)")
        reg_world_7_munch_2_tile_smb3 = world.get_region("World 7-Muncher2 Tile (SMB3)")
        reg_level_7_munch_2_smb3 = world.get_region("Level 7-Muncher2 (SMB3)")
        reg_world_7_castle_tile_smb3 = world.get_region("World 7-Castle Tile (SMB3)")
        reg_level_7_castle_smb3 = world.get_region("Level 7-Castle (SMB3)")
        # World 8
        reg_world_8_smb3 = world.get_region("World 8 (SMB3)")
        reg_world_8_tank_1_tile_smb3 = world.get_region("World 8-Tank1 Tile (SMB3)")
        reg_level_8_tank_1_smb3 = world.get_region("Level 8-Tank1 (SMB3)")
        reg_world_8_navy_tile_smb3 = world.get_region("World 8-Navy Tile (SMB3)")
        reg_level_8_navy_smb3 = world.get_region("Level 8-Navy (SMB3)")
        reg_world_8_airship_tile_smb3 = world.get_region("World 8-Airship Tile (SMB3)")
        reg_level_8_airship_smb3 = world.get_region("Level 8-Airship (SMB3)")
        reg_world_8_hand_1_tile_smb3 = world.get_region("World 8-Hand1 Tile (SMB3)")
        reg_level_8_hand_1_smb3 = world.get_region("Level 8-Hand1 (SMB3)")
        reg_world_8_hand_2_tile_smb3 = world.get_region("World 8-Hand2 Tile (SMB3)")
        reg_level_8_hand_2_smb3 = world.get_region("Level 8-Hand2 (SMB3)")
        reg_world_8_hand_3_tile_smb3 = world.get_region("World 8-Hand3 Tile (SMB3)")
        reg_level_8_hand_3_smb3 = world.get_region("Level 8-Hand3 (SMB3)")
        reg_world_8_1_tile_smb3 = world.get_region("World 8-1 Tile (SMB3)")
        reg_level_8_1_smb3 = world.get_region("Level 8-1 (SMB3)")
        reg_world_8_2_tile_smb3 = world.get_region("World 8-2 Tile (SMB3)")
        reg_level_8_2_smb3 = world.get_region("Level 8-2 (SMB3)")
        reg_world_8_fort_1_tile_smb3 = world.get_region("World 8-Fort Tile (SMB3)")
        reg_level_8_fort_1_smb3 = world.get_region("Level 8-Fort (SMB3)")
        reg_world_8_tank_2_tile_smb3 = world.get_region("World 8-Tank2 Tile (SMB3)")
        reg_level_8_tank_2_smb3 = world.get_region("Level 8-Tank2 (SMB3)")
        reg_world_8_castle_tile_smb3 = world.get_region("World 8-Castle Tile (SMB3)")
        reg_level_8_castle_smb3 = world.get_region("Level 8-Castle (SMB3)")
    
    ##
    ##
    
    # Insert Regular Locations
    if world.options.available_smb1.value != 0:
        # World 1, Locations
        w1_1_smb1_locs = get_location_names_with_ids([loc_name.loc_world_1_1_smb1])
        w1_2_smb1_locs = get_location_names_with_ids([loc_name.loc_world_1_2_smb1])
        w1_3_smb1_locs = get_location_names_with_ids([loc_name.loc_world_1_3_smb1])
        w1_4_smb1_locs = get_location_names_with_ids([loc_name.loc_world_1_4_smb1])
        # World 1, Add to Regions
        reg_level_1_1_smb1.add_locations(w1_1_smb1_locs, SMASWLocation)
        reg_level_1_2_smb1.add_locations(w1_2_smb1_locs, SMASWLocation)
        reg_level_1_3_smb1.add_locations(w1_3_smb1_locs, SMASWLocation)
        reg_level_1_4_smb1.add_locations(w1_4_smb1_locs, SMASWLocation)
        # World 2, Locations
        w2_1_smb1_locs = get_location_names_with_ids([loc_name.loc_world_2_1_smb1])
        w2_2_smb1_locs = get_location_names_with_ids([loc_name.loc_world_2_2_smb1])
        w2_3_smb1_locs = get_location_names_with_ids([loc_name.loc_world_2_3_smb1])
        w2_4_smb1_locs = get_location_names_with_ids([loc_name.loc_world_2_4_smb1])
        # World 2, Add to Regions
        reg_level_2_1_smb1.add_locations(w2_1_smb1_locs, SMASWLocation)
        reg_level_2_2_smb1.add_locations(w2_2_smb1_locs, SMASWLocation)
        reg_level_2_3_smb1.add_locations(w2_3_smb1_locs, SMASWLocation)
        reg_level_2_4_smb1.add_locations(w2_4_smb1_locs, SMASWLocation)
        # World 3, Locations
        w3_1_smb1_locs = get_location_names_with_ids([loc_name.loc_world_3_1_smb1])
        w3_2_smb1_locs = get_location_names_with_ids([loc_name.loc_world_3_2_smb1])
        w3_3_smb1_locs = get_location_names_with_ids([loc_name.loc_world_3_3_smb1])
        w3_4_smb1_locs = get_location_names_with_ids([loc_name.loc_world_3_4_smb1])
        # World 3, Add to Regions
        reg_level_3_1_smb1.add_locations(w3_1_smb1_locs, SMASWLocation)
        reg_level_3_2_smb1.add_locations(w3_2_smb1_locs, SMASWLocation)
        reg_level_3_3_smb1.add_locations(w3_3_smb1_locs, SMASWLocation)
        reg_level_3_4_smb1.add_locations(w3_4_smb1_locs, SMASWLocation)
        # World 4, Locations
        w4_1_smb1_locs = get_location_names_with_ids([loc_name.loc_world_4_1_smb1])
        w4_2_smb1_locs = get_location_names_with_ids([loc_name.loc_world_4_2_smb1])
        w4_3_smb1_locs = get_location_names_with_ids([loc_name.loc_world_4_3_smb1])
        w4_4_smb1_locs = get_location_names_with_ids([loc_name.loc_world_4_4_smb1])
        # World 4, Add to Regions
        reg_level_4_1_smb1.add_locations(w4_1_smb1_locs, SMASWLocation)
        reg_level_4_2_smb1.add_locations(w4_2_smb1_locs, SMASWLocation)
        reg_level_4_3_smb1.add_locations(w4_3_smb1_locs, SMASWLocation)
        reg_level_4_4_smb1.add_locations(w4_4_smb1_locs, SMASWLocation)
        # World 5, Locations
        w5_1_smb1_locs = get_location_names_with_ids([loc_name.loc_world_5_1_smb1])
        w5_2_smb1_locs = get_location_names_with_ids([loc_name.loc_world_5_2_smb1])
        w5_3_smb1_locs = get_location_names_with_ids([loc_name.loc_world_5_3_smb1])
        w5_4_smb1_locs = get_location_names_with_ids([loc_name.loc_world_5_4_smb1])
        # World 5, Add to Regions
        reg_level_5_1_smb1.add_locations(w5_1_smb1_locs, SMASWLocation)
        reg_level_5_2_smb1.add_locations(w5_2_smb1_locs, SMASWLocation)
        reg_level_5_3_smb1.add_locations(w5_3_smb1_locs, SMASWLocation)
        reg_level_5_4_smb1.add_locations(w5_4_smb1_locs, SMASWLocation)
        # World 6, Locations
        w6_1_smb1_locs = get_location_names_with_ids([loc_name.loc_world_6_1_smb1])
        w6_2_smb1_locs = get_location_names_with_ids([loc_name.loc_world_6_2_smb1])
        w6_3_smb1_locs = get_location_names_with_ids([loc_name.loc_world_6_3_smb1])
        w6_4_smb1_locs = get_location_names_with_ids([loc_name.loc_world_6_4_smb1])
        # World 6, Add to Regions
        reg_level_6_1_smb1.add_locations(w6_1_smb1_locs, SMASWLocation)
        reg_level_6_2_smb1.add_locations(w6_2_smb1_locs, SMASWLocation)
        reg_level_6_3_smb1.add_locations(w6_3_smb1_locs, SMASWLocation)
        reg_level_6_4_smb1.add_locations(w6_4_smb1_locs, SMASWLocation)
        # World 7, Locations
        w7_1_smb1_locs = get_location_names_with_ids([loc_name.loc_world_7_1_smb1])
        w7_2_smb1_locs = get_location_names_with_ids([loc_name.loc_world_7_2_smb1])
        w7_3_smb1_locs = get_location_names_with_ids([loc_name.loc_world_7_3_smb1])
        w7_4_smb1_locs = get_location_names_with_ids([loc_name.loc_world_7_4_smb1])
        # World 7, Add to Regions
        reg_level_7_1_smb1.add_locations(w7_1_smb1_locs, SMASWLocation)
        reg_level_7_2_smb1.add_locations(w7_2_smb1_locs, SMASWLocation)
        reg_level_7_3_smb1.add_locations(w7_3_smb1_locs, SMASWLocation)
        reg_level_7_4_smb1.add_locations(w7_4_smb1_locs, SMASWLocation)
        # World 8, Locations
        w8_1_smb1_locs = get_location_names_with_ids([loc_name.loc_world_8_1_smb1])
        w8_2_smb1_locs = get_location_names_with_ids([loc_name.loc_world_8_2_smb1])
        w8_3_smb1_locs = get_location_names_with_ids([loc_name.loc_world_8_3_smb1])
        w8_4_smb1_locs = get_location_names_with_ids([loc_name.loc_world_8_4_smb1])
        # World 8, Add to Regions
        reg_level_8_1_smb1.add_locations(w8_1_smb1_locs, SMASWLocation)
        reg_level_8_2_smb1.add_locations(w8_2_smb1_locs, SMASWLocation)
        reg_level_8_3_smb1.add_locations(w8_3_smb1_locs, SMASWLocation)
        reg_level_8_4_smb1.add_locations(w8_4_smb1_locs, SMASWLocation)
        if world.options.hard_worlds_smb1.value != 0:
            # World X1, Locations
            w1x1_smb1_locs = get_location_names_with_ids([loc_name.loc_world_1x1_smb1])
            w1x2_smb1_locs = get_location_names_with_ids([loc_name.loc_world_1x2_smb1])
            w1x3_smb1_locs = get_location_names_with_ids([loc_name.loc_world_1x3_smb1])
            w1x4_smb1_locs = get_location_names_with_ids([loc_name.loc_world_1x4_smb1])
            # World X1, Add to Regions
            reg_level_1x1_smb1.add_locations(w1x1_smb1_locs, SMASWLocation)
            reg_level_1x2_smb1.add_locations(w1x2_smb1_locs, SMASWLocation)
            reg_level_1x3_smb1.add_locations(w1x3_smb1_locs, SMASWLocation)
            reg_level_1x4_smb1.add_locations(w1x4_smb1_locs, SMASWLocation)
            # World X2, Locations
            w2x1_smb1_locs = get_location_names_with_ids([loc_name.loc_world_2x1_smb1])
            w2x2_smb1_locs = get_location_names_with_ids([loc_name.loc_world_2x2_smb1])
            w2x3_smb1_locs = get_location_names_with_ids([loc_name.loc_world_2x3_smb1])
            w2x4_smb1_locs = get_location_names_with_ids([loc_name.loc_world_2x4_smb1])
            # World X2, Add to Regions
            reg_level_2x1_smb1.add_locations(w2x1_smb1_locs, SMASWLocation)
            reg_level_2x2_smb1.add_locations(w2x2_smb1_locs, SMASWLocation)
            reg_level_2x3_smb1.add_locations(w2x3_smb1_locs, SMASWLocation)
            reg_level_2x4_smb1.add_locations(w2x4_smb1_locs, SMASWLocation)
            # World X3, Locations
            w3x1_smb1_locs = get_location_names_with_ids([loc_name.loc_world_3x1_smb1])
            w3x2_smb1_locs = get_location_names_with_ids([loc_name.loc_world_3x2_smb1])
            w3x3_smb1_locs = get_location_names_with_ids([loc_name.loc_world_3x3_smb1])
            w3x4_smb1_locs = get_location_names_with_ids([loc_name.loc_world_3x4_smb1])
            # World X3, Add to Regions
            reg_level_3x1_smb1.add_locations(w3x1_smb1_locs, SMASWLocation)
            reg_level_3x2_smb1.add_locations(w3x2_smb1_locs, SMASWLocation)
            reg_level_3x3_smb1.add_locations(w3x3_smb1_locs, SMASWLocation)
            reg_level_3x4_smb1.add_locations(w3x4_smb1_locs, SMASWLocation)
            # World X4, Locations
            w4x1_smb1_locs = get_location_names_with_ids([loc_name.loc_world_4x1_smb1])
            w4x2_smb1_locs = get_location_names_with_ids([loc_name.loc_world_4x2_smb1])
            w4x3_smb1_locs = get_location_names_with_ids([loc_name.loc_world_4x3_smb1])
            w4x4_smb1_locs = get_location_names_with_ids([loc_name.loc_world_4x4_smb1])
            # World X4, Add to Regions
            reg_level_4x1_smb1.add_locations(w4x1_smb1_locs, SMASWLocation)
            reg_level_4x2_smb1.add_locations(w4x2_smb1_locs, SMASWLocation)
            reg_level_4x3_smb1.add_locations(w4x3_smb1_locs, SMASWLocation)
            reg_level_4x4_smb1.add_locations(w4x4_smb1_locs, SMASWLocation)
            # World X5, Locations
            w5x1_smb1_locs = get_location_names_with_ids([loc_name.loc_world_5x1_smb1])
            w5x2_smb1_locs = get_location_names_with_ids([loc_name.loc_world_5x2_smb1])
            w5x3_smb1_locs = get_location_names_with_ids([loc_name.loc_world_5x3_smb1])
            w5x4_smb1_locs = get_location_names_with_ids([loc_name.loc_world_5x4_smb1])
            # World X5, Add to Regions
            reg_level_5x1_smb1.add_locations(w5x1_smb1_locs, SMASWLocation)
            reg_level_5x2_smb1.add_locations(w5x2_smb1_locs, SMASWLocation)
            reg_level_5x3_smb1.add_locations(w5x3_smb1_locs, SMASWLocation)
            reg_level_5x4_smb1.add_locations(w5x4_smb1_locs, SMASWLocation)
            # World X6, Locations
            w6x1_smb1_locs = get_location_names_with_ids([loc_name.loc_world_6x1_smb1])
            w6x2_smb1_locs = get_location_names_with_ids([loc_name.loc_world_6x2_smb1])
            w6x3_smb1_locs = get_location_names_with_ids([loc_name.loc_world_6x3_smb1])
            w6x4_smb1_locs = get_location_names_with_ids([loc_name.loc_world_6x4_smb1])
            # World X6, Add to Regions
            reg_level_6x1_smb1.add_locations(w6x1_smb1_locs, SMASWLocation)
            reg_level_6x2_smb1.add_locations(w6x2_smb1_locs, SMASWLocation)
            reg_level_6x3_smb1.add_locations(w6x3_smb1_locs, SMASWLocation)
            reg_level_6x4_smb1.add_locations(w6x4_smb1_locs, SMASWLocation)
            # World X7, Locations
            w7x1_smb1_locs = get_location_names_with_ids([loc_name.loc_world_7x1_smb1])
            w7x2_smb1_locs = get_location_names_with_ids([loc_name.loc_world_7x2_smb1])
            w7x3_smb1_locs = get_location_names_with_ids([loc_name.loc_world_7x3_smb1])
            w7x4_smb1_locs = get_location_names_with_ids([loc_name.loc_world_7x4_smb1])
            # World X7, Add to Regions
            reg_level_7x1_smb1.add_locations(w7x1_smb1_locs, SMASWLocation)
            reg_level_7x2_smb1.add_locations(w7x2_smb1_locs, SMASWLocation)
            reg_level_7x3_smb1.add_locations(w7x3_smb1_locs, SMASWLocation)
            reg_level_7x4_smb1.add_locations(w7x4_smb1_locs, SMASWLocation)
            # World X8, Locations
            w8x1_smb1_locs = get_location_names_with_ids([loc_name.loc_world_8x1_smb1])
            w8x2_smb1_locs = get_location_names_with_ids([loc_name.loc_world_8x2_smb1])
            w8x3_smb1_locs = get_location_names_with_ids([loc_name.loc_world_8x3_smb1])
            w8x4_smb1_locs = get_location_names_with_ids([loc_name.loc_world_8x4_smb1])
            # World X8, Add to Regions
            reg_level_8x1_smb1.add_locations(w8x1_smb1_locs, SMASWLocation)
            reg_level_8x2_smb1.add_locations(w8x2_smb1_locs, SMASWLocation)
            reg_level_8x3_smb1.add_locations(w8x3_smb1_locs, SMASWLocation)
            reg_level_8x4_smb1.add_locations(w8x4_smb1_locs, SMASWLocation)
        #DONE SMB1
    if world.options.available_smbll.value != 0:
        # World 1, Locations
        w1_1_smbll_locs = get_location_names_with_ids([loc_name.loc_world_1_1_smbll])
        w1_2_smbll_locs = get_location_names_with_ids([loc_name.loc_world_1_2_smbll])
        w1_3_smbll_locs = get_location_names_with_ids([loc_name.loc_world_1_3_smbll])
        w1_4_smbll_locs = get_location_names_with_ids([loc_name.loc_world_1_4_smbll])
        # World 1, Add to Regions
        reg_level_1_1_smbll.add_locations(w1_1_smbll_locs, SMASWLocation)
        reg_level_1_2_smbll.add_locations(w1_2_smbll_locs, SMASWLocation)
        reg_level_1_3_smbll.add_locations(w1_3_smbll_locs, SMASWLocation)
        reg_level_1_4_smbll.add_locations(w1_4_smbll_locs, SMASWLocation)
        # World 2, Locations
        w2_1_smbll_locs = get_location_names_with_ids([loc_name.loc_world_2_1_smbll])
        w2_2_smbll_locs = get_location_names_with_ids([loc_name.loc_world_2_2_smbll])
        w2_3_smbll_locs = get_location_names_with_ids([loc_name.loc_world_2_3_smbll])
        w2_4_smbll_locs = get_location_names_with_ids([loc_name.loc_world_2_4_smbll])
        # World 2, Add to Regions
        reg_level_2_1_smbll.add_locations(w2_1_smbll_locs, SMASWLocation)
        reg_level_2_2_smbll.add_locations(w2_2_smbll_locs, SMASWLocation)
        reg_level_2_3_smbll.add_locations(w2_3_smbll_locs, SMASWLocation)
        reg_level_2_4_smbll.add_locations(w2_4_smbll_locs, SMASWLocation)
        # World 3, Locations
        w3_1_smbll_locs = get_location_names_with_ids([loc_name.loc_world_3_1_smbll])
        w3_2_smbll_locs = get_location_names_with_ids([loc_name.loc_world_3_2_smbll])
        w3_3_smbll_locs = get_location_names_with_ids([loc_name.loc_world_3_3_smbll])
        w3_4_smbll_locs = get_location_names_with_ids([loc_name.loc_world_3_4_smbll])
        # World 3, Add to Regions
        reg_level_3_1_smbll.add_locations(w3_1_smbll_locs, SMASWLocation)
        reg_level_3_2_smbll.add_locations(w3_2_smbll_locs, SMASWLocation)
        reg_level_3_3_smbll.add_locations(w3_3_smbll_locs, SMASWLocation)
        reg_level_3_4_smbll.add_locations(w3_4_smbll_locs, SMASWLocation)
        # World 4, Locations
        w4_1_smbll_locs = get_location_names_with_ids([loc_name.loc_world_4_1_smbll])
        w4_2_smbll_locs = get_location_names_with_ids([loc_name.loc_world_4_2_smbll])
        w4_3_smbll_locs = get_location_names_with_ids([loc_name.loc_world_4_3_smbll])
        w4_4_smbll_locs = get_location_names_with_ids([loc_name.loc_world_4_4_smbll])
        # World 4, Add to Regions
        reg_level_4_1_smbll.add_locations(w4_1_smbll_locs, SMASWLocation)
        reg_level_4_2_smbll.add_locations(w4_2_smbll_locs, SMASWLocation)
        reg_level_4_3_smbll.add_locations(w4_3_smbll_locs, SMASWLocation)
        reg_level_4_4_smbll.add_locations(w4_4_smbll_locs, SMASWLocation)
        # World 5, Locations
        w5_1_smbll_locs = get_location_names_with_ids([loc_name.loc_world_5_1_smbll])
        w5_2_smbll_locs = get_location_names_with_ids([loc_name.loc_world_5_2_smbll])
        w5_3_smbll_locs = get_location_names_with_ids([loc_name.loc_world_5_3_smbll])
        w5_4_smbll_locs = get_location_names_with_ids([loc_name.loc_world_5_4_smbll])
        # World 5, Add to Regions
        reg_level_5_1_smbll.add_locations(w5_1_smbll_locs, SMASWLocation)
        reg_level_5_2_smbll.add_locations(w5_2_smbll_locs, SMASWLocation)
        reg_level_5_3_smbll.add_locations(w5_3_smbll_locs, SMASWLocation)
        reg_level_5_4_smbll.add_locations(w5_4_smbll_locs, SMASWLocation)
        # World 6, Locations
        w6_1_smbll_locs = get_location_names_with_ids([loc_name.loc_world_6_1_smbll])
        w6_2_smbll_locs = get_location_names_with_ids([loc_name.loc_world_6_2_smbll])
        w6_3_smbll_locs = get_location_names_with_ids([loc_name.loc_world_6_3_smbll])
        w6_4_smbll_locs = get_location_names_with_ids([loc_name.loc_world_6_4_smbll])
        # World 6, Add to Regions
        reg_level_6_1_smbll.add_locations(w6_1_smbll_locs, SMASWLocation)
        reg_level_6_2_smbll.add_locations(w6_2_smbll_locs, SMASWLocation)
        reg_level_6_3_smbll.add_locations(w6_3_smbll_locs, SMASWLocation)
        reg_level_6_4_smbll.add_locations(w6_4_smbll_locs, SMASWLocation)
        # World 7, Locations
        w7_1_smbll_locs = get_location_names_with_ids([loc_name.loc_world_7_1_smbll])
        w7_2_smbll_locs = get_location_names_with_ids([loc_name.loc_world_7_2_smbll])
        w7_3_smbll_locs = get_location_names_with_ids([loc_name.loc_world_7_3_smbll])
        w7_4_smbll_locs = get_location_names_with_ids([loc_name.loc_world_7_4_smbll])
        # World 7, Add to Regions
        reg_level_7_1_smbll.add_locations(w7_1_smbll_locs, SMASWLocation)
        reg_level_7_2_smbll.add_locations(w7_2_smbll_locs, SMASWLocation)
        reg_level_7_3_smbll.add_locations(w7_3_smbll_locs, SMASWLocation)
        reg_level_7_4_smbll.add_locations(w7_4_smbll_locs, SMASWLocation)
        # World 8, Locations
        w8_1_smbll_locs = get_location_names_with_ids([loc_name.loc_world_8_1_smbll])
        w8_2_smbll_locs = get_location_names_with_ids([loc_name.loc_world_8_2_smbll])
        w8_3_smbll_locs = get_location_names_with_ids([loc_name.loc_world_8_3_smbll])
        w8_4_smbll_locs = get_location_names_with_ids([loc_name.loc_world_8_4_smbll])
        # World 8, Add to Regions
        reg_level_8_1_smbll.add_locations(w8_1_smbll_locs, SMASWLocation)
        reg_level_8_2_smbll.add_locations(w8_2_smbll_locs, SMASWLocation)
        reg_level_8_3_smbll.add_locations(w8_3_smbll_locs, SMASWLocation)
        reg_level_8_4_smbll.add_locations(w8_4_smbll_locs, SMASWLocation)
        if world.options.fantasy_world_smbll.value != 0:
            # World 9, Locations
            w9_1_smbll_locs = get_location_names_with_ids([loc_name.loc_world_fantasy_1_smbll])
            w9_2_smbll_locs = get_location_names_with_ids([loc_name.loc_world_fantasy_2_smbll])
            w9_3_smbll_locs = get_location_names_with_ids([loc_name.loc_world_fantasy_3_smbll])
            w9_4_smbll_locs = get_location_names_with_ids([loc_name.loc_world_fantasy_4_smbll])
            # World 9, Add to Regions
            reg_level_9_1_smbll.add_locations(w9_1_smbll_locs, SMASWLocation)
            reg_level_9_2_smbll.add_locations(w9_2_smbll_locs, SMASWLocation)
            reg_level_9_3_smbll.add_locations(w9_3_smbll_locs, SMASWLocation)
            reg_level_9_4_smbll.add_locations(w9_4_smbll_locs, SMASWLocation)
        if world.options.bonus_worlds_smbll.value != 0:
            # World A, Locations
            wa_1_smbll_locs = get_location_names_with_ids([loc_name.loc_world_a_1_smbll])
            wa_2_smbll_locs = get_location_names_with_ids([loc_name.loc_world_a_2_smbll])
            wa_3_smbll_locs = get_location_names_with_ids([loc_name.loc_world_a_3_smbll])
            wa_4_smbll_locs = get_location_names_with_ids([loc_name.loc_world_a_4_smbll])
            # World A, Add to Regions
            reg_level_a_1_smbll.add_locations(wa_1_smbll_locs, SMASWLocation)
            reg_level_a_2_smbll.add_locations(wa_2_smbll_locs, SMASWLocation)
            reg_level_a_3_smbll.add_locations(wa_3_smbll_locs, SMASWLocation)
            reg_level_a_4_smbll.add_locations(wa_4_smbll_locs, SMASWLocation)
            # World B, Locations
            wb_1_smbll_locs = get_location_names_with_ids([loc_name.loc_world_b_1_smbll])
            wb_2_smbll_locs = get_location_names_with_ids([loc_name.loc_world_b_2_smbll])
            wb_3_smbll_locs = get_location_names_with_ids([loc_name.loc_world_b_3_smbll])
            wb_4_smbll_locs = get_location_names_with_ids([loc_name.loc_world_b_4_smbll])
            # World B, Add to Regions
            reg_level_b_1_smbll.add_locations(wb_1_smbll_locs, SMASWLocation)
            reg_level_b_2_smbll.add_locations(wb_2_smbll_locs, SMASWLocation)
            reg_level_b_3_smbll.add_locations(wb_3_smbll_locs, SMASWLocation)
            reg_level_b_4_smbll.add_locations(wb_4_smbll_locs, SMASWLocation)
            # World C, Locations
            wc_1_smbll_locs = get_location_names_with_ids([loc_name.loc_world_c_1_smbll])
            wc_2_smbll_locs = get_location_names_with_ids([loc_name.loc_world_c_2_smbll])
            wc_3_smbll_locs = get_location_names_with_ids([loc_name.loc_world_c_3_smbll])
            wc_4_smbll_locs = get_location_names_with_ids([loc_name.loc_world_c_4_smbll])
            # World C, Add to Regions
            reg_level_c_1_smbll.add_locations(wc_1_smbll_locs, SMASWLocation)
            reg_level_c_2_smbll.add_locations(wc_2_smbll_locs, SMASWLocation)
            reg_level_c_3_smbll.add_locations(wc_3_smbll_locs, SMASWLocation)
            reg_level_c_4_smbll.add_locations(wc_4_smbll_locs, SMASWLocation)
            # World D, Locations
            wd_1_smbll_locs = get_location_names_with_ids([loc_name.loc_world_d_1_smbll])
            wd_2_smbll_locs = get_location_names_with_ids([loc_name.loc_world_d_2_smbll])
            wd_3_smbll_locs = get_location_names_with_ids([loc_name.loc_world_d_3_smbll])
            wd_4_smbll_locs = get_location_names_with_ids([loc_name.loc_world_d_4_smbll])
            # World D, Add to Regions
            reg_level_d_1_smbll.add_locations(wd_1_smbll_locs, SMASWLocation)
            reg_level_d_2_smbll.add_locations(wd_2_smbll_locs, SMASWLocation)
            reg_level_d_3_smbll.add_locations(wd_3_smbll_locs, SMASWLocation)
            reg_level_d_4_smbll.add_locations(wd_4_smbll_locs, SMASWLocation)
        #DONE SMBLL
    if world.options.available_smb2.value != 0:
        # Character Select Locations
        if world.options.char_select_checks_smb2.value != 0:
            if world.options.char_select_checks_smb2.value&2 == 2:
                char_sel_locs = get_location_names_with_ids(
                    [loc_name.loc_char_pick_mario_smb2, loc_name.loc_char_pick_peach_smb2, loc_name.loc_char_pick_toad_smb2, loc_name.loc_char_pick_luigi_smb2]
                )
                char_sel_smb2.add_locations(char_sel_locs, SMASWLocation)
            if world.options.char_select_checks_smb2.value&1 == 1:
                char_sel_locs = get_location_names_with_ids(
                    [loc_name.loc_char_view_mario_smb2, loc_name.loc_char_view_peach_smb2, loc_name.loc_char_view_toad_smb2, loc_name.loc_char_view_luigi_smb2]
                )
                char_sel_smb2.add_locations(char_sel_locs, SMASWLocation)
        # World 1, Locations
        w1_1_smb2_locs = get_location_names_with_ids(
            [loc_name.loc_world_1_1_smb2,loc_name.loc_world_1_1_smb2_mush_1,loc_name.loc_world_1_1_smb2_mush_2]
        )
        w1_2_smb2_locs = get_location_names_with_ids(
            [loc_name.loc_world_1_2_smb2,loc_name.loc_world_1_2_smb2_mush_1,loc_name.loc_world_1_2_smb2_mush_2]
        )
        w1_3_smb2_locs = get_location_names_with_ids(
            [loc_name.loc_world_1_3_smb2,loc_name.loc_world_1_3_smb2_mush_1,loc_name.loc_world_1_3_smb2_mush_2]
        )
        # World 1, Add to Regions
        reg_level_1_1_smb2.add_locations(w1_1_smb2_locs, SMASWLocation)
        reg_level_1_2_smb2.add_locations(w1_2_smb2_locs, SMASWLocation)
        reg_level_1_3_smb2.add_locations(w1_3_smb2_locs, SMASWLocation)
        # World 2, Locations
        w2_1_smb2_locs = get_location_names_with_ids(
            [loc_name.loc_world_2_1_smb2,loc_name.loc_world_2_1_smb2_mush_1]
        )
        w2_2_smb2_locs = get_location_names_with_ids(
            [loc_name.loc_world_2_2_smb2,loc_name.loc_world_2_2_smb2_mush_1,loc_name.loc_world_2_2_smb2_mush_2]
        )
        w2_3_smb2_locs = get_location_names_with_ids(
            [loc_name.loc_world_2_3_smb2,loc_name.loc_world_2_3_smb2_mush_1,loc_name.loc_world_2_3_smb2_mush_2]
        )
        # World 2, Add to Regions
        reg_level_2_1_smb2.add_locations(w2_1_smb2_locs, SMASWLocation)
        reg_level_2_2_smb2.add_locations(w2_2_smb2_locs, SMASWLocation)
        reg_level_2_3_smb2.add_locations(w2_3_smb2_locs, SMASWLocation)
        # World 3, Locations
        w3_1_smb2_locs = get_location_names_with_ids(
            [loc_name.loc_world_3_1_smb2,loc_name.loc_world_3_1_smb2_mush_1,loc_name.loc_world_3_1_smb2_mush_2]
        )
        w3_2_smb2_locs = get_location_names_with_ids(
            [loc_name.loc_world_3_2_smb2,loc_name.loc_world_3_2_smb2_mush_1,loc_name.loc_world_3_2_smb2_mush_2]
        )
        w3_3_smb2_locs = get_location_names_with_ids(
            [loc_name.loc_world_3_3_smb2,loc_name.loc_world_3_3_smb2_mush_1,loc_name.loc_world_3_3_smb2_mush_2]
        )
        # World 3, Add to Regions
        reg_level_3_1_smb2.add_locations(w3_1_smb2_locs, SMASWLocation)
        reg_level_3_2_smb2.add_locations(w3_2_smb2_locs, SMASWLocation)
        reg_level_3_3_smb2.add_locations(w3_3_smb2_locs, SMASWLocation)
        # World 4, Locations
        w4_1_smb2_locs = get_location_names_with_ids(
            [loc_name.loc_world_4_1_smb2,loc_name.loc_world_4_1_smb2_mush_1,loc_name.loc_world_4_1_smb2_mush_2]
        )
        w4_2_smb2_locs = get_location_names_with_ids(
            [loc_name.loc_world_4_2_smb2,loc_name.loc_world_4_2_smb2_mush_1,loc_name.loc_world_4_2_smb2_mush_2]
        )
        w4_3_smb2_locs = get_location_names_with_ids(
            [loc_name.loc_world_4_3_smb2,loc_name.loc_world_4_3_smb2_mush_1,loc_name.loc_world_4_3_smb2_mush_2]
        )
        # World 4, Add to Regions
        reg_level_4_1_smb2.add_locations(w4_1_smb2_locs, SMASWLocation)
        reg_level_4_2_smb2.add_locations(w4_2_smb2_locs, SMASWLocation)
        reg_level_4_3_smb2.add_locations(w4_3_smb2_locs, SMASWLocation)
        # World 5, Locations
        w5_1_smb2_locs = get_location_names_with_ids(
            [loc_name.loc_world_5_1_smb2,loc_name.loc_world_5_1_smb2_mush_1,loc_name.loc_world_5_1_smb2_mush_2]
        )
        w5_2_smb2_locs = get_location_names_with_ids(
            [loc_name.loc_world_5_2_smb2,loc_name.loc_world_5_2_smb2_mush_1,loc_name.loc_world_5_2_smb2_mush_2]
        )
        w5_3_smb2_locs = get_location_names_with_ids(
            [loc_name.loc_world_5_3_smb2,loc_name.loc_world_5_3_smb2_mush_1,loc_name.loc_world_5_3_smb2_mush_2]
        )
        # World 5, Add to Regions
        reg_level_5_1_smb2.add_locations(w5_1_smb2_locs, SMASWLocation)
        reg_level_5_2_smb2.add_locations(w5_2_smb2_locs, SMASWLocation)
        reg_level_5_3_smb2.add_locations(w5_3_smb2_locs, SMASWLocation)
        # World 6, Locations
        w6_1_smb2_locs = get_location_names_with_ids(
            [loc_name.loc_world_6_1_smb2,loc_name.loc_world_6_1_smb2_mush_1,loc_name.loc_world_6_1_smb2_mush_2]
        )
        w6_2_smb2_locs = get_location_names_with_ids(
            [loc_name.loc_world_6_2_smb2,loc_name.loc_world_6_2_smb2_mush_1]
        )
        w6_3_smb2_locs = get_location_names_with_ids(
            [loc_name.loc_world_6_3_smb2,loc_name.loc_world_6_3_smb2_mush_1,loc_name.loc_world_6_3_smb2_mush_2]
        )
        # World 6, Add to Regions
        reg_level_6_1_smb2.add_locations(w6_1_smb2_locs, SMASWLocation)
        reg_level_6_2_smb2.add_locations(w6_2_smb2_locs, SMASWLocation)
        reg_level_6_3_smb2.add_locations(w6_3_smb2_locs, SMASWLocation)
        # World 7, Locations
        w7_1_smb2_locs = get_location_names_with_ids(
            [loc_name.loc_world_7_1_smb2,loc_name.loc_world_7_1_smb2_mush_1,loc_name.loc_world_7_1_smb2_mush_2]
        )
        w7_2_smb2_locs = get_location_names_with_ids(
            [loc_name.loc_world_7_2_smb2,loc_name.loc_world_7_2_smb2_mush_1,loc_name.loc_world_7_2_smb2_mush_2]
        )
        # World 7, Add to Regions
        reg_level_7_1_smb2.add_locations(w7_1_smb2_locs, SMASWLocation)
        reg_level_7_2_smb2.add_locations(w7_2_smb2_locs, SMASWLocation)
        # TODO: Add the Extra Mushrooms
        #DONE SMB2
    if world.options.available_smb3.value != 0:
        #menu.connect(reg_game_smb3)
        #reg_game_smb3
        # TODO: Mushroom Houses, Spade Games, Bro Fights, Etc.
        # Handle Locations Fetching First
        # World 1
        w1_1_smb3_locs = get_location_names_with_ids([loc_name.loc_world_1_1_smb3])
        w1_2_smb3_locs = get_location_names_with_ids([loc_name.loc_world_1_2_smb3])
        w1_3_smb3_locs = get_location_names_with_ids([loc_name.loc_world_1_3_smb3])
        w1_4_smb3_locs = get_location_names_with_ids([loc_name.loc_world_1_4_smb3])
        w1_fort_1_smb3_locs = get_location_names_with_ids([loc_name.loc_world_1_fort_1_smb3])
        w1_5_smb3_locs = get_location_names_with_ids([loc_name.loc_world_1_5_smb3])
        w1_6_smb3_locs = get_location_names_with_ids([loc_name.loc_world_1_6_smb3])
        w1_castle_smb3_locs = get_location_names_with_ids([loc_name.loc_world_1_castle_smb3])
        # World 2
        w2_1_smb3_locs = get_location_names_with_ids([loc_name.loc_world_2_1_smb3])
        w2_2_smb3_locs = get_location_names_with_ids([loc_name.loc_world_2_2_smb3])
        w2_fort_1_smb3_locs = get_location_names_with_ids([loc_name.loc_world_2_fort_1_smb3])
        w2_3_smb3_locs = get_location_names_with_ids([loc_name.loc_world_2_3_smb3])
        w2_sand_smb3_locs = get_location_names_with_ids([loc_name.loc_world_2_sand_smb3])
        w2_4_smb3_locs = get_location_names_with_ids([loc_name.loc_world_2_4_smb3])
        w2_5_smb3_locs = get_location_names_with_ids([loc_name.loc_world_2_5_smb3])
        w2_pyramid_smb3_locs = get_location_names_with_ids([loc_name.loc_world_2_pyramid_smb3])
        w2_castle_smb3_locs = get_location_names_with_ids([loc_name.loc_world_2_castle_smb3])
        # World 3
        w3_1_smb3_locs = get_location_names_with_ids([loc_name.loc_world_3_1_smb3])
        w3_2_smb3_locs = get_location_names_with_ids([loc_name.loc_world_3_2_smb3])
        w3_3_smb3_locs = get_location_names_with_ids([loc_name.loc_world_3_3_smb3])
        w3_fort_1_smb3_locs = get_location_names_with_ids([loc_name.loc_world_3_fort_1_smb3])
        w3_4_smb3_locs = get_location_names_with_ids([loc_name.loc_world_3_4_smb3])
        w3_5_smb3_locs = get_location_names_with_ids([loc_name.loc_world_3_5_smb3])
        w3_6_smb3_locs = get_location_names_with_ids([loc_name.loc_world_3_6_smb3])
        w3_7_smb3_locs = get_location_names_with_ids([loc_name.loc_world_3_7_smb3])
        w3_fort_2_smb3_locs = get_location_names_with_ids([loc_name.loc_world_3_fort_2_smb3])
        w3_8_smb3_locs = get_location_names_with_ids([loc_name.loc_world_3_8_smb3])
        w3_9_smb3_locs = get_location_names_with_ids([loc_name.loc_world_3_9_smb3])
        w3_castle_smb3_locs = get_location_names_with_ids([loc_name.loc_world_3_castle_smb3])
        # World 4
        w4_1_smb3_locs = get_location_names_with_ids([loc_name.loc_world_4_1_smb3])
        w4_2_smb3_locs = get_location_names_with_ids([loc_name.loc_world_4_2_smb3])
        w4_3_smb3_locs = get_location_names_with_ids([loc_name.loc_world_4_3_smb3])
        w4_fort_1_smb3_locs = get_location_names_with_ids([loc_name.loc_world_4_fort_1_smb3])
        w4_4_smb3_locs = get_location_names_with_ids([loc_name.loc_world_4_4_smb3])
        w4_5_smb3_locs = get_location_names_with_ids([loc_name.loc_world_4_5_smb3])
        w4_6_smb3_locs = get_location_names_with_ids([loc_name.loc_world_4_6_smb3])
        w4_fort_2_smb3_locs = get_location_names_with_ids([loc_name.loc_world_4_fort_2_smb3])
        w4_castle_smb3_locs = get_location_names_with_ids([loc_name.loc_world_4_castle_smb3])
        # World 5
        w5_1_smb3_locs = get_location_names_with_ids([loc_name.loc_world_5_1_smb3])
        w5_2_smb3_locs = get_location_names_with_ids([loc_name.loc_world_5_2_smb3])
        w5_fort_1_smb3_locs = get_location_names_with_ids([loc_name.loc_world_5_fort_1_smb3])
        w5_3_smb3_locs = get_location_names_with_ids([loc_name.loc_world_5_3_smb3])
        w5_4_smb3_locs = get_location_names_with_ids([loc_name.loc_world_5_4_smb3])
        w5_5_smb3_locs = get_location_names_with_ids([loc_name.loc_world_5_5_smb3])
        w5_6_smb3_locs = get_location_names_with_ids([loc_name.loc_world_5_6_smb3])
        w5_7_smb3_locs = get_location_names_with_ids([loc_name.loc_world_5_7_smb3])
        w5_fort_2_smb3_locs = get_location_names_with_ids([loc_name.loc_world_5_fort_2_smb3])
        w5_8_smb3_locs = get_location_names_with_ids([loc_name.loc_world_5_8_smb3])
        w5_9_smb3_locs = get_location_names_with_ids([loc_name.loc_world_5_9_smb3])
        w5_castle_smb3_locs = get_location_names_with_ids([loc_name.loc_world_5_castle_smb3])
        # World 6
        w6_1_smb3_locs = get_location_names_with_ids([loc_name.loc_world_6_1_smb3])
        w6_2_smb3_locs = get_location_names_with_ids([loc_name.loc_world_6_2_smb3])
        w6_3_smb3_locs = get_location_names_with_ids([loc_name.loc_world_6_3_smb3])
        w6_fort_1_smb3_locs = get_location_names_with_ids([loc_name.loc_world_6_fort_1_smb3])
        w6_4_smb3_locs = get_location_names_with_ids([loc_name.loc_world_6_4_smb3])
        w6_5_smb3_locs = get_location_names_with_ids([loc_name.loc_world_6_5_smb3])
        w6_6_smb3_locs = get_location_names_with_ids([loc_name.loc_world_6_6_smb3])
        w6_7_smb3_locs = get_location_names_with_ids([loc_name.loc_world_6_7_smb3])
        w6_fort_2_smb3_locs = get_location_names_with_ids([loc_name.loc_world_6_fort_2_smb3])
        w6_8_smb3_locs = get_location_names_with_ids([loc_name.loc_world_6_8_smb3])
        w6_9_smb3_locs = get_location_names_with_ids([loc_name.loc_world_6_9_smb3])
        w6_10_smb3_locs = get_location_names_with_ids([loc_name.loc_world_6_10_smb3])
        w6_fort_3_smb3_locs = get_location_names_with_ids([loc_name.loc_world_6_fort_3_smb3])
        w6_castle_smb3_locs = get_location_names_with_ids([loc_name.loc_world_6_castle_smb3])
        # World 7
        w7_1_smb3_locs = get_location_names_with_ids([loc_name.loc_world_7_1_smb3])
        w7_2_smb3_locs = get_location_names_with_ids([loc_name.loc_world_7_2_smb3])
        w7_3_smb3_locs = get_location_names_with_ids([loc_name.loc_world_7_3_smb3])
        w7_4_smb3_locs = get_location_names_with_ids([loc_name.loc_world_7_4_smb3])
        w7_5_smb3_locs = get_location_names_with_ids([loc_name.loc_world_7_5_smb3])
        # Dead-end M.House Tile Here
        w7_munch_1_smb3_locs = get_location_names_with_ids([loc_name.loc_world_7_munch_1_smb3])
        w7_fort_1_smb3_locs = get_location_names_with_ids([loc_name.loc_world_7_fort_1_smb3])
        w7_6_smb3_locs = get_location_names_with_ids([loc_name.loc_world_7_6_smb3])
        w7_7_smb3_locs = get_location_names_with_ids([loc_name.loc_world_7_7_smb3])
        w7_8_smb3_locs = get_location_names_with_ids([loc_name.loc_world_7_8_smb3])
        w7_9_smb3_locs = get_location_names_with_ids([loc_name.loc_world_7_9_smb3])
        w7_fort_2_smb3_locs = get_location_names_with_ids([loc_name.loc_world_7_fort_2_smb3])
        w7_munch_2_smb3_locs = get_location_names_with_ids([loc_name.loc_world_7_munch_2_smb3])
        w7_castle_smb3_locs = get_location_names_with_ids([loc_name.loc_world_7_castle_smb3])
        # World 8
        w8_tank_1_smb3_locs = get_location_names_with_ids([loc_name.loc_world_8_tank_1_smb3])
        w8_navy_smb3_locs = get_location_names_with_ids([loc_name.loc_world_8_navy_smb3])
        # Hands can technically be skipped if RNG allows it
        w8_hand_1_smb3_locs = get_location_names_with_ids([loc_name.loc_world_8_hand_1_smb3])
        w8_hand_2_smb3_locs = get_location_names_with_ids([loc_name.loc_world_8_hand_2_smb3])
        w8_hand_3_smb3_locs = get_location_names_with_ids([loc_name.loc_world_8_hand_3_smb3])
        # Back to Regular
        w8_airship_smb3_locs = get_location_names_with_ids([loc_name.loc_world_8_airship_smb3])
        w8_1_smb3_locs = get_location_names_with_ids([loc_name.loc_world_8_1_smb3])
        w8_2_smb3_locs = get_location_names_with_ids([loc_name.loc_world_8_2_smb3])
        w8_fort_1_smb3_locs = get_location_names_with_ids([loc_name.loc_world_8_fort_1_smb3])
        w8_tank_2_smb3_locs = get_location_names_with_ids([loc_name.loc_world_8_tank_2_smb3])
        w8_castle_smb3_locs = get_location_names_with_ids([loc_name.loc_world_8_castle_smb3])
        # Handle Adding Locations Next
        # World 1
        reg_level_1_1_smb3.add_locations(w1_1_smb3_locs, SMASWLocation)
        reg_level_1_2_smb3.add_locations(w1_2_smb3_locs, SMASWLocation)
        reg_level_1_3_smb3.add_locations(w1_3_smb3_locs, SMASWLocation)
        reg_level_1_4_smb3.add_locations(w1_4_smb3_locs, SMASWLocation)
        reg_level_1_fort_1_smb3.add_locations(w1_fort_1_smb3_locs, SMASWLocation)
        reg_level_1_5_smb3.add_locations(w1_5_smb3_locs, SMASWLocation)
        reg_level_1_6_smb3.add_locations(w1_6_smb3_locs, SMASWLocation)
        reg_level_1_castle_smb3.add_locations(w1_castle_smb3_locs, SMASWLocation)
        # World 2
        reg_level_2_1_smb3.add_locations(w2_1_smb3_locs, SMASWLocation)
        reg_level_2_2_smb3.add_locations(w2_2_smb3_locs, SMASWLocation)
        reg_level_2_fort_1_smb3.add_locations(w2_fort_1_smb3_locs, SMASWLocation)
        reg_level_2_3_smb3.add_locations(w2_3_smb3_locs, SMASWLocation)
        reg_level_2_sand_smb3.add_locations(w2_sand_smb3_locs, SMASWLocation)
        reg_level_2_4_smb3.add_locations(w2_4_smb3_locs, SMASWLocation)
        reg_level_2_5_smb3.add_locations(w2_5_smb3_locs, SMASWLocation)
        reg_level_2_pyramid_smb3.add_locations(w2_pyramid_smb3_locs, SMASWLocation)
        reg_level_2_castle_smb3.add_locations(w2_castle_smb3_locs, SMASWLocation)
        # World 3
        reg_level_3_1_smb3.add_locations(w3_1_smb3_locs, SMASWLocation)
        reg_level_3_2_smb3.add_locations(w3_2_smb3_locs, SMASWLocation)
        reg_level_3_3_smb3.add_locations(w3_3_smb3_locs, SMASWLocation)
        reg_level_3_fort_1_smb3.add_locations(w3_fort_1_smb3_locs, SMASWLocation)
        reg_level_3_4_smb3.add_locations(w3_4_smb3_locs, SMASWLocation)
        reg_level_3_5_smb3.add_locations(w3_5_smb3_locs, SMASWLocation)
        reg_level_3_6_smb3.add_locations(w3_6_smb3_locs, SMASWLocation)
        reg_level_3_7_smb3.add_locations(w3_7_smb3_locs, SMASWLocation)
        reg_level_3_fort_2_smb3.add_locations(w3_fort_2_smb3_locs, SMASWLocation)
        reg_level_3_8_smb3.add_locations(w3_8_smb3_locs, SMASWLocation)
        reg_level_3_9_smb3.add_locations(w3_9_smb3_locs, SMASWLocation)
        reg_level_3_castle_smb3.add_locations(w3_castle_smb3_locs, SMASWLocation)
        # World 4
        reg_level_4_1_smb3.add_locations(w4_1_smb3_locs, SMASWLocation)
        reg_level_4_2_smb3.add_locations(w4_2_smb3_locs, SMASWLocation)
        reg_level_4_3_smb3.add_locations(w4_3_smb3_locs, SMASWLocation)
        reg_level_4_fort_1_smb3.add_locations(w4_fort_1_smb3_locs, SMASWLocation)
        reg_level_4_4_smb3.add_locations(w4_4_smb3_locs, SMASWLocation)
        reg_level_4_5_smb3.add_locations(w4_5_smb3_locs, SMASWLocation)
        reg_level_4_6_smb3.add_locations(w4_6_smb3_locs, SMASWLocation)
        reg_level_4_fort_2_smb3.add_locations(w4_fort_2_smb3_locs, SMASWLocation)
        reg_level_4_castle_smb3.add_locations(w4_castle_smb3_locs, SMASWLocation)
        # World 5
        reg_level_5_1_smb3.add_locations(w5_1_smb3_locs, SMASWLocation)
        reg_level_5_2_smb3.add_locations(w5_2_smb3_locs, SMASWLocation)
        reg_level_5_fort_1_smb3.add_locations(w5_fort_1_smb3_locs, SMASWLocation)
        reg_level_5_3_smb3.add_locations(w5_3_smb3_locs, SMASWLocation)
        reg_level_5_4_smb3.add_locations(w5_4_smb3_locs, SMASWLocation)
        reg_level_5_5_smb3.add_locations(w5_5_smb3_locs, SMASWLocation)
        reg_level_5_6_smb3.add_locations(w5_6_smb3_locs, SMASWLocation)
        reg_level_5_7_smb3.add_locations(w5_7_smb3_locs, SMASWLocation)
        reg_level_5_fort_2_smb3.add_locations(w5_fort_2_smb3_locs, SMASWLocation)
        reg_level_5_8_smb3.add_locations(w5_8_smb3_locs, SMASWLocation)
        reg_level_5_9_smb3.add_locations(w5_9_smb3_locs, SMASWLocation)
        reg_level_5_castle_smb3.add_locations(w5_castle_smb3_locs, SMASWLocation)
        # World 6
        reg_level_6_1_smb3.add_locations(w6_1_smb3_locs, SMASWLocation)
        reg_level_6_2_smb3.add_locations(w6_2_smb3_locs, SMASWLocation)
        reg_level_6_3_smb3.add_locations(w6_3_smb3_locs, SMASWLocation)
        reg_level_6_fort_1_smb3.add_locations(w6_fort_1_smb3_locs, SMASWLocation)
        reg_level_6_4_smb3.add_locations(w6_4_smb3_locs, SMASWLocation)
        reg_level_6_5_smb3.add_locations(w6_5_smb3_locs, SMASWLocation)
        reg_level_6_6_smb3.add_locations(w6_6_smb3_locs, SMASWLocation)
        reg_level_6_7_smb3.add_locations(w6_7_smb3_locs, SMASWLocation)
        reg_level_6_fort_2_smb3.add_locations(w6_fort_2_smb3_locs, SMASWLocation)
        reg_level_6_8_smb3.add_locations(w6_8_smb3_locs, SMASWLocation)
        reg_level_6_9_smb3.add_locations(w6_9_smb3_locs, SMASWLocation)
        reg_level_6_10_smb3.add_locations(w6_10_smb3_locs, SMASWLocation)
        reg_level_6_fort_3_smb3.add_locations(w6_fort_3_smb3_locs, SMASWLocation)
        reg_level_6_castle_smb3.add_locations(w6_castle_smb3_locs, SMASWLocation)
        # World 7
        reg_level_7_1_smb3.add_locations(w7_1_smb3_locs, SMASWLocation)
        reg_level_7_2_smb3.add_locations(w7_2_smb3_locs, SMASWLocation)
        reg_level_7_3_smb3.add_locations(w7_3_smb3_locs, SMASWLocation)
        reg_level_7_4_smb3.add_locations(w7_4_smb3_locs, SMASWLocation)
        reg_level_7_5_smb3.add_locations(w7_5_smb3_locs, SMASWLocation)
        # Dead-end M.House Tile Here
        reg_level_7_munch_1_smb3.add_locations(w7_munch_1_smb3_locs, SMASWLocation)
        reg_level_7_fort_1_smb3.add_locations(w7_fort_1_smb3_locs, SMASWLocation)
        reg_level_7_6_smb3.add_locations(w7_6_smb3_locs, SMASWLocation)
        reg_level_7_7_smb3.add_locations(w7_7_smb3_locs, SMASWLocation)
        reg_level_7_8_smb3.add_locations(w7_8_smb3_locs, SMASWLocation)
        reg_level_7_9_smb3.add_locations(w7_9_smb3_locs, SMASWLocation)
        reg_level_7_fort_2_smb3.add_locations(w7_fort_2_smb3_locs, SMASWLocation)
        reg_level_7_munch_2_smb3.add_locations(w7_munch_2_smb3_locs, SMASWLocation)
        reg_level_7_castle_smb3.add_locations(w7_castle_smb3_locs, SMASWLocation)
        # World 8
        reg_level_8_tank_1_smb3.add_locations(w8_tank_1_smb3_locs, SMASWLocation)
        reg_level_8_navy_smb3.add_locations(w8_navy_smb3_locs, SMASWLocation)
        # Hands can technically be skipped if RNG allows it
        reg_level_8_hand_1_smb3.add_locations(w8_hand_1_smb3_locs, SMASWLocation)
        reg_level_8_hand_2_smb3.add_locations(w8_hand_2_smb3_locs, SMASWLocation)
        reg_level_8_hand_3_smb3.add_locations(w8_hand_3_smb3_locs, SMASWLocation)
        # Back to Regular
        reg_level_8_airship_smb3.add_locations(w8_airship_smb3_locs, SMASWLocation)
        reg_level_8_1_smb3.add_locations(w8_1_smb3_locs, SMASWLocation)
        reg_level_8_2_smb3.add_locations(w8_2_smb3_locs, SMASWLocation)
        reg_level_8_fort_1_smb3.add_locations(w8_fort_1_smb3_locs, SMASWLocation)
        reg_level_8_tank_2_smb3.add_locations(w8_tank_2_smb3_locs, SMASWLocation)
        reg_level_8_castle_smb3.add_locations(w8_castle_smb3_locs, SMASWLocation)
        #DONE SMB#



def create_events(world: SMASWWorld) -> None:
    ## Sometimes, the player may perform in-game actions that allow them to progress which are not related to Items.
    ## In our case, the player must press a button in the top left room to open the final boss door.
    ## AP has something for this purpose: "Event locations" and "Event items".
    ## An event location is no different than a regular location, except it has the address "None".
    ## It is treated during generation like any other location, but then it is discarded.
    ## This location cannot be "sent" and its item cannot be "received", but the item can be used in logic rules.
    ## Since we are creating more locations and adding them to regions, we need to grab those regions again first.
    #top_left_room = world.get_region("Top Left Room")
    #final_boss_room = world.get_region("Final Boss Room")
    #
    ## One way to create an event is simply to use one of the normal methods of creating a location.
    #button_in_top_left_room = SMASWLocation(world.player, "Top Left Room Button", None, top_left_room)
    #top_left_room.locations.append(button_in_top_left_room)
    #
    ## We then need to put an event item onto the location.
    ## An event item is an item whose code is "None" (same as the event location's address),
    ## and whose classification is "progression". Item creation will be discussed more in items.py.
    ## Note: Usually, items are created in world.create_items(), which for us happens in items.py.
    ## However, when the location of an item is known ahead of time (as is the case with an event location/item pair),
    ## it is common practice to create the item when creating the location.
    ## Since locations also have to be finalized after world.create_regions(), which runs before world.create_items(),
    ## we'll create both the event location and the event item in our locations.py code.
    #button_item = items.SMASWItem("Top Left Room Button Pressed", ItemClassification.progression, None, world.player)
    #button_in_top_left_room.place_locked_item(button_item)
    #
    ## A way simpler way to do create an event location/item pair is by using the region.create_event helper.
    ## Luckily, we have another event we want to create: The Victory event.
    ## We will use this event to track whether the player can win the game.
    ## The Victory event is a completely optional abstraction - This will be discussed more in set_rules().
    #final_boss_room.add_event( # NOTE NOTE NOTE: Location Name, then Item Name
    #    "Final Boss Defeated", "Victory", location_type=SMASWLocation, item_type=items.SMASWItem
    #)
    
    # Fetch required Regions, except only the ones we want this time.
    menu = world.get_region("Game Select") # Probably not necessary, but it's here
    smasw_req_goals = world.get_region("Completed Required SubGoals")
    smasw_goals = world.get_region("Completed All SubGoals")

    # SMB1
    if world.options.available_smb1.value != 0:
        reg_goal_smb1 = world.get_region("SMB1 Goal")
        # World Castles
        reg_level_1_4_smb1 = world.get_region("Level 1-4 (SMB1)")
        reg_level_2_4_smb1 = world.get_region("Level 2-4 (SMB1)")
        reg_level_3_4_smb1 = world.get_region("Level 3-4 (SMB1)")
        reg_level_4_4_smb1 = world.get_region("Level 4-4 (SMB1)")
        reg_level_5_4_smb1 = world.get_region("Level 5-4 (SMB1)")
        reg_level_6_4_smb1 = world.get_region("Level 6-4 (SMB1)")
        reg_level_7_4_smb1 = world.get_region("Level 7-4 (SMB1)")
        reg_level_8_4_smb1 = world.get_region("Level 8-4 (SMB1)")
        # Hardmode Worlds
        if world.options.hard_worlds_smb1.value != 0:
            # World Castles
            reg_level_1x4_smb1 = world.get_region("Level 1x4 (SMB1)")
            reg_level_2x4_smb1 = world.get_region("Level 2x4 (SMB1)")
            reg_level_3x4_smb1 = world.get_region("Level 3x4 (SMB1)")
            reg_level_4x4_smb1 = world.get_region("Level 4x4 (SMB1)")
            reg_level_5x4_smb1 = world.get_region("Level 5x4 (SMB1)")
            reg_level_6x4_smb1 = world.get_region("Level 6x4 (SMB1)")
            reg_level_7x4_smb1 = world.get_region("Level 7x4 (SMB1)")
            reg_level_8x4_smb1 = world.get_region("Level 8x4 (SMB1)")

    # SMBLL
    if world.options.available_smbll.value != 0:
        reg_goal_smbll = world.get_region("SMBLL Goal")
        # World Castles
        reg_level_1_4_smbll = world.get_region("Level 1-4 (SMBLL)")
        reg_level_2_4_smbll = world.get_region("Level 2-4 (SMBLL)")
        reg_level_3_4_smbll = world.get_region("Level 3-4 (SMBLL)")
        reg_level_4_4_smbll = world.get_region("Level 4-4 (SMBLL)")
        reg_level_5_4_smbll = world.get_region("Level 5-4 (SMBLL)")
        reg_level_6_4_smbll = world.get_region("Level 6-4 (SMBLL)")
        reg_level_7_4_smbll = world.get_region("Level 7-4 (SMBLL)")
        reg_level_8_4_smbll = world.get_region("Level 8-4 (SMBLL)")
        # Fantasy World (World 9) doesn't have a boss, skip
        # Bonus Worlds
        if world.options.bonus_worlds_smbll.value != 0:
            reg_level_a_4_smbll = world.get_region("Level A-4 (SMBLL)")
            reg_level_b_4_smbll = world.get_region("Level B-4 (SMBLL)")
            reg_level_c_4_smbll = world.get_region("Level C-4 (SMBLL)")
            reg_level_d_4_smbll = world.get_region("Level D-4 (SMBLL)")

    # SMB2
    if world.options.available_smb2.value != 0:
        reg_game_smb2 = world.get_region("SMB2 Game")
        # World Bosses
        reg_level_1_3_smb2 = world.get_region("Level 1-3 (SMB2)")
        reg_level_2_3_smb2 = world.get_region("Level 2-3 (SMB2)")
        reg_level_3_3_smb2 = world.get_region("Level 3-3 (SMB2)")
        reg_level_4_3_smb2 = world.get_region("Level 4-3 (SMB2)")
        reg_level_5_3_smb2 = world.get_region("Level 5-3 (SMB2)")
        reg_level_6_3_smb2 = world.get_region("Level 6-3 (SMB2)")
        reg_level_7_2_smb2 = world.get_region("Level 7-2 (SMB2)")

    # SMB3
    if world.options.available_smb3.value != 0:
        #reg_game_smb3 = world.get_region("SMB3 Game")
        # TODO: Mushroom Houses? Hammer Bro Fights Inventory?
        # World 1
        #reg_level_1_fort_1_smb3 = world.get_region("Level 1-Fort (SMB3)")
        reg_level_1_castle_smb3 = world.get_region("Level 1-Castle (SMB3)")
        # World 2
        #reg_level_2_fort_1_smb3 = world.get_region("Level 2-Fort (SMB3)")
        reg_level_2_castle_smb3 = world.get_region("Level 2-Castle (SMB3)")
        # World 3
        #reg_level_3_fort_1_smb3 = world.get_region("Level 3-Fort1 (SMB3)")
        #reg_level_3_fort_2_smb3 = world.get_region("Level 3-Fort2 (SMB3)")
        reg_level_3_castle_smb3 = world.get_region("Level 3-Castle (SMB3)")
        # World 4
        #reg_level_4_fort_1_smb3 = world.get_region("Level 4-Fort1 (SMB3)")
        #reg_level_4_fort_2_smb3 = world.get_region("Level 4-Fort2 (SMB3)")
        reg_level_4_castle_smb3 = world.get_region("Level 4-Castle (SMB3)")
        # World 5
        #reg_level_5_fort_1_smb3 = world.get_region("Level 5-Fort1 (SMB3)")
        #reg_level_5_fort_2_smb3 = world.get_region("Level 5-Fort2 (SMB3)")
        reg_level_5_castle_smb3 = world.get_region("Level 5-Castle (SMB3)")
        # World 6
        #reg_level_6_fort_1_smb3 = world.get_region("Level 6-Fort1 (SMB3)")
        #reg_level_6_fort_2_smb3 = world.get_region("Level 6-Fort2 (SMB3)")
        #reg_level_6_fort_3_smb3 = world.get_region("Level 6-Fort3 (SMB3)")
        reg_level_6_castle_smb3 = world.get_region("Level 6-Castle (SMB3)")
        # World 7, Munchers are uncommented since they can drop Inventory Treasures.
        #reg_world_7_munch_1_tile_smb3 = world.get_region("World 7-Muncher1 Tile (SMB3)")
        #reg_level_7_munch_1_smb3 = world.get_region("Level 7-Muncher1 (SMB3)")
        #reg_level_7_fort_1_smb3 = world.get_region("Level 7-Fort1 (SMB3)")
        #reg_level_7_fort_2_smb3 = world.get_region("Level 7-Fort2 (SMB3)")
        #reg_world_7_munch_2_tile_smb3 = world.get_region("World 7-Muncher2 Tile (SMB3)")
        #reg_level_7_munch_2_smb3 = world.get_region("Level 7-Muncher2 (SMB3)")
        reg_level_7_castle_smb3 = world.get_region("Level 7-Castle (SMB3)")
        # World 8, some tiles can drop Inventory Treasures
        #reg_world_8_tank_1_tile_smb3 = world.get_region("World 8-Tank1 Tile (SMB3)")
        #reg_level_8_tank_1_smb3 = world.get_region("Level 8-Tank1 (SMB3)")
        #reg_world_8_hand_1_tile_smb3 = world.get_region("World 8-Hand1 Tile (SMB3)")
        #reg_level_8_hand_1_smb3 = world.get_region("Level 8-Hand1 (SMB3)")
        #reg_world_8_hand_2_tile_smb3 = world.get_region("World 8-Hand2 Tile (SMB3)")
        #reg_level_8_hand_2_smb3 = world.get_region("Level 8-Hand2 (SMB3)")
        #reg_world_8_hand_3_tile_smb3 = world.get_region("World 8-Hand3 Tile (SMB3)")
        #reg_level_8_hand_3_smb3 = world.get_region("Level 8-Hand3 (SMB3)")
        #reg_level_8_fort_1_smb3 = world.get_region("Level 8-Fort (SMB3)")
        reg_level_8_castle_smb3 = world.get_region("Level 8-Castle (SMB3)")
    
    ##
    ##
    
    # Start adding the MetaLocations w/ MetaItems
    
    
    smasw_goals.add_event(
        loc_name.loc_goal_smasw, item_name.goal_smasw,
        location_type=SMASWLocation, item_type=items.SMASWItem
    )

    # SMB1
    if world.options.available_smb1.value != 0:
        reg_goal_smb1.add_event(loc_name.loc_goal_smb1, item_name.goal_smb1, location_type=SMASWLocation, item_type=items.SMASWItem)
        # World Castles
        reg_level_1_4_smb1.add_event(loc_name.loc_boss_1_smb1, item_name.bosscoin_smb1, location_type=SMASWLocation, item_type=items.SMASWItem)
        reg_level_2_4_smb1.add_event(loc_name.loc_boss_2_smb1, item_name.bosscoin_smb1, location_type=SMASWLocation, item_type=items.SMASWItem)
        reg_level_3_4_smb1.add_event(loc_name.loc_boss_3_smb1, item_name.bosscoin_smb1, location_type=SMASWLocation, item_type=items.SMASWItem)
        reg_level_4_4_smb1.add_event(loc_name.loc_boss_4_smb1, item_name.bosscoin_smb1, location_type=SMASWLocation, item_type=items.SMASWItem)
        reg_level_5_4_smb1.add_event(loc_name.loc_boss_5_smb1, item_name.bosscoin_smb1, location_type=SMASWLocation, item_type=items.SMASWItem)
        reg_level_6_4_smb1.add_event(loc_name.loc_boss_6_smb1, item_name.bosscoin_smb1, location_type=SMASWLocation, item_type=items.SMASWItem)
        reg_level_7_4_smb1.add_event(loc_name.loc_boss_7_smb1, item_name.bosscoin_smb1, location_type=SMASWLocation, item_type=items.SMASWItem)
        reg_level_8_4_smb1.add_event(loc_name.loc_boss_8_smb1, item_name.bosscoin_smb1, location_type=SMASWLocation, item_type=items.SMASWItem)
        #if world.options.goal_smb1.value == GoalSmb1.option_final_bowser or world.options.goal_smb1.value == GoalSmb1.option_both_bowsers:
        #    reg_level_8_4_smb1.add_event(loc_name.loc_goal_smb1_part, item_name.goal_smb1_part, location_type=SMASWLocation, item_type=items.SMASWItem)
        reg_level_8_4_smb1.add_event(loc_name.loc_goal_smb1_part, item_name.goal_smb1_part, location_type=SMASWLocation, item_type=items.SMASWItem)
        # Hardmode Worlds
        if world.options.hard_worlds_smb1.value != 0:
            # World Castles
            reg_level_1x4_smb1.add_event(loc_name.loc_boss_x1_smb1, item_name.bosscoin_smb1, location_type=SMASWLocation, item_type=items.SMASWItem)
            reg_level_2x4_smb1.add_event(loc_name.loc_boss_x2_smb1, item_name.bosscoin_smb1, location_type=SMASWLocation, item_type=items.SMASWItem)
            reg_level_3x4_smb1.add_event(loc_name.loc_boss_x3_smb1, item_name.bosscoin_smb1, location_type=SMASWLocation, item_type=items.SMASWItem)
            reg_level_4x4_smb1.add_event(loc_name.loc_boss_x4_smb1, item_name.bosscoin_smb1, location_type=SMASWLocation, item_type=items.SMASWItem)
            reg_level_5x4_smb1.add_event(loc_name.loc_boss_x5_smb1, item_name.bosscoin_smb1, location_type=SMASWLocation, item_type=items.SMASWItem)
            reg_level_6x4_smb1.add_event(loc_name.loc_boss_x6_smb1, item_name.bosscoin_smb1, location_type=SMASWLocation, item_type=items.SMASWItem)
            reg_level_7x4_smb1.add_event(loc_name.loc_boss_x7_smb1, item_name.bosscoin_smb1, location_type=SMASWLocation, item_type=items.SMASWItem)
            reg_level_8x4_smb1.add_event(loc_name.loc_boss_x8_smb1, item_name.bosscoin_smb1, location_type=SMASWLocation, item_type=items.SMASWItem)
            #if world.options.goal_smb1.value == GoalSmb1.option_true_bowser or world.options.goal_smb1.value == GoalSmb1.option_both_bowsers:
            #    reg_level_8x4_smb1.add_event(loc_name.loc_goal_smb1_true, item_name.goal_smb1_true, location_type=SMASWLocation, item_type=items.SMASWItem)
            reg_level_8x4_smb1.add_event(loc_name.loc_goal_smb1_true, item_name.goal_smb1_true, location_type=SMASWLocation, item_type=items.SMASWItem)

    # SMBLL
    if world.options.available_smbll.value != 0:
        reg_goal_smbll.add_event(loc_name.loc_goal_smbll, item_name.goal_smbll, location_type=SMASWLocation, item_type=items.SMASWItem)
        # World Castles
        reg_level_1_4_smbll.add_event(loc_name.loc_boss_1_smbll, item_name.bosscoin_smbll, location_type=SMASWLocation, item_type=items.SMASWItem)
        reg_level_2_4_smbll.add_event(loc_name.loc_boss_2_smbll, item_name.bosscoin_smbll, location_type=SMASWLocation, item_type=items.SMASWItem)
        reg_level_3_4_smbll.add_event(loc_name.loc_boss_3_smbll, item_name.bosscoin_smbll, location_type=SMASWLocation, item_type=items.SMASWItem)
        reg_level_4_4_smbll.add_event(loc_name.loc_boss_4_smbll, item_name.bosscoin_smbll, location_type=SMASWLocation, item_type=items.SMASWItem)
        reg_level_5_4_smbll.add_event(loc_name.loc_boss_5_smbll, item_name.bosscoin_smbll, location_type=SMASWLocation, item_type=items.SMASWItem)
        reg_level_6_4_smbll.add_event(loc_name.loc_boss_6_smbll, item_name.bosscoin_smbll, location_type=SMASWLocation, item_type=items.SMASWItem)
        reg_level_7_4_smbll.add_event(loc_name.loc_boss_7_smbll, item_name.bosscoin_smbll, location_type=SMASWLocation, item_type=items.SMASWItem)
        reg_level_8_4_smbll.add_event(loc_name.loc_boss_8_smbll, item_name.bosscoin_smbll, location_type=SMASWLocation, item_type=items.SMASWItem)
        #if world.options.goal_smbll.value == GoalSmbll.option_final_bowser or world.options.goal_smbll.value == GoalSmbll.option_both_bowsers:
        #    reg_level_8_4_smbll.add_event(loc_name.loc_goal_smbll_part, item_name.goal_smbll_part, location_type=SMASWLocation, item_type=items.SMASWItem)
        reg_level_8_4_smbll.add_event(loc_name.loc_goal_smbll_part, item_name.goal_smbll_part, location_type=SMASWLocation, item_type=items.SMASWItem)
        # Fantasy World (World 9) doesn't have a boss, skip
        # Bonus Worlds
        if world.options.bonus_worlds_smbll.value != 0:
            reg_level_a_4_smbll.add_event(loc_name.loc_boss_a_smbll, item_name.bosscoin_smbll, location_type=SMASWLocation, item_type=items.SMASWItem)
            reg_level_b_4_smbll.add_event(loc_name.loc_boss_b_smbll, item_name.bosscoin_smbll, location_type=SMASWLocation, item_type=items.SMASWItem)
            reg_level_c_4_smbll.add_event(loc_name.loc_boss_c_smbll, item_name.bosscoin_smbll, location_type=SMASWLocation, item_type=items.SMASWItem)
            reg_level_d_4_smbll.add_event(loc_name.loc_boss_d_smbll, item_name.bosscoin_smbll, location_type=SMASWLocation, item_type=items.SMASWItem)
            #if world.options.goal_smbll.value == GoalSmbll.option_true_bowser or world.options.goal_smbll.value == GoalSmbll.option_both_bowsers:
            #    reg_level_d_4_smbll.add_event(loc_name.loc_goal_smbll_true, item_name.goal_smbll_true, location_type=SMASWLocation, item_type=items.SMASWItem)
            reg_level_d_4_smbll.add_event(loc_name.loc_goal_smbll_true, item_name.goal_smbll_true, location_type=SMASWLocation, item_type=items.SMASWItem)

    # SMB2
    if world.options.available_smb2.value != 0:
        reg_level_1_3_smb2.add_event(loc_name.loc_boss_1_smb2, item_name.bosscoin_smb2, location_type=SMASWLocation, item_type=items.SMASWItem)
        reg_level_2_3_smb2.add_event(loc_name.loc_boss_2_smb2, item_name.bosscoin_smb2, location_type=SMASWLocation, item_type=items.SMASWItem)
        reg_level_3_3_smb2.add_event(loc_name.loc_boss_3_smb2, item_name.bosscoin_smb2, location_type=SMASWLocation, item_type=items.SMASWItem)
        reg_level_4_3_smb2.add_event(loc_name.loc_boss_4_smb2, item_name.bosscoin_smb2, location_type=SMASWLocation, item_type=items.SMASWItem)
        reg_level_5_3_smb2.add_event(loc_name.loc_boss_5_smb2, item_name.bosscoin_smb2, location_type=SMASWLocation, item_type=items.SMASWItem)
        reg_level_6_3_smb2.add_event(loc_name.loc_boss_6_smb2, item_name.bosscoin_smb2, location_type=SMASWLocation, item_type=items.SMASWItem)
        reg_level_7_2_smb2.add_event(loc_name.loc_boss_7_smb2, item_name.bosscoin_smb2, location_type=SMASWLocation, item_type=items.SMASWItem)
        reg_level_7_2_smb2.add_event(loc_name.loc_goal_smb2, item_name.goal_smb2, location_type=SMASWLocation, item_type=items.SMASWItem)

    # SMB3
    if world.options.available_smb3.value != 0:
        reg_level_1_castle_smb3.add_event(loc_name.loc_boss_1_smb3, item_name.bosscoin_smb3, location_type=SMASWLocation, item_type=items.SMASWItem)
        reg_level_2_castle_smb3.add_event(loc_name.loc_boss_2_smb3, item_name.bosscoin_smb3, location_type=SMASWLocation, item_type=items.SMASWItem)
        reg_level_3_castle_smb3.add_event(loc_name.loc_boss_3_smb3, item_name.bosscoin_smb3, location_type=SMASWLocation, item_type=items.SMASWItem)
        reg_level_4_castle_smb3.add_event(loc_name.loc_boss_4_smb3, item_name.bosscoin_smb3, location_type=SMASWLocation, item_type=items.SMASWItem)
        reg_level_5_castle_smb3.add_event(loc_name.loc_boss_5_smb3, item_name.bosscoin_smb3, location_type=SMASWLocation, item_type=items.SMASWItem)
        reg_level_6_castle_smb3.add_event(loc_name.loc_boss_6_smb3, item_name.bosscoin_smb3, location_type=SMASWLocation, item_type=items.SMASWItem)
        reg_level_7_castle_smb3.add_event(loc_name.loc_boss_7_smb3, item_name.bosscoin_smb3, location_type=SMASWLocation, item_type=items.SMASWItem)
        reg_level_8_castle_smb3.add_event(loc_name.loc_boss_8_smb3, item_name.bosscoin_smb3, location_type=SMASWLocation, item_type=items.SMASWItem)
        reg_level_8_castle_smb3.add_event(loc_name.loc_goal_smb3, item_name.goal_smb3, location_type=SMASWLocation, item_type=items.SMASWItem)
        
        
        
        
    

    # If you create all your regions and locations line-by-line like this,
    # the length of your create_regions might get out of hand.
    # Many worlds use more data-driven approaches using dataclasses or NamedTuples.
    # However, it is worth understanding how the actual creation of regions and locations works,
    # That way, we're not just mindlessly copy-pasting! :)
