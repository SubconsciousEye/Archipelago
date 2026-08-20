from __future__ import annotations

import typing
from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification as Classed
from worlds.AutoWorld import World
from .names import item_name

if TYPE_CHECKING:
    from .world import SMASWWorld

## Every item must have a unique integer ID associated with it.
## We will have a lookup from item name to ID here that, in world.py, we will import and bind to the world class.
## Even if an item doesn't exist on specific options, it must be present in this lookup.
#ITEM_NAME_TO_ID = {
#    "Key": 1,
#    "Sword": 2,
#    "Shield": 3,
#    "Hammer": 4,
#    "Health Upgrade": 5,
#    "Confetti Cannon": 6,
#    "Math Trap": 7,
#}
#
## Items should have a defined default classification.
## In our case, we will make a dictionary from item name to classification.
#DEFAULT_ITEM_CLASSIFICATIONS = {
#    "Key": ItemClassification.progression,
#    "Sword": ItemClassification.progression | ItemClassification.useful,  # Items can have multiple classifications.
#    "Shield": ItemClassification.progression,
#    "Hammer": ItemClassification.progression,
#    "Health Upgrade": ItemClassification.useful,
#    "Confetti Cannon": ItemClassification.filler,
#    "Math Trap": ItemClassification.trap,
#}

class ItemData(typing.NamedTuple):
    idcode: typing.Optional[int]
    classify: Classed
    group: typing.Optional[str]

# Some Offsets
BASE_OFFSET = 0x53A53000
GAME_OFFSET_SMB1 = 0
GAME_OFFSET_SMBLL = 1
GAME_OFFSET_SMB2 = 2
GAME_OFFSET_SMB3 = 3
GAME_OFFSET_SMW = 4

class SMASWItem(Item):
    game = "Super Mario All-Stars + Super Mario World"

# Begin
# Item IDs are handled a bit weirdly due to a number of reasons:
# A) We may not have nearly as much space for SNES Code for each unique Item
# B) The Item Receiver is shared between all subgames
# C) Makes it a bit easier to handle Local-Game Item Links (e.g. Linking SMB3 and SMW's Mounts)

# World Keys
world_keys = {
    # SMB1, Normal
    item_name.key_world_1_smb1: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB1 * 0x20) + 0x00, Classed.progression,
                                                       "Gate Keys"),
    item_name.key_world_2_smb1: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB1 * 0x20) + 0x01, Classed.progression,
                                        "Gate Keys"),
    item_name.key_world_3_smb1: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB1 * 0x20) + 0x02, Classed.progression,
                                        "Gate Keys"),
    item_name.key_world_4_smb1: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB1 * 0x20) + 0x03, Classed.progression,
                                        "Gate Keys"),
    item_name.key_world_5_smb1: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB1 * 0x20) + 0x04, Classed.progression,
                                        "Gate Keys"),
    item_name.key_world_6_smb1: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB1 * 0x20) + 0x05, Classed.progression,
                                        "Gate Keys"),
    item_name.key_world_7_smb1: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB1 * 0x20) + 0x06, Classed.progression,
                                        "Gate Keys"),
    item_name.key_world_8_smb1: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB1 * 0x20) + 0x07, Classed.progression,
                                        "Gate Keys"),
    item_name.key_world_x1_smb1: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB1 * 0x20) + 0x08, Classed.progression,
                                                       "Gate Keys"),
    item_name.key_world_x2_smb1: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB1 * 0x20) + 0x09, Classed.progression,
                                        "Gate Keys"),
    item_name.key_world_x3_smb1: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB1 * 0x20) + 0x0a, Classed.progression,
                                        "Gate Keys"),
    item_name.key_world_x4_smb1: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB1 * 0x20) + 0x0b, Classed.progression,
                                        "Gate Keys"),
    item_name.key_world_x5_smb1: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB3 * 0x20) + 0x08, Classed.progression,
                                        "Gate Keys"),
    item_name.key_world_x6_smb1: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB3 * 0x20) + 0x09, Classed.progression,
                                        "Gate Keys"),
    item_name.key_world_x7_smb1: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB3 * 0x20) + 0x0a, Classed.progression,
                                        "Gate Keys"),
    item_name.key_world_x8_smb1: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB3 * 0x20) + 0x0b, Classed.progression,
                                        "Gate Keys"),
    item_name.key_prog_smb1: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB1 * 0x20) + 0x0f, Classed.progression,
                                        "Gate Keys"),
    # SMBLL, Normal
    item_name.key_world_1_smbll: ItemData(BASE_OFFSET + (GAME_OFFSET_SMBLL * 0x20) + 0x00, Classed.progression,
                                         "Gate Keys"),
    item_name.key_world_2_smbll: ItemData(BASE_OFFSET + (GAME_OFFSET_SMBLL * 0x20) + 0x01, Classed.progression,
                                         "Gate Keys"),
    item_name.key_world_3_smbll: ItemData(BASE_OFFSET + (GAME_OFFSET_SMBLL * 0x20) + 0x02, Classed.progression,
                                         "Gate Keys"),
    item_name.key_world_4_smbll: ItemData(BASE_OFFSET + (GAME_OFFSET_SMBLL * 0x20) + 0x03, Classed.progression,
                                         "Gate Keys"),
    item_name.key_world_5_smbll: ItemData(BASE_OFFSET + (GAME_OFFSET_SMBLL * 0x20) + 0x04, Classed.progression,
                                         "Gate Keys"),
    item_name.key_world_6_smbll: ItemData(BASE_OFFSET + (GAME_OFFSET_SMBLL * 0x20) + 0x05, Classed.progression,
                                         "Gate Keys"),
    item_name.key_world_7_smbll: ItemData(BASE_OFFSET + (GAME_OFFSET_SMBLL * 0x20) + 0x06, Classed.progression,
                                         "Gate Keys"),
    item_name.key_world_8_smbll: ItemData(BASE_OFFSET + (GAME_OFFSET_SMBLL * 0x20) + 0x07, Classed.progression,
                                         "Gate Keys"),
    item_name.key_world_a_smbll: ItemData(BASE_OFFSET + (GAME_OFFSET_SMBLL * 0x20) + 0x09, Classed.progression,
                                         "Gate Keys"),
    item_name.key_world_b_smbll: ItemData(BASE_OFFSET + (GAME_OFFSET_SMBLL * 0x20) + 0x0a, Classed.progression,
                                         "Gate Keys"),
    item_name.key_world_c_smbll: ItemData(BASE_OFFSET + (GAME_OFFSET_SMBLL * 0x20) + 0x0b, Classed.progression,
                                         "Gate Keys"),
    item_name.key_world_d_smbll: ItemData(BASE_OFFSET + (GAME_OFFSET_SMBLL * 0x20) + 0x0c, Classed.progression,
                                         "Gate Keys"),
    item_name.key_prog_smbll: ItemData(BASE_OFFSET + (GAME_OFFSET_SMBLL * 0x20) + 0x0f, Classed.progression,
                                         "Gate Keys"),
    # SMB1+SMBLL, CrossCombo and Bonuses
    item_name.key_world_minus: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB1 * 0x20) + 0x0c, Classed.progression,
                                         "Bonus Keys"),
    item_name.key_world_fantasy: ItemData(BASE_OFFSET + (GAME_OFFSET_SMBLL * 0x20) + 0x08, Classed.progression,
                                         "Bonus Keys"),
    item_name.key_prog_crosscombo: ItemData(BASE_OFFSET + (GAME_OFFSET_SMBLL * 0x20) + 0x0e, Classed.progression,
                                         "Gate Keys"),
    # SMB2
    item_name.key_world_1_smb2: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB2 * 0x20) + 0x00, Classed.progression,
                                         "Gate Keys"),
    item_name.key_world_2_smb2: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB2 * 0x20) + 0x01, Classed.progression,
                                         "Gate Keys"),
    item_name.key_world_3_smb2: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB2 * 0x20) + 0x02, Classed.progression,
                                         "Gate Keys"),
    item_name.key_world_4_smb2: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB2 * 0x20) + 0x03, Classed.progression,
                                         "Gate Keys"),
    item_name.key_world_5_smb2: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB2 * 0x20) + 0x04, Classed.progression,
                                         "Gate Keys"),
    item_name.key_world_6_smb2: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB2 * 0x20) + 0x05, Classed.progression,
                                         "Gate Keys"),
    item_name.key_world_7_smb2: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB2 * 0x20) + 0x06, Classed.progression,
                                         "Gate Keys"),
    item_name.key_prog_smb2: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB2 * 0x20) + 0x0f, Classed.progression,
                                         "Gate Keys"),
    # SMB3
    item_name.key_world_1_smb3: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB3 * 0x20) + 0x00, Classed.progression,
                                         "Gate Keys"),
    item_name.key_world_2_smb3: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB3 * 0x20) + 0x01, Classed.progression,
                                         "Gate Keys"),
    item_name.key_world_3_smb3: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB3 * 0x20) + 0x02, Classed.progression,
                                         "Gate Keys"),
    item_name.key_world_4_smb3: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB3 * 0x20) + 0x03, Classed.progression,
                                         "Gate Keys"),
    item_name.key_world_5_smb3: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB3 * 0x20) + 0x04, Classed.progression,
                                         "Gate Keys"),
    item_name.key_world_6_smb3: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB3 * 0x20) + 0x05, Classed.progression,
                                         "Gate Keys"),
    item_name.key_world_7_smb3: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB3 * 0x20) + 0x06, Classed.progression,
                                         "Gate Keys"),
    item_name.key_world_8_smb3: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB3 * 0x20) + 0x07, Classed.progression,
                                         "Gate Keys"),
    item_name.key_prog_smb3: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB3 * 0x20) + 0x0f, Classed.progression,
                                         "Gate Keys"),
    # SMW's Game Unlock
    item_name.key_game_smw: ItemData(BASE_OFFSET + (GAME_OFFSET_SMW * 0x20) + 0x0f, Classed.progression,
                                         "Gate Keys"),
}

# Egghunt Eggs
egghunt = {
    item_name.egghunt_smb1: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB1 * 0x20) + 0x0d,
                                    Classed.progression_skip_balancing, "Egghunt Eggs"),
    item_name.egghunt_smbll: ItemData(BASE_OFFSET + (GAME_OFFSET_SMBLL * 0x20) + 0x0d,
                                    Classed.progression_skip_balancing, "Egghunt Eggs"),
    item_name.egghunt_smb2: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB2 * 0x20) + 0x0d,
                                    Classed.progression_skip_balancing, "Egghunt Eggs"),
    item_name.egghunt_smb3: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB3 * 0x20) + 0x0d,
                                    Classed.progression_skip_balancing, "Egghunt Eggs"),
    item_name.egghunt_smw: ItemData(BASE_OFFSET + (GAME_OFFSET_SMW * 0x20) + 0x0d,
                                    Classed.progression_skip_balancing, "Egghunt Eggs"),
}

# Auxiliary Important Unlocks
char_unlocks = {
    # Not sure what to classify these as, had them at Useful at first
    item_name.unlock_char_mario: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB2 * 0x20) + 0x08,
                                         Classed.progression_skip_balancing, "Character Unlocks"),
    item_name.unlock_char_luigi: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB2 * 0x20) + 0x09,
                                         Classed.progression_skip_balancing, "Character Unlocks"),
    item_name.unlock_char_peach: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB2 * 0x20) + 0x0a,
                                         Classed.progression_skip_balancing, "Character Unlocks"),
    item_name.unlock_char_toad: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB2 * 0x20) + 0x0b,
                                         Classed.progression_skip_balancing, "Character Unlocks"),
}

switch_palaces = {
    item_name.unlock_switch_yellow: ItemData(BASE_OFFSET + (GAME_OFFSET_SMW * 0x20) + 0x09,
                                         Classed.progression, "Switch Palaces"),
    item_name.unlock_switch_green: ItemData(BASE_OFFSET + (GAME_OFFSET_SMW * 0x20) + 0x0a,
                                         Classed.progression, "Switch Palaces"),
    item_name.unlock_switch_red: ItemData(BASE_OFFSET + (GAME_OFFSET_SMW * 0x20) + 0x0b,
                                         Classed.progression, "Switch Palaces"),
    item_name.unlock_switch_blue: ItemData(BASE_OFFSET + (GAME_OFFSET_SMW * 0x20) + 0x0c,
                                        Classed.progression, "Switch Palaces"),
}

autumn_koopa = {
    # Technically, since this is the only one, it doesn't strictly need an array
    item_name.unlock_autumn_koopa: ItemData(BASE_OFFSET + (GAME_OFFSET_SMW * 0x20) + 0x0e,
                                         Classed.progression, "Special Unlock"),
}

# Abilities
abilities = {
    # SMB1
    item_name.ability_dash_smb1: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB1 * 0x20) + 0x10, Classed.progression,
                                        "Dash"),
    item_name.ability_climb_smb1: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB1 * 0x20) + 0x11, Classed.progression,
                                        "Climb"),
    item_name.ability_swim_smb1: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB1 * 0x20) + 0x12, Classed.progression,
                                        "Swim"),
    item_name.ability_starman_smb1: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB1 * 0x20) + 0x14, Classed.progression,
                                        "Starman"),
    # SMBLL
    item_name.ability_dash_smbll: ItemData(BASE_OFFSET + (GAME_OFFSET_SMBLL * 0x20) + 0x10, Classed.progression,
                                        "Dash"),
    item_name.ability_climb_smbll: ItemData(BASE_OFFSET + (GAME_OFFSET_SMBLL * 0x20) + 0x11, Classed.progression,
                                        "Climb"),
    item_name.ability_swim_smbll: ItemData(BASE_OFFSET + (GAME_OFFSET_SMBLL * 0x20) + 0x12, Classed.progression,
                                        "Swim"),
    item_name.ability_starman_smbll: ItemData(BASE_OFFSET + (GAME_OFFSET_SMBLL * 0x20) + 0x14, Classed.progression,
                                        "Starman"),
    # SMB2
    item_name.ability_dash_smb2: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB2 * 0x20) + 0x10, Classed.useful,
                                        "Dash"),
    item_name.ability_climb_smb2: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB2 * 0x20) + 0x11, Classed.progression,
                                        "Climb"),
    item_name.ability_carry_smb2: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB2 * 0x20) + 0x13, Classed.progression,
                                        "Carry"),
    item_name.ability_starman_smb2: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB2 * 0x20) + 0x14, Classed.progression,
                                        "Starman"),
    item_name.ability_pswitch_smb2: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB2 * 0x20) + 0x15, Classed.useful,
                                        "P-Switch"),
    item_name.ability_special_smb2: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB2 * 0x20) + 0x17, Classed.progression,
                                        "Unique"),
    # SMB3
    item_name.ability_dash_smb3: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB3 * 0x20) + 0x10, Classed.progression,
                                        "Dash"),
    item_name.ability_climb_smb3: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB3 * 0x20) + 0x11, Classed.progression,
                                        "Climb"),
    item_name.ability_swim_smb3: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB3 * 0x20) + 0x12, Classed.progression,
                                        "Swim"),
    item_name.ability_carry_smb3: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB3 * 0x20) + 0x13, Classed.progression,
                                        "Carry"),
    item_name.ability_starman_smb3: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB3 * 0x20) + 0x14, Classed.progression,
                                        "Starman"),
    item_name.ability_pswitch_smb3: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB3 * 0x20) + 0x15, Classed.progression,
                                        "P-Switch"),
    item_name.ability_mount_smb3: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB3 * 0x20) + 0x16, Classed.progression,
                                        "Mount"),
    # SMW
    item_name.ability_dash_smw: ItemData(BASE_OFFSET + (GAME_OFFSET_SMW * 0x20) + 0x10, Classed.progression,
                                        "Dash"),
    item_name.ability_climb_smw: ItemData(BASE_OFFSET + (GAME_OFFSET_SMW * 0x20) + 0x11, Classed.progression,
                                        "Climb"),
    item_name.ability_swim_smw: ItemData(BASE_OFFSET + (GAME_OFFSET_SMW * 0x20) + 0x12, Classed.progression,
                                        "Swim"),
    item_name.ability_carry_smw: ItemData(BASE_OFFSET + (GAME_OFFSET_SMW * 0x20) + 0x13, Classed.progression,
                                        "Carry"),
    item_name.ability_starman_smw: ItemData(BASE_OFFSET + (GAME_OFFSET_SMW * 0x20) + 0x14, Classed.progression,
                                        "Starman"),
    item_name.ability_pswitch_smw: ItemData(BASE_OFFSET + (GAME_OFFSET_SMW * 0x20) + 0x15, Classed.progression,
                                        "P-Switch"),
    item_name.ability_mount_smw: ItemData(BASE_OFFSET + (GAME_OFFSET_SMW * 0x20) + 0x16, Classed.progression,
                                        "Mount"),
    item_name.ability_special_smw: ItemData(BASE_OFFSET + (GAME_OFFSET_SMW * 0x20) + 0x17, Classed.progression,
                                        "Unique"),
}

# Power-Ups
power_ups = {
    # SMB1
    item_name.powerup_mushroom_smb1: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB1 * 0x20) + 0x18, Classed.progression,
                                        "Power-Ups"),
    item_name.powerup_flower_smb1: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB1 * 0x20) + 0x19, Classed.progression,
                                        "Power-Ups"),
    item_name.powerup_prog_smb1: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB1 * 0x20) + 0x1e, Classed.progression,
                                        "Power-Ups"),
    # SMBLL
    item_name.powerup_mushroom_smbll: ItemData(BASE_OFFSET + (GAME_OFFSET_SMBLL * 0x20) + 0x18, Classed.progression,
                                        "Power-Ups"),
    item_name.powerup_flower_smbll: ItemData(BASE_OFFSET + (GAME_OFFSET_SMBLL * 0x20) + 0x19, Classed.progression,
                                        "Power-Ups"),
    item_name.powerup_prog_smbll: ItemData(BASE_OFFSET + (GAME_OFFSET_SMBLL * 0x20) + 0x1e, Classed.progression,
                                        "Power-Ups"),
    # SMB2
    item_name.powerup_prog_health_1: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB2 * 0x20) + 0x18, Classed.progression,
                                        "Power-Ups"),
    item_name.powerup_prog_health_2: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB2 * 0x20) + 0x19, Classed.progression,
                                        "Power-Ups"),
    item_name.powerup_prog_health_3: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB2 * 0x20) + 0x1a, Classed.progression,
                                        "Power-Ups"),
    item_name.powerup_prog_health_4: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB2 * 0x20) + 0x1b, Classed.progression,
                                        "Power-Ups"),
    item_name.powerup_prog_health_5: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB2 * 0x20) + 0x1c, Classed.progression,
                                        "Power-Ups"),
    item_name.powerup_prog_health_6: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB2 * 0x20) + 0x1d, Classed.progression,
                                        "Power-Ups"),
    item_name.powerup_prog_health_7: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB2 * 0x20) + 0x1e, Classed.progression,
                                        "Power-Ups"),
    item_name.powerup_prog_health_a: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB2 * 0x20) + 0x1f, Classed.progression,
                                        "Power-Ups"),
    # SMB3
    item_name.powerup_mushroom_smb3: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB3 * 0x20) + 0x18, Classed.progression,
                                        "Power-Ups"),
    item_name.powerup_flower_smb3: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB3 * 0x20) + 0x19, Classed.progression,
                                        "Power-Ups"),
    item_name.powerup_leaf: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB3 * 0x20) + 0x1a, Classed.progression,
                                        "Power-Ups"),
    item_name.powerup_frog: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB3 * 0x20) + 0x1b, Classed.progression,
                                        "Power-Ups"),
    item_name.powerup_hammer: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB3 * 0x20) + 0x1c, Classed.progression,
                                        "Power-Ups"),
    item_name.powerup_tanuki: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB3 * 0x20) + 0x1d, Classed.progression,
                                        "Power-Ups"),
    item_name.powerup_infinifly: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB3 * 0x20) + 0x1e, Classed.progression,
                                        "Power-Ups"),
    # SMW
    item_name.powerup_mushroom_smw: ItemData(BASE_OFFSET + (GAME_OFFSET_SMW * 0x20) + 0x18, Classed.progression,
                                        "Power-Ups"),
    item_name.powerup_flower_smw: ItemData(BASE_OFFSET + (GAME_OFFSET_SMW * 0x20) + 0x19, Classed.progression,
                                        "Power-Ups"),
    item_name.powerup_feather: ItemData(BASE_OFFSET + (GAME_OFFSET_SMW * 0x20) + 0x1f, Classed.progression,
                                        "Power-Ups"),
    item_name.powerup_balloon: ItemData(BASE_OFFSET + (GAME_OFFSET_SMW * 0x20) + 0x1b, Classed.progression,
                                        "Power-Ups"),
    item_name.powerup_prog_smw: ItemData(BASE_OFFSET + (GAME_OFFSET_SMW * 0x20) + 0x1e, Classed.progression,
                                        "Power-Ups"),
}

# Filler Items
fillers = {
    item_name.filler_coin_single_smb1: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB1 * 0x08) + 0xa0,
                                         Classed.filler, "Filler"),
    item_name.filler_coin_single_smbll: ItemData(BASE_OFFSET + (GAME_OFFSET_SMBLL * 0x08) + 0xa0,
                                         Classed.filler, "Filler"),
    item_name.filler_coin_single_smb2: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB2 * 0x08) + 0xa0,
                                         Classed.filler, "Filler"),
    item_name.filler_coin_single_smb3: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB3 * 0x08) + 0xa0,
                                         Classed.filler, "Filler"),
    item_name.filler_coin_single_smw: ItemData(BASE_OFFSET + (GAME_OFFSET_SMW * 0x08) + 0xa0,
                                         Classed.filler, "Filler"),
    item_name.filler_coin_five_smb1: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB1 * 0x08) + 0xa1,
                                         Classed.filler, "Filler"),
    item_name.filler_coin_five_smbll: ItemData(BASE_OFFSET + (GAME_OFFSET_SMBLL * 0x08) + 0xa1,
                                         Classed.filler, "Filler"),
    item_name.filler_coin_five_smb2: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB2 * 0x08) + 0xa1,
                                         Classed.filler, "Filler"),
    item_name.filler_coin_five_smb3: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB3 * 0x08) + 0xa1,
                                         Classed.filler, "Filler"),
    item_name.filler_coin_five_smw: ItemData(BASE_OFFSET + (GAME_OFFSET_SMW * 0x08) + 0xa1,
                                         Classed.filler, "Filler"),
    item_name.filler_coin_ten_smb1: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB1 * 0x08) + 0xa2,
                                         Classed.filler, "Filler"),
    item_name.filler_coin_ten_smbll: ItemData(BASE_OFFSET + (GAME_OFFSET_SMBLL * 0x08) + 0xa2,
                                         Classed.filler, "Filler"),
    item_name.filler_coin_ten_smb2: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB2 * 0x08) + 0xa2,
                                         Classed.filler, "Filler"),
    item_name.filler_coin_ten_smb3: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB3 * 0x08) + 0xa2,
                                         Classed.filler, "Filler"),
    item_name.filler_coin_ten_smw: ItemData(BASE_OFFSET + (GAME_OFFSET_SMW * 0x08) + 0xa2,
                                         Classed.filler, "Filler"),
    item_name.filler_coin_huge_smb1: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB1 * 0x08) + 0xa3,
                                         Classed.filler, "Filler"),
    item_name.filler_coin_huge_smbll: ItemData(BASE_OFFSET + (GAME_OFFSET_SMBLL * 0x08) + 0xa3,
                                         Classed.filler, "Filler"),
    item_name.filler_coin_huge_smb2: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB2 * 0x08) + 0xa3,
                                         Classed.filler, "Filler"),
    item_name.filler_coin_huge_smb3: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB3 * 0x08) + 0xa3,
                                         Classed.filler, "Filler"),
    item_name.filler_coin_huge_smw: ItemData(BASE_OFFSET + (GAME_OFFSET_SMW * 0x08) + 0xa3,
                                         Classed.filler, "Filler"),
    item_name.filler_mini_star_smb1: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB1 * 0x08) + 0xa5,
                                         Classed.filler, "Filler"),
    item_name.filler_mini_star_smbll: ItemData(BASE_OFFSET + (GAME_OFFSET_SMBLL * 0x08) + 0xa5,
                                         Classed.filler, "Filler"),
    item_name.filler_mini_star_smb2: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB2 * 0x08) + 0xa5,
                                         Classed.filler, "Filler"),
    item_name.filler_mini_star_smb3: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB3 * 0x08) + 0xa5,
                                         Classed.filler, "Filler"),
    item_name.filler_mini_star_smw: ItemData(BASE_OFFSET + (GAME_OFFSET_SMW * 0x08) + 0xa5,
                                         Classed.filler, "Filler"),
    item_name.filler_mini_powerup_smb1: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB1 * 0x08) + 0xa6,
                                         Classed.filler, "Filler"),
    item_name.filler_mini_powerup_smbll: ItemData(BASE_OFFSET + (GAME_OFFSET_SMBLL * 0x08) + 0xa6,
                                         Classed.filler, "Filler"),
    item_name.filler_mini_powerup_smb2: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB2 * 0x08) + 0xa6,
                                         Classed.filler, "Filler"),
    item_name.filler_mini_powerup_smb3: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB3 * 0x08) + 0xa6,
                                         Classed.filler, "Filler"),
    item_name.filler_mini_powerup_smw: ItemData(BASE_OFFSET + (GAME_OFFSET_SMW * 0x08) + 0xa6,
                                         Classed.filler, "Filler"),
    item_name.filler_extra_life_smb1: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB1 * 0x08) + 0xa7,
                                         Classed.filler, "Filler"),
    item_name.filler_extra_life_smbll: ItemData(BASE_OFFSET + (GAME_OFFSET_SMBLL * 0x08) + 0xa7,
                                         Classed.filler, "Filler"),
    item_name.filler_extra_life_smb2: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB2 * 0x08) + 0xa7,
                                         Classed.filler, "Filler"),
    item_name.filler_extra_life_smb3: ItemData(BASE_OFFSET + (GAME_OFFSET_SMB3 * 0x08) + 0xa7,
                                         Classed.filler, "Filler"),
    item_name.filler_extra_life_smw: ItemData(BASE_OFFSET + (GAME_OFFSET_SMW * 0x08) + 0xa7,
                                         Classed.filler, "Filler"),
    "Empty Item": ItemData(BASE_OFFSET + 0xe0, Classed.filler, "Filler"),
}

# All Items
all_items = {
    **world_keys,
    **egghunt,
    **char_unlocks,
    **switch_palaces,
    **autumn_koopa,
    **abilities,
    **power_ups,
    **fillers,
}

# Lookup ID to Name, not sure if needed? Just grabbed from other Worlds
lookup_id_to_name: typing.Dict[int, str] = {data.idcode: item_name for item_name, data in all_items.items() if data.idcode}

# Item Groups
item_groups = {
    # Everything from above group naming
    "Gate Keys": {name for name, data in all_items.items() if data[2] == "Gate Keys"},
    "Bonus Keys": {name for name, data in all_items.items() if data[2] == "Bonus Keys"},
    "Character Unlocks": {name for name, data in all_items.items() if data[2] == "Character Unlocks"},
    "Switch Palaces": {name for name, data in all_items.items() if data[2] == "Switch Palaces"},
    "Special Unlock": {name for name, data in all_items.items() if data[2] == "Special Unlock"},
    "Power-Ups": {name for name, data in all_items.items() if data[2] == "Power-Ups"},
    "Dash": {name for name, data in all_items.items() if data[2] == "Dash"},
    "Climb": {name for name, data in all_items.items() if data[2] == "Climb"},
    "Swim": {name for name, data in all_items.items() if data[2] == "Swim"},
    "Carry": {name for name, data in all_items.items() if data[2] == "Carry"},
    "Starman": {name for name, data in all_items.items() if data[2] == "Starman"},
    "P-Switch": {name for name, data in all_items.items() if data[2] == "P-Switch"},
    "Mount": {name for name, data in all_items.items() if data[2] == "Mount"},
    "Unique": {name for name, data in all_items.items() if data[2] == "Unique"},
    "Egghunt Eggs": {name for name, data in all_items.items() if data[2] == "Egghunt Eggs"},
    "Filler": {name for name, data in all_items.items() if data[2] == "Filler"},
    # Game Specific, #TODO: FIX, maybe as an additional data[3]
    "SMB1 Items": {name for name, data in all_items.items() if " (SMB1)" in name},
    "SMBLL Items": {name for name, data in all_items.items() if " (SMBLL)" in name},
    "SMB2 Items": {name for name, data in all_items.items() if " (SMB2)" in name},
    "SMB3 Items": {name for name, data in all_items.items() if " (SMB3)" in name},
    "SMW Items": {name for name, data in all_items.items() if " (SMW)" in name},
}

# Generation Tables
keymap_smb1_normal = [
    item_name.key_world_1_smb1,
    item_name.key_world_2_smb1,
    item_name.key_world_3_smb1,
    item_name.key_world_4_smb1,
    item_name.key_world_5_smb1,
    item_name.key_world_6_smb1,
    item_name.key_world_7_smb1,
    item_name.key_world_8_smb1,
    item_name.key_world_x1_smb1,
    item_name.key_world_x2_smb1,
    item_name.key_world_x3_smb1,
    item_name.key_world_x4_smb1,
    item_name.key_world_x5_smb1,
    item_name.key_world_x6_smb1,
    item_name.key_world_x7_smb1,
    item_name.key_world_x8_smb1,
]
keymap_smb1_dupeswap = [
    item_name.key_world_1_smb1,
    item_name.key_world_2_smb1,
    item_name.key_world_3_smb1,
    item_name.key_world_4_smb1,
    item_name.key_world_5_smb1,
    item_name.key_world_6_smb1,
    item_name.key_world_7_smb1,
    item_name.key_world_8_smb1,
    item_name.key_world_1_smb1,
    item_name.key_world_2_smb1,
    item_name.key_world_3_smb1,
    item_name.key_world_4_smb1,
    item_name.key_world_5_smb1,
    item_name.key_world_6_smb1,
    item_name.key_world_7_smb1,
    item_name.key_world_8_smb1,
]
keymap_smb1_prog = [
    item_name.key_prog_smb1,
    item_name.key_prog_smb1,
    item_name.key_prog_smb1,
    item_name.key_prog_smb1,
    item_name.key_prog_smb1,
    item_name.key_prog_smb1,
    item_name.key_prog_smb1,
    item_name.key_prog_smb1,
    item_name.key_prog_smb1,
    item_name.key_prog_smb1,
    item_name.key_prog_smb1,
    item_name.key_prog_smb1,
    item_name.key_prog_smb1,
    item_name.key_prog_smb1,
    item_name.key_prog_smb1,
    item_name.key_prog_smb1,
]

keymap_smbll_normal = [
    item_name.key_world_1_smbll,
    item_name.key_world_2_smbll,
    item_name.key_world_3_smbll,
    item_name.key_world_4_smbll,
    item_name.key_world_5_smbll,
    item_name.key_world_6_smbll,
    item_name.key_world_7_smbll,
    item_name.key_world_8_smbll,
    item_name.key_world_a_smbll,
    item_name.key_world_b_smbll,
    item_name.key_world_c_smbll,
    item_name.key_world_d_smbll,
]
keymap_smbll_prog = [
    item_name.key_prog_smbll,
    item_name.key_prog_smbll,
    item_name.key_prog_smbll,
    item_name.key_prog_smbll,
    item_name.key_prog_smbll,
    item_name.key_prog_smbll,
    item_name.key_prog_smbll,
    item_name.key_prog_smbll,
    item_name.key_prog_smbll,
    item_name.key_prog_smbll,
    item_name.key_prog_smbll,
    item_name.key_prog_smbll,
]

keymap_smb2_normal = [
    item_name.key_world_1_smb2,
    item_name.key_world_2_smb2,
    item_name.key_world_3_smb2,
    item_name.key_world_4_smb2,
    item_name.key_world_5_smb2,
    item_name.key_world_6_smb2,
    item_name.key_world_7_smb2,
]
keymap_smb2_prog = [
    item_name.key_prog_smb2,
    item_name.key_prog_smb2,
    item_name.key_prog_smb2,
    item_name.key_prog_smb2,
    item_name.key_prog_smb2,
    item_name.key_prog_smb2,
    item_name.key_prog_smb2,
]

hpmap_smb2_normal = [
    item_name.powerup_prog_health_1,
    item_name.powerup_prog_health_2,
    item_name.powerup_prog_health_3,
    item_name.powerup_prog_health_4,
    item_name.powerup_prog_health_5,
    item_name.powerup_prog_health_6,
    item_name.powerup_prog_health_7,
]
hpmap_smb2_prog = [
    item_name.powerup_prog_health_a,
    item_name.powerup_prog_health_a,
    item_name.powerup_prog_health_a,
    item_name.powerup_prog_health_a,
    item_name.powerup_prog_health_a,
    item_name.powerup_prog_health_a,
    item_name.powerup_prog_health_a,
]


keymap_smb3_normal = [
    item_name.key_world_1_smb3,
    item_name.key_world_2_smb3,
    item_name.key_world_3_smb3,
    item_name.key_world_4_smb3,
    item_name.key_world_5_smb3,
    item_name.key_world_6_smb3,
    item_name.key_world_7_smb3,
    item_name.key_world_8_smb3,
]
keymap_smb3_prog = [
    item_name.key_prog_smb3,
    item_name.key_prog_smb3,
    item_name.key_prog_smb3,
    item_name.key_prog_smb3,
    item_name.key_prog_smb3,
    item_name.key_prog_smb3,
    item_name.key_prog_smb3,
    item_name.key_prog_smb3,
]

#class SMASWItem(Item):
#    game = "Super Mario All-Stars + Super Mario World"


# TODO: Real Filler Items when coded in ASM-Side
def get_random_filler_item_name(world: SMASWWorld) -> str:
    ## APQuest base
    #if world.random.randint(0, 99) < world.options.trap_chance:
    #    return "Math Trap"
    #return "Confetti Cannon"
    return "Empty Item"


def create_item_with_correct_classification(world: SMASWWorld, name: str) -> SMASWItem:
    #data = item_table[name]
    data = all_items[name]
    # TODO: Verify it works?
    return SMASWItem(name, data.classify, data.idcode, world.player)


# With those two helper functions defined, let's now get to actually creating and submitting our itempool.
def create_all_items(world: SMASWWorld) -> None:
    # This is the function in which we will create all the items that this world submits to the multiworld item pool.
    # There must be exactly as many items as there are locations.
    # In our case, there are either six or seven locations.
    # We must make sure that when there are six locations, there are six items,
    # and when there are seven locations, there are seven items.

    # Creating items should generally be done via the world's create_item method.
    # First, we create a list containing all the items that always exist.

    itempool: list[Item] = [
    #    world.create_item("Key"),
    #    world.create_item("Sword"),
    #    world.create_item("Shield"),
    #    world.create_item("Health Upgrade"),
    #    world.create_item("Health Upgrade"),
    ]
    #starting_items: list[Item] = world.multiworld.precollected_items[world.player]

    ## Some items may only exist if the player enables certain options.
    ## In our case, If the hammer option is enabled, the sixth item is the Hammer.
    ## Otherwise, we add a filler Confetti Cannon.
    #if world.options.hammer:
    #    # Once again, it is important to stress that even though the Hammer doesn't always exist,
    #    # it must be present in the worlds item_name_to_id.
    #    # Whether it is actually in the itempool is determined purely by whether we create and add the item here.
    #    itempool.append(world.create_item("Hammer"))
    
    # Temp Value for "(Solo) Starting Game"
    valid_games = world.options.unlocked_smb1.value + world.options.unlocked_smbll.value + world.options.unlocked_smb2.value + world.options.unlocked_smb3.value + world.options.unlocked_smw.value
    
    # SMB1 Handling
    smb1_itempool: list[Item] = []
    smb1_itempool_extras: list[Item] = []

    if world.options.available_smb1.value != 0:
        # Abilities
        
        # Oldtest of precollected?
        #smb1_itempool.append(world.create_item(item_name.ability_dash_smb1)) if item_name.ability_dash_smb1 not in starting_items
        
        # TODO: Actually figure this out on a later date
        #if item_name.ability_dash_smb1 not in world.multierworld.precollected_items[world.player]:
        #    smb1_itempool.append(world.create_item(item_name.ability_dash_smb1)
        #if item_name.ability_climb_smb1 not in world.multierworld.precollected_items[world.player]:
        #    smb1_itempool.append(world.create_item(item_name.ability_climb_smb1)
        #if item_name.ability_swim_smb1 not in world.multierworld.precollected_items[world.player]:
        #    smb1_itempool.append(world.create_item(item_name.ability_swim_smb1)
        #if item_name.ability_starman_smb1 not in world.multierworld.precollected_items[world.player]:
        #    smb1_itempool.append(world.create_item(item_name.ability_starman_smb1)
        smb1_itempool.append(world.create_item(item_name.ability_dash_smb1))
        smb1_itempool.append(world.create_item(item_name.ability_climb_smb1))
        smb1_itempool.append(world.create_item(item_name.ability_swim_smb1))
        smb1_itempool.append(world.create_item(item_name.ability_starman_smb1))
        smb1_itempool_extras.append(world.create_item(item_name.ability_dash_smb1))
        smb1_itempool_extras.append(world.create_item(item_name.ability_climb_smb1))
        smb1_itempool_extras.append(world.create_item(item_name.ability_swim_smb1))
        smb1_itempool_extras.append(world.create_item(item_name.ability_starman_smb1))
        # Power-Ups
        if world.options.prog_powerups_smb1.value == 1:
            smb1_itempool.append(world.create_item(item_name.powerup_prog_smb1))
            smb1_itempool.append(world.create_item(item_name.powerup_prog_smb1))
            smb1_itempool_extras.append(world.create_item(item_name.powerup_prog_smb1))
            smb1_itempool_extras.append(world.create_item(item_name.powerup_prog_smb1))
        else:
            smb1_itempool.append(world.create_item(item_name.powerup_mushroom_smb1))
            smb1_itempool.append(world.create_item(item_name.powerup_flower_smb1))
            smb1_itempool_extras.append(world.create_item(item_name.powerup_mushroom_smb1))
            smb1_itempool_extras.append(world.create_item(item_name.powerup_flower_smb1))
        # World Keys
        if world.options.hard_worlds_smb1.value == 1:
            max_worlds_smb1 = 16
        else:
            max_worlds_smb1 = 8
        
        unlocked_game_smb1 = world.options.unlocked_smb1.value
        start_world_smb1 = world.random.randint(0, max_worlds_smb1-1)
        
        #if world.options.prog_keys_smb1:
        #    if unlocked_game_smb1 != 0:
        #        smb1_itempool.append(world.create_item(item_name.key_prog_smb1))
        #    else:
        #        world.push_precollected(world.create_item(item_name.key_prog_smb1))
        #    for i in range(max_worlds_smb1-1)
        #        smb1_itempool.append(world.create_item(item_name.key_prog_smb1))
        #else:
        #    smb1_itempool.append(world.create_item(item_name.powerup_mushroom_smb1))
        #    smb1_itempool.append(world.create_item(item_name.powerup_flower_smb1))
        for i in range(max_worlds_smb1):
            if start_world_smb1 == i and unlocked_game_smb1 != 0:
                if world.options.prog_keys_smb1.value == 1:
                    world.push_precollected(world.create_item(keymap_smb1_prog[i]))
                elif world.options.dupeswap_keys_smb1.value&1 == 1:
                    world.push_precollected(world.create_item(keymap_smb1_dupeswap[i]))
                else:
                    world.push_precollected(world.create_item(keymap_smb1_normal[i]))
            else: # Game not unlocked from start (or not starting world)
                if world.options.prog_keys_smb1.value == 1:
                    smb1_itempool.append(world.create_item(keymap_smb1_prog[i]))
                    smb1_itempool_extras.append(world.create_item(keymap_smb1_prog[i]))
                elif world.options.dupeswap_keys_smb1.value&1 == 1:
                    smb1_itempool.append(world.create_item(keymap_smb1_dupeswap[i]))
                    smb1_itempool_extras.append(world.create_item(keymap_smb1_dupeswap[i]))
                else:
                    smb1_itempool.append(world.create_item(keymap_smb1_normal[i]))
                    smb1_itempool_extras.append(world.create_item(keymap_smb1_normal[i]))
        # Easy Itempool Stuff
        temp_class = 0
        for item_this in smb1_itempool_extras:
            temp_class = world.random.randint(0,0b11111)&0b11011 # Ignore Trap Classification
            # Randomly assign a classification type, if applicable
            # This is a little bit weird due to how we manipulate the classifications
            if not item_this.advancement:
                # If our Item isn't a Prog-Item (such as SMB2's Dash or Clock),
                # turn into only Useful/Filler
                temp_class &= Classed.useful
            # Weird if-chain for weird special-cases
            if temp_class&Classed.progression == Classed.progression:
                # Ensures only Progression and its special flags.
                temp_class &= Classed.progression_deprioritized_skip_balancing
            elif temp_class&Classed.useful == Classed.useful:
                # Item is classified as Useful (Never Exclude)
                temp_class &= Classed.useful
            else:
                # Item becomes Filler
                temp_class &= Classed.filler
            item_this.classification = Classed(temp_class)
        # Finalize
        itempool.extend(smb1_itempool)
        if world.options.easy_itempool_smasw.value == 1 or world.options.easy_itempool_smb1.value == 1:
            itempool.extend(smb1_itempool_extras)

    # SMBLL Handling
    smbll_itempool: list[Item] = []
    smbll_itempool_extras: list[Item] = []

    if world.options.available_smbll.value != 0:
        # Abilities
        smbll_itempool.append(world.create_item(item_name.ability_dash_smbll))
        smbll_itempool.append(world.create_item(item_name.ability_climb_smbll))
        smbll_itempool.append(world.create_item(item_name.ability_swim_smbll))
        smbll_itempool.append(world.create_item(item_name.ability_starman_smbll))
        smbll_itempool_extras.append(world.create_item(item_name.ability_dash_smbll))
        smbll_itempool_extras.append(world.create_item(item_name.ability_climb_smbll))
        smbll_itempool_extras.append(world.create_item(item_name.ability_swim_smbll))
        smbll_itempool_extras.append(world.create_item(item_name.ability_starman_smbll))
        # Power-Ups
        if world.options.prog_powerups_smbll.value == 1:
            smbll_itempool.append(world.create_item(item_name.powerup_prog_smbll))
            smbll_itempool.append(world.create_item(item_name.powerup_prog_smbll))
            smbll_itempool_extras.append(world.create_item(item_name.powerup_prog_smbll))
            smbll_itempool_extras.append(world.create_item(item_name.powerup_prog_smbll))
        else:
            smbll_itempool.append(world.create_item(item_name.powerup_mushroom_smbll))
            smbll_itempool.append(world.create_item(item_name.powerup_flower_smbll))
            smbll_itempool_extras.append(world.create_item(item_name.powerup_mushroom_smbll))
            smbll_itempool_extras.append(world.create_item(item_name.powerup_flower_smbll))
        # World Keys
        if world.options.bonus_worlds_smbll.value == 1:
            max_worlds_smbll = 12
        else:
            max_worlds_smbll = 8
        
        unlocked_game_smbll = world.options.unlocked_smbll.value
        start_world_smbll = world.random.randint(0, max_worlds_smbll-1)
        
        for i in range(max_worlds_smbll):
            if start_world_smbll == i and unlocked_game_smbll != 0:
                if world.options.prog_keys_smbll.value == 1:
                    world.push_precollected(world.create_item(keymap_smbll_prog[i]))
                else:
                    world.push_precollected(world.create_item(keymap_smbll_normal[i]))
            else: # Game not unlocked from start (or not starting world)
                if world.options.prog_keys_smbll.value == 1:
                    smbll_itempool.append(world.create_item(keymap_smbll_prog[i]))
                    smbll_itempool_extras.append(world.create_item(keymap_smbll_prog[i]))
                else:
                    smbll_itempool.append(world.create_item(keymap_smbll_normal[i]))
                    smbll_itempool_extras.append(world.create_item(keymap_smbll_normal[i]))
        if world.options.fantasy_world_smbll.value == 1:
            smbll_itempool.append(world.create_item(item_name.key_world_fantasy))
            smbll_itempool_extras.append(world.create_item(item_name.key_world_fantasy))
        # Easy Itempool Stuff
        temp_class = 0
        for item_this in smbll_itempool_extras:
            temp_class = world.random.randint(0,0b11111)&0b11011 # Ignore Trap Classification
            # Randomly assign a classification type, if applicable
            # This is a little bit weird due to how we manipulate the classifications
            if not item_this.advancement:
                # If our Item isn't a Prog-Item (such as SMB2's Dash or Clock),
                # turn into only Useful/Filler
                temp_class &= Classed.useful
            # Weird if-chain for weird special-cases
            if temp_class&Classed.progression == Classed.progression:
                # Ensures only Progression and its special flags.
                temp_class &= Classed.progression_deprioritized_skip_balancing
            elif temp_class&Classed.useful == Classed.useful:
                # Item is classified as Useful (Never Exclude)
                temp_class &= Classed.useful
            else:
                # Item becomes Filler
                temp_class &= Classed.filler
            item_this.classification = Classed(temp_class)
        # Finalize
        itempool.extend(smbll_itempool)
        if world.options.easy_itempool_smasw.value == 1 or world.options.easy_itempool_smbll.value == 1:
            itempool.extend(smbll_itempool_extras)
    
    # SMB2 Handling
    smb2_itempool: list[Item] = []
    smb2_itempool_extras: list[Item] = []

    if world.options.available_smb2.value != 0:
        unlocked_char = 0
        unlocked_char += world.options.unlocked_mario.value
        unlocked_char += world.options.unlocked_luigi.value
        unlocked_char += world.options.unlocked_toad.value
        unlocked_char += world.options.unlocked_peach.value
        
        if not unlocked_char:
            unlocked_char = 1 # default to mario if no character auto-unlocked
        
        # Characters
        if unlocked_char&1 == 1: # Mario
            world.push_precollected(world.create_item(item_name.unlock_char_mario))
        else:
            smb2_itempool.append(world.create_item(item_name.unlock_char_mario))
            smb2_itempool_extras.append(world.create_item(item_name.unlock_char_mario))
        if unlocked_char&2 == 2: # Luigi
            world.push_precollected(world.create_item(item_name.unlock_char_luigi))
        else:
            smb2_itempool.append(world.create_item(item_name.unlock_char_luigi))
            smb2_itempool_extras.append(world.create_item(item_name.unlock_char_luigi))
        if unlocked_char&4 == 4: # Peach
            world.push_precollected(world.create_item(item_name.unlock_char_peach))
        else:
            smb2_itempool.append(world.create_item(item_name.unlock_char_peach))
            smb2_itempool_extras.append(world.create_item(item_name.unlock_char_peach))
        if unlocked_char&8 == 8: # Toad
            world.push_precollected(world.create_item(item_name.unlock_char_toad))
        else:
            smb2_itempool.append(world.create_item(item_name.unlock_char_toad))
            smb2_itempool_extras.append(world.create_item(item_name.unlock_char_toad))

        if valid_games == 4:
            #earlyitemer_smb2 = (world.random.randint(0,1) << 1) + 1
            earlyitemer_smb2 = 3
        else:
            earlyitemer_smb2 = world.random.randint(0,3)

        # Abilities
        smb2_itempool.append(world.create_item(item_name.ability_dash_smb2))
        smb2_itempool.append(world.create_item(item_name.ability_climb_smb2))
        smb2_itempool_extras.append(world.create_item(item_name.ability_dash_smb2))
        smb2_itempool_extras.append(world.create_item(item_name.ability_climb_smb2))
        if earlyitemer_smb2&2 == 2:
            world.multiworld.early_items[world.player][item_name.ability_climb_smb2] = 1
        if world.options.grab_behavior_smb2.value != 2:
            smb2_itempool.append(world.create_item(item_name.ability_carry_smb2))
            smb2_itempool_extras.append(world.create_item(item_name.ability_carry_smb2))
            if earlyitemer_smb2&1 == 1:
                world.multiworld.early_items[world.player][item_name.ability_carry_smb2] = 1
        else: # Grab Behavior is "Start With"
            world.push_precollected(world.create_item(item_name.ability_carry_smb2))
        smb2_itempool.append(world.create_item(item_name.ability_starman_smb2))
        smb2_itempool.append(world.create_item(item_name.ability_pswitch_smb2))
        smb2_itempool.append(world.create_item(item_name.ability_special_smb2))
        smb2_itempool_extras.append(world.create_item(item_name.ability_starman_smb2))
        smb2_itempool_extras.append(world.create_item(item_name.ability_pswitch_smb2))
        smb2_itempool_extras.append(world.create_item(item_name.ability_special_smb2))
        # Health
        max_hearts = world.options.max_health_smb2.value
        start_hearts = world.options.start_health_smb2.value
        pool_hearts = max_hearts - start_hearts
        
        for i in range(7): # Create appropriate health upgrades per world count
            for j in range(pool_hearts):
                if world.options.prog_health_smb2.value == 1:
                    smb2_itempool.append(world.create_item(hpmap_smb2_prog[i]))
                else:
                    smb2_itempool.append(world.create_item(hpmap_smb2_normal[i]))
            # Create one extra Health Upgrade per World, for Easy Itempools
            if world.options.prog_health_smb2.value == 1:
                smb2_itempool_extras.append(world.create_item(hpmap_smb2_prog[i]))
            else:
                smb2_itempool_extras.append(world.create_item(hpmap_smb2_normal[i]))
        
        # World Keys
        unlocked_game_smb2 = world.options.unlocked_smb2.value
        start_world_smb2 = world.random.randint(0, 6)
        
        for i in range(7):
            if start_world_smb2 == i and unlocked_game_smb2 != 0:
                if world.options.prog_keys_smb2.value == 1:
                    world.push_precollected(world.create_item(keymap_smb2_prog[i]))
                else:
                    world.push_precollected(world.create_item(keymap_smb2_normal[i]))
            else: # Game not unlocked from start (or not starting world)
                if world.options.prog_keys_smb2.value == 1:
                    smb2_itempool.append(world.create_item(keymap_smb2_prog[i]))
                    smb2_itempool_extras.append(world.create_item(keymap_smb2_prog[i]))
                else:
                    smb2_itempool.append(world.create_item(keymap_smb2_normal[i]))
                    smb2_itempool_extras.append(world.create_item(keymap_smb2_normal[i]))
        # Easy Itempool Stuff
        temp_class = 0
        for item_this in smb2_itempool_extras:
            temp_class = world.random.randint(0,0b11111)&0b11011 # Ignore Trap Classification
            # Randomly assign a classification type, if applicable
            # This is a little bit weird due to how we manipulate the classifications
            if not item_this.advancement:
                # If our Item isn't a Prog-Item (such as SMB2's Dash or Clock),
                # turn into only Useful/Filler
                temp_class &= Classed.useful
            # Weird if-chain for weird special-cases
            if temp_class&Classed.progression == Classed.progression:
                # Ensures only Progression and its special flags.
                temp_class &= Classed.progression_deprioritized_skip_balancing
            elif temp_class&Classed.useful == Classed.useful:
                # Item is classified as Useful (Never Exclude)
                temp_class &= Classed.useful
            else:
                # Item becomes Filler
                temp_class &= Classed.filler
            item_this.classification = Classed(temp_class)
        # Finalize
        itempool.extend(smb2_itempool)
        if world.options.easy_itempool_smasw.value == 1 or world.options.easy_itempool_smb2.value == 1:
            itempool.extend(smb2_itempool_extras)
    
    # SMB3 Handling
    smb3_itempool: list[Item] = []
    smb3_itempool_extras: list[Item] = []

    if world.options.available_smb3.value != 0:
        # Abilities
        smb3_itempool.append(world.create_item(item_name.ability_dash_smb3))
        smb3_itempool.append(world.create_item(item_name.ability_climb_smb3))
        smb3_itempool.append(world.create_item(item_name.ability_swim_smb3))
        smb3_itempool.append(world.create_item(item_name.ability_carry_smb3))
        smb3_itempool.append(world.create_item(item_name.ability_starman_smb3))
        smb3_itempool.append(world.create_item(item_name.ability_pswitch_smb3))
        smb3_itempool.append(world.create_item(item_name.ability_mount_smb3))
        # Abilities, Easy Itempool
        smb3_itempool_extras.append(world.create_item(item_name.ability_dash_smb3))
        smb3_itempool_extras.append(world.create_item(item_name.ability_climb_smb3))
        smb3_itempool_extras.append(world.create_item(item_name.ability_swim_smb3))
        smb3_itempool_extras.append(world.create_item(item_name.ability_carry_smb3))
        smb3_itempool_extras.append(world.create_item(item_name.ability_starman_smb3))
        smb3_itempool_extras.append(world.create_item(item_name.ability_pswitch_smb3))
        smb3_itempool_extras.append(world.create_item(item_name.ability_mount_smb3))
        # Power-Ups
        smb3_itempool.append(world.create_item(item_name.powerup_mushroom_smb3))
        smb3_itempool.append(world.create_item(item_name.powerup_flower_smb3))
        smb3_itempool.append(world.create_item(item_name.powerup_leaf))
        smb3_itempool.append(world.create_item(item_name.powerup_frog))
        smb3_itempool.append(world.create_item(item_name.powerup_hammer))
        smb3_itempool.append(world.create_item(item_name.powerup_tanuki))
        smb3_itempool.append(world.create_item(item_name.powerup_infinifly))
        # Power-Ups, Easy Itempool
        smb3_itempool_extras.append(world.create_item(item_name.powerup_mushroom_smb3))
        smb3_itempool_extras.append(world.create_item(item_name.powerup_flower_smb3))
        smb3_itempool_extras.append(world.create_item(item_name.powerup_leaf))
        smb3_itempool_extras.append(world.create_item(item_name.powerup_frog))
        smb3_itempool_extras.append(world.create_item(item_name.powerup_hammer))
        smb3_itempool_extras.append(world.create_item(item_name.powerup_tanuki))
        smb3_itempool_extras.append(world.create_item(item_name.powerup_infinifly))
        # World Keys
        unlocked_game_smb3 = world.options.unlocked_smb3.value
        start_world_smb3 = world.random.randint(0, 7)
        
        # Reroll if we land on World 3, but SMB3 is our only Starting Game.
        # This is due to the W3-1 being a Water Level, when the Player does not have Swim.
        # TODO: Rework for Level Shuffle and Starting Abilities/Power-Ups
        if valid_games == 8:
            start_world_smb3 = world.random.randint(0, 6)
            if start_world_smb3 >= 2: # Bump up the World Number (skips W3)
                start_world_smb3+=1
        
        for i in range(8):
            if start_world_smb3 == i and unlocked_game_smb3 != 0:
                if world.options.prog_keys_smb3.value == 1:
                    world.push_precollected(world.create_item(keymap_smb3_prog[i]))
                else:
                    world.push_precollected(world.create_item(keymap_smb3_normal[i]))
            else: # Game not unlocked from start (or not starting world)
                if world.options.prog_keys_smb3.value == 1:
                    smb3_itempool.append(world.create_item(keymap_smb3_prog[i]))
                    smb3_itempool_extras.append(world.create_item(keymap_smb3_prog[i]))
                else:
                    smb3_itempool.append(world.create_item(keymap_smb3_normal[i]))
                    smb3_itempool_extras.append(world.create_item(keymap_smb3_normal[i]))
        # Easy Itempool Stuff
        temp_class = 0
        for item_this in smb3_itempool_extras:
            temp_class = world.random.randint(0,0b11111)&0b11011 # Ignore Trap Classification
            # Randomly assign a classification type, if applicable
            # This is a little bit weird due to how we manipulate the classifications
            if not item_this.advancement:
                # If our Item isn't a Prog-Item (such as SMB2's Dash or Clock),
                # turn into only Useful/Filler
                temp_class &= Classed.useful
            # Weird if-chain for weird special-cases
            if temp_class&Classed.progression == Classed.progression:
                # Ensures only Progression and its special flags.
                temp_class &= Classed.progression_deprioritized_skip_balancing
            elif temp_class&Classed.useful == Classed.useful:
                # Item is classified as Useful (Never Exclude)
                temp_class &= Classed.useful
            else:
                # Item becomes Filler
                temp_class &= Classed.filler
            item_this.classification = Classed(temp_class)
        # Finalize
        itempool.extend(smb3_itempool)
        if world.options.easy_itempool_smasw.value == 1 or world.options.easy_itempool_smb3.value == 1:
            itempool.extend(smb3_itempool_extras)

    # Refer to APQuest stuff
    number_of_items = len(itempool)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items
    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]
    world.multiworld.itempool += itempool

