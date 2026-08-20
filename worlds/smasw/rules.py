from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.options import OptionFilter
from rule_builder.rules import Has, HasFromList, HasAll, HasFromListUnique, Rule, HasAny

from .options import DupeswapKeysSmb1, GrabBehaviorSmb2, RequireSmb1, RequireSmbll, RequireSmb2, RequireSmb3, GoalCount, \
    GoalSmb1, GoalSmbll, BosscoinSmb1, BosscoinSmbll, BosscoinSmb2, BosscoinSmb3

from .names import item_name, location_name

if TYPE_CHECKING:
    from .world import SMASWWorld


# Various Rule-Related Stuff based on weirdo options
# World Keys
can_enter_w1_smb1 = Has(item_name.key_world_1_smb1) | Has(item_name.key_world_x1_smb1, options=[OptionFilter(DupeswapKeysSmb1, 0, operator="ne")], count=2) | Has(item_name.key_prog_smb1, 1)
can_enter_w2_smb1 = Has(item_name.key_world_2_smb1) | Has(item_name.key_world_x2_smb1, options=[OptionFilter(DupeswapKeysSmb1, 0, operator="ne")], count=2) | Has(item_name.key_prog_smb1, 2)
can_enter_w3_smb1 = Has(item_name.key_world_3_smb1) | Has(item_name.key_world_x3_smb1, options=[OptionFilter(DupeswapKeysSmb1, 0, operator="ne")], count=2) | Has(item_name.key_prog_smb1, 3)
can_enter_w4_smb1 = Has(item_name.key_world_4_smb1) | Has(item_name.key_world_x4_smb1, options=[OptionFilter(DupeswapKeysSmb1, 0, operator="ne")], count=2) | Has(item_name.key_prog_smb1, 4)
can_enter_w5_smb1 = Has(item_name.key_world_5_smb1) | Has(item_name.key_world_x5_smb1, options=[OptionFilter(DupeswapKeysSmb1, 0, operator="ne")], count=2) | Has(item_name.key_prog_smb1, 5)
can_enter_w6_smb1 = Has(item_name.key_world_6_smb1) | Has(item_name.key_world_x6_smb1, options=[OptionFilter(DupeswapKeysSmb1, 0, operator="ne")], count=2) | Has(item_name.key_prog_smb1, 6)
can_enter_w7_smb1 = Has(item_name.key_world_7_smb1) | Has(item_name.key_world_x7_smb1, options=[OptionFilter(DupeswapKeysSmb1, 0, operator="ne")], count=2) | Has(item_name.key_prog_smb1, 7)
can_enter_w8_smb1 = Has(item_name.key_world_8_smb1) | Has(item_name.key_world_x8_smb1, options=[OptionFilter(DupeswapKeysSmb1, 0, operator="ne")], count=2) | Has(item_name.key_prog_smb1, 8)
can_enter_x1_smb1 = Has(item_name.key_world_x1_smb1) | Has(item_name.key_world_1_smb1, options=[OptionFilter(DupeswapKeysSmb1, 0, operator="ne")], count=2) | Has(item_name.key_prog_smb1, 9)
can_enter_x2_smb1 = Has(item_name.key_world_x2_smb1) | Has(item_name.key_world_2_smb1, options=[OptionFilter(DupeswapKeysSmb1, 0, operator="ne")], count=2) | Has(item_name.key_prog_smb1, 10)
can_enter_x3_smb1 = Has(item_name.key_world_x3_smb1) | Has(item_name.key_world_3_smb1, options=[OptionFilter(DupeswapKeysSmb1, 0, operator="ne")], count=2) | Has(item_name.key_prog_smb1, 11)
can_enter_x4_smb1 = Has(item_name.key_world_x4_smb1) | Has(item_name.key_world_4_smb1, options=[OptionFilter(DupeswapKeysSmb1, 0, operator="ne")], count=2) | Has(item_name.key_prog_smb1, 12)
can_enter_x5_smb1 = Has(item_name.key_world_x5_smb1) | Has(item_name.key_world_5_smb1, options=[OptionFilter(DupeswapKeysSmb1, 0, operator="ne")], count=2) | Has(item_name.key_prog_smb1, 13)
can_enter_x6_smb1 = Has(item_name.key_world_x6_smb1) | Has(item_name.key_world_6_smb1, options=[OptionFilter(DupeswapKeysSmb1, 0, operator="ne")], count=2) | Has(item_name.key_prog_smb1, 14)
can_enter_x7_smb1 = Has(item_name.key_world_x7_smb1) | Has(item_name.key_world_7_smb1, options=[OptionFilter(DupeswapKeysSmb1, 0, operator="ne")], count=2) | Has(item_name.key_prog_smb1, 15)
can_enter_x8_smb1 = Has(item_name.key_world_x8_smb1) | Has(item_name.key_world_8_smb1, options=[OptionFilter(DupeswapKeysSmb1, 0, operator="ne")], count=2) | Has(item_name.key_prog_smb1, 16)
can_enter_w1_smbll = Has(item_name.key_world_1_smbll) | Has(item_name.key_prog_smbll, 1)
can_enter_w2_smbll = Has(item_name.key_world_2_smbll) | Has(item_name.key_prog_smbll, 2)
can_enter_w3_smbll = Has(item_name.key_world_3_smbll) | Has(item_name.key_prog_smbll, 3)
can_enter_w4_smbll = Has(item_name.key_world_4_smbll) | Has(item_name.key_prog_smbll, 4)
can_enter_w5_smbll = Has(item_name.key_world_5_smbll) | Has(item_name.key_prog_smbll, 5)
can_enter_w6_smbll = Has(item_name.key_world_6_smbll) | Has(item_name.key_prog_smbll, 6)
can_enter_w7_smbll = Has(item_name.key_world_7_smbll) | Has(item_name.key_prog_smbll, 7)
can_enter_w8_smbll = Has(item_name.key_world_8_smbll) | Has(item_name.key_prog_smbll, 8)
can_enter_wa_smbll = Has(item_name.key_world_a_smbll) | Has(item_name.key_prog_smbll, 9)
can_enter_wb_smbll = Has(item_name.key_world_b_smbll) | Has(item_name.key_prog_smbll, 10)
can_enter_wc_smbll = Has(item_name.key_world_c_smbll) | Has(item_name.key_prog_smbll, 11)
can_enter_wd_smbll = Has(item_name.key_world_d_smbll) | Has(item_name.key_prog_smbll, 12)
can_enter_w9_smbll = Has(item_name.key_world_fantasy)
can_enter_w1_smb2 = Has(item_name.key_world_1_smb2) | Has(item_name.key_prog_smb2, 1)
can_enter_w2_smb2 = Has(item_name.key_world_2_smb2) | Has(item_name.key_prog_smb2, 2)
can_enter_w3_smb2 = Has(item_name.key_world_3_smb2) | Has(item_name.key_prog_smb2, 3)
can_enter_w4_smb2 = Has(item_name.key_world_4_smb2) | Has(item_name.key_prog_smb2, 4)
can_enter_w5_smb2 = Has(item_name.key_world_5_smb2) | Has(item_name.key_prog_smb2, 5)
can_enter_w6_smb2 = Has(item_name.key_world_6_smb2) | Has(item_name.key_prog_smb2, 6)
can_enter_w7_smb2 = Has(item_name.key_world_7_smb2) | Has(item_name.key_prog_smb2, 7)
can_enter_w1_smb3 = Has(item_name.key_world_1_smb3) | Has(item_name.key_prog_smb3, 1)
can_enter_w2_smb3 = Has(item_name.key_world_2_smb3) | Has(item_name.key_prog_smb3, 2)
can_enter_w3_smb3 = Has(item_name.key_world_3_smb3) | Has(item_name.key_prog_smb3, 3)
can_enter_w4_smb3 = Has(item_name.key_world_4_smb3) | Has(item_name.key_prog_smb3, 4)
can_enter_w5_smb3 = Has(item_name.key_world_5_smb3) | Has(item_name.key_prog_smb3, 5)
can_enter_w6_smb3 = Has(item_name.key_world_6_smb3) | Has(item_name.key_prog_smb3, 6)
can_enter_w7_smb3 = Has(item_name.key_world_7_smb3) | Has(item_name.key_prog_smb3, 7)
can_enter_w8_smb3 = Has(item_name.key_world_8_smb3) | Has(item_name.key_prog_smb3, 8)
# Power-Ups
has_mushroom_smb1 = Has(item_name.powerup_mushroom_smb1) | Has(item_name.powerup_prog_smb1, 1)
has_mushroom_smbll = Has(item_name.powerup_mushroom_smbll) | Has(item_name.powerup_prog_smbll, 1)
has_mushroom_smb3 = Has(item_name.powerup_mushroom_smb3)
has_flower_smb1 = HasAll(item_name.powerup_flower_smb1, item_name.powerup_mushroom_smb1) | Has(item_name.powerup_prog_smb1, 2)
has_flower_smbll = HasAll(item_name.powerup_flower_smbll, item_name.powerup_mushroom_smbll) | Has(item_name.powerup_prog_smbll, 2)
has_flower_smb3 = Has(item_name.powerup_flower_smb3)
has_leaf_smb3 = Has(item_name.powerup_leaf)
has_frog_smb3 = Has(item_name.powerup_frog)
has_hammer_smb3 = Has(item_name.powerup_hammer) # Hammer Suit
has_tanuki_smb3 = Has(item_name.powerup_tanuki)
has_pwing_smb3 = Has(item_name.powerup_infinifly) & has_leaf_smb3 # TODO: Alternate P-Wing Power Options
has_flight_smb3 = has_leaf_smb3 | has_tanuki_smb3
# SMB2 Health stuff
# TODO: Properly calculate the "Global Progressive" Health of Variable Maximums
has_w1_2hp = Has(item_name.powerup_prog_health_1, 1) | Has(item_name.powerup_prog_health_a, 1)
has_w1_3hp = Has(item_name.powerup_prog_health_1, 2) | Has(item_name.powerup_prog_health_a, 2)
has_w1_4hp = Has(item_name.powerup_prog_health_1, 3) | Has(item_name.powerup_prog_health_a, 3)
has_w2_2hp = Has(item_name.powerup_prog_health_2, 1) | Has(item_name.powerup_prog_health_a, 4)
has_w2_3hp = Has(item_name.powerup_prog_health_2, 2) | Has(item_name.powerup_prog_health_a, 5)
has_w2_4hp = Has(item_name.powerup_prog_health_2, 3) | Has(item_name.powerup_prog_health_a, 6)
has_w3_2hp = Has(item_name.powerup_prog_health_3, 1) | Has(item_name.powerup_prog_health_a, 7)
has_w3_3hp = Has(item_name.powerup_prog_health_3, 2) | Has(item_name.powerup_prog_health_a, 8)
has_w3_4hp = Has(item_name.powerup_prog_health_3, 3) | Has(item_name.powerup_prog_health_a, 9)
has_w4_2hp = Has(item_name.powerup_prog_health_4, 1) | Has(item_name.powerup_prog_health_a, 10)
has_w4_3hp = Has(item_name.powerup_prog_health_4, 2) | Has(item_name.powerup_prog_health_a, 11)
has_w4_4hp = Has(item_name.powerup_prog_health_4, 3) | Has(item_name.powerup_prog_health_a, 12)
has_w5_2hp = Has(item_name.powerup_prog_health_5, 1) | Has(item_name.powerup_prog_health_a, 13)
has_w5_3hp = Has(item_name.powerup_prog_health_5, 2) | Has(item_name.powerup_prog_health_a, 14)
has_w5_4hp = Has(item_name.powerup_prog_health_5, 3) | Has(item_name.powerup_prog_health_a, 15)
has_w6_2hp = Has(item_name.powerup_prog_health_6, 1) | Has(item_name.powerup_prog_health_a, 16)
has_w6_3hp = Has(item_name.powerup_prog_health_6, 2) | Has(item_name.powerup_prog_health_a, 17)
has_w6_4hp = Has(item_name.powerup_prog_health_6, 3) | Has(item_name.powerup_prog_health_a, 18)
has_w7_2hp = Has(item_name.powerup_prog_health_7, 1) | Has(item_name.powerup_prog_health_a, 19)
has_w7_3hp = Has(item_name.powerup_prog_health_7, 2) | Has(item_name.powerup_prog_health_a, 20)
has_w7_4hp = Has(item_name.powerup_prog_health_7, 3) | Has(item_name.powerup_prog_health_a, 21)

# Handle Certain Composite Rules
can_subspace_mushroom = HasAll(item_name.ability_special_smb2, item_name.ability_carry_smb2)
can_basic_grab_smb2 = Has(item_name.ability_carry_smb2, options=[OptionFilter(GrabBehaviorSmb2, 1, operator="ge")], filtered_resolution=True)
can_swim_smb3 = has_frog_smb3 | Has(item_name.ability_swim_smb3)
has_takeoff_smb3 = Has(item_name.ability_dash_smb3) | has_pwing_smb3
can_fly_smb3 = has_takeoff_smb3 & has_flight_smb3
# TODO: SMB3 Power-Up Inventory Shenanigans


# Custom Rules (some because "field resolvers" don't currently exist
# This is used for Boss Coins, grabebd from Oracle of Seasons
class HasOption(Has, game="Super Mario All-Stars + Super Mario World"):
    option_name: str

    def __init__(self, item_name_t: str, option_name: str):
        self.option_name = option_name
        super().__init__(item_name_t)

    def _instantiate(self, world: SMASWWorld) -> Rule.Resolved:
        self.count = getattr(world.options, self.option_name).value
        return super()._instantiate(world)

# This is used for Counted Subgoals, half-grabbed from Oracle of Seasons
class HasFromListOption(HasFromListUnique, game="Super Mario All-Stars + Super Mario World"):
    option_name: str

    def __init__(self, *item_names: str, option_name: str):
        self.option_name = option_name
        super().__init__(*item_names)

    def _instantiate(self, world: SMASWWorld) -> Rule.Resolved:
        self.count = getattr(world.options, self.option_name).value
        return super()._instantiate(world)

# TODO: Health Logic for SMB2


def set_all_rules(world: SMASWWorld) -> None:
    # In order for AP to generate an item layout that is actually possible for the player to complete,
    # we need to define rules for our Entrances and Locations.
    # Note: Regions do not have rules, the Entrances connecting them do!
    # We'll do entrances first, then locations, and then finally we set our victory condition.

    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)


def set_all_entrance_rules(world: SMASWWorld) -> None:
    ## First, we need to actually grab our entrances. Luckily, there is a helper method for this.
    #overworld_to_bottom_right_room = world.get_entrance("Overworld to Bottom Right Room")
    #overworld_to_top_left_room = world.get_entrance("Overworld to Top Left Room")
    #right_room_to_final_boss_room = world.get_entrance("Right Room to Final Boss Room")


    
    
    ## Handle Option Checking of requirements
    #opt_req_smb1 = OptionFilter(AvailableSmb1, AvailableSmb1.option_required) | OptionFilter(RequireSmb1, RequireSmb1.option_require)
    #opt_req_smbll = OptionFilter(AvailableSmbll, AvailableSmbll.option_required) | OptionFilter(RequireSmbll, RequireSmbll.option_require)
    #opt_req_smb2 = OptionFilter(AvailableSmb2, AvailableSmb2.option_required) | OptionFilter(RequireSmb2, RequireSmb2.option_require)
    #opt_req_smb3 = OptionFilter(AvailableSmb3, AvailableSmb3.option_required) | OptionFilter(RequireSmb3, RequireSmb3.option_require)
    
    
    # Handle Required Goal, gets resolved to True if option is not set (so entrances can still work)
    require_smb1 = Has(item_name.goal_smb1, options=[OptionFilter(RequireSmb1, RequireSmb1.option_require)], filtered_resolution=True)
    require_smbll = Has(item_name.goal_smbll, options=[OptionFilter(RequireSmbll, RequireSmbll.option_require)], filtered_resolution=True)
    require_smb2 = Has(item_name.goal_smb2, options=[OptionFilter(RequireSmb2, RequireSmb2.option_require)], filtered_resolution=True)
    require_smb3 = Has(item_name.goal_smb3, options=[OptionFilter(RequireSmb3, RequireSmb3.option_require)], filtered_resolution=True)
    required_games = require_smb1 & require_smbll & require_smb2 & require_smb3
    
    # Apply to entrance
    smasw_req_goals = world.get_entrance("Check Required SubGoals")
    world.set_rule(smasw_req_goals, required_games)
    
    # Handle "Number of Games Completed" SMASW Goal
    #goal_count = world.option.goal_smasw_count.value
    goals = []
    if world.options.available_smb1.value != 0:
        goals.append(item_name.goal_smb1)
    if world.options.available_smbll.value != 0:
        goals.append(item_name.goal_smbll)
    if world.options.available_smb2.value != 0:
        goals.append(item_name.goal_smb2)
    if world.options.available_smb3.value != 0:
        goals.append(item_name.goal_smb3)
    #if world.options.available_smw != 0:
    #    goals.append(item_name.goal_smw)
    goaled_games = HasFromListOption(*tuple(goals), option_name="goal_smasw_count")
    
    # Apply to entrance
    smasw_goals = world.get_entrance("Checking All SubGoals")
    world.set_rule(smasw_goals, goaled_games)
    
    # BossCoin-related stuff (partial subgoals for SMB1/SMBLL are handled later)
    free_8_4_smb1 = OptionFilter(GoalSmb1, GoalSmb1.option_true_bowser)
    free_8x4_smb1 = OptionFilter(GoalSmb1, GoalSmb1.option_final_bowser)
    free_8_4_smbll = OptionFilter(GoalSmbll, GoalSmbll.option_true_bowser)
    free_d_4_smbll = OptionFilter(GoalSmbll, GoalSmbll.option_final_bowser)
    
    has_bosscoins_smb1 = HasOption(item_name.bosscoin_smb1, "bosscoin_smb1")
    has_bosscoins_smbll = HasOption(item_name.bosscoin_smbll, "bosscoin_smbll")
    has_bosscoins_smb2 = HasOption(item_name.bosscoin_smb2, "bosscoin_smb2")
    has_bosscoins_smb3 = HasOption(item_name.bosscoin_smb3, "bosscoin_smb3")
    
    # Consolidate the above rules
    #enter_8_4_smb1 = free_8_4_smb1 | has_bosscoins_smb1
    #enter_8x4_smb1 = free_8x4_smb1 | has_bosscoins_smb1
    #enter_8_4_smbll = free_8_4_smbll | has_bosscoins_smbll
    #enter_d_4_smbll = free_d_4_smbll | has_bosscoins_smbll
    enter_8_4_smb1 = has_bosscoins_smb1
    enter_8x4_smb1 = has_bosscoins_smb1
    enter_8_4_smbll = has_bosscoins_smbll
    enter_d_4_smbll = has_bosscoins_smbll
    enter_7_2_smb2 = has_bosscoins_smb2
    enter_final_smb3 = has_bosscoins_smb3
    
    # Apply To Entrances, If Applicable
    if world.options.available_smb1.value != 0:
        ent_8_4_smb1 = world.get_entrance("World 8-4 Tile (SMB1) -> Level 8-4 (SMB1)")
        if world.options.goal_smb1.value == GoalSmb1.option_true_bowser:
            world.set_rule(ent_8_4_smb1, HasAll(item_name.ability_dash_smb1,item_name.ability_swim_smb1))
        else:
            world.set_rule(ent_8_4_smb1, enter_8_4_smb1 & HasAll(item_name.ability_dash_smb1,item_name.ability_swim_smb1))
        if world.options.hard_worlds_smb1.value != 0:
            ent_8x4_smb1  = world.get_entrance("World 8x4 Tile (SMB1) -> Level 8x4 (SMB1)")
            if world.options.goal_smb1.value == GoalSmb1.option_final_bowser:
                world.set_rule(ent_8x4_smb1, HasAll(item_name.ability_dash_smb1,item_name.ability_swim_smb1))
            else:
                world.set_rule(ent_8x4_smb1, enter_8x4_smb1 & HasAll(item_name.ability_dash_smb1,item_name.ability_swim_smb1))
    if world.options.available_smbll.value != 0:
        ent_8_4_smbll = world.get_entrance("World 8-4 Tile (SMBLL) -> Level 8-4 (SMBLL)")
        if world.options.goal_smbll.value == GoalSmbll.option_true_bowser:
            world.set_rule(ent_8_4_smbll, HasAll(item_name.ability_dash_smbll,item_name.ability_swim_smbll))
        else:
            world.set_rule(ent_8_4_smbll, enter_8_4_smbll & HasAll(item_name.ability_dash_smbll,item_name.ability_swim_smbll))
        if world.options.bonus_worlds_smbll.value != 0:
            ent_d_4_smbll  = world.get_entrance("World D-4 Tile (SMBLL) -> Level D-4 (SMBLL)")
            if world.options.goal_smbll.value == GoalSmbll.option_final_bowser:
                world.set_rule(ent_d_4_smbll, Has(item_name.ability_dash_smbll))
            else:
                world.set_rule(ent_d_4_smbll, enter_d_4_smbll & Has(item_name.ability_dash_smbll))
    if world.options.available_smb2.value != 0: #TODO: Health Logic
        ent_7_2_smb2 = world.get_entrance("World 7-2 Tile (SMB2) -> Level 7-2 (SMB2)")
        world.set_rule(ent_7_2_smb2, enter_7_2_smb2 & HasAll(item_name.ability_carry_smb2,item_name.ability_climb_smb2))
    if world.options.available_smb3.value != 0:
        ent_final_smb3 = world.get_entrance("World 8-Castle Tile (SMB3) -> Level 8-Castle (SMB3)")
        world.set_rule(ent_final_smb3, enter_final_smb3)
    
    # Apply World Keys for World Access
    if world.options.available_smb1.value != 0:
        ent_w1_smb1 = world.get_entrance("SMB1 Game -> World 1 (SMB1)")
        world.set_rule(ent_w1_smb1, can_enter_w1_smb1)
        ent_w2_smb1 = world.get_entrance("SMB1 Game -> World 2 (SMB1)")
        world.set_rule(ent_w2_smb1, can_enter_w2_smb1)
        ent_w3_smb1 = world.get_entrance("SMB1 Game -> World 3 (SMB1)")
        world.set_rule(ent_w3_smb1, can_enter_w3_smb1)
        ent_w4_smb1 = world.get_entrance("SMB1 Game -> World 4 (SMB1)")
        world.set_rule(ent_w4_smb1, can_enter_w4_smb1)
        ent_w5_smb1 = world.get_entrance("SMB1 Game -> World 5 (SMB1)")
        world.set_rule(ent_w5_smb1, can_enter_w5_smb1)
        ent_w6_smb1 = world.get_entrance("SMB1 Game -> World 6 (SMB1)")
        world.set_rule(ent_w6_smb1, can_enter_w6_smb1)
        ent_w7_smb1 = world.get_entrance("SMB1 Game -> World 7 (SMB1)")
        world.set_rule(ent_w7_smb1, can_enter_w7_smb1)
        ent_w8_smb1 = world.get_entrance("SMB1 Game -> World 8 (SMB1)")
        world.set_rule(ent_w8_smb1, can_enter_w8_smb1)
        if world.options.hard_worlds_smb1.value != 0:
            ent_x1_smb1 = world.get_entrance("SMB1 Game -> World X1 (SMB1)")
            world.set_rule(ent_x1_smb1, can_enter_x1_smb1)
            ent_x2_smb1 = world.get_entrance("SMB1 Game -> World X2 (SMB1)")
            world.set_rule(ent_x2_smb1, can_enter_x2_smb1)
            ent_x3_smb1 = world.get_entrance("SMB1 Game -> World X3 (SMB1)")
            world.set_rule(ent_x3_smb1, can_enter_x3_smb1)
            ent_x4_smb1 = world.get_entrance("SMB1 Game -> World X4 (SMB1)")
            world.set_rule(ent_x4_smb1, can_enter_x4_smb1)
            ent_x5_smb1 = world.get_entrance("SMB1 Game -> World X5 (SMB1)")
            world.set_rule(ent_x5_smb1, can_enter_x5_smb1)
            ent_x6_smb1 = world.get_entrance("SMB1 Game -> World X6 (SMB1)")
            world.set_rule(ent_x6_smb1, can_enter_x6_smb1)
            ent_x7_smb1 = world.get_entrance("SMB1 Game -> World X7 (SMB1)")
            world.set_rule(ent_x7_smb1, can_enter_x7_smb1)
            ent_x8_smb1 = world.get_entrance("SMB1 Game -> World X8 (SMB1)")
            world.set_rule(ent_x8_smb1, can_enter_x8_smb1)
    if world.options.available_smbll.value != 0:
        ent_w1_smbll = world.get_entrance("SMBLL Game -> World 1 (SMBLL)")
        world.set_rule(ent_w1_smbll, can_enter_w1_smbll)
        ent_w2_smbll = world.get_entrance("SMBLL Game -> World 2 (SMBLL)")
        world.set_rule(ent_w2_smbll, can_enter_w2_smbll)
        ent_w3_smbll = world.get_entrance("SMBLL Game -> World 3 (SMBLL)")
        world.set_rule(ent_w3_smbll, can_enter_w3_smbll)
        ent_w4_smbll = world.get_entrance("SMBLL Game -> World 4 (SMBLL)")
        world.set_rule(ent_w4_smbll, can_enter_w4_smbll)
        ent_w5_smbll = world.get_entrance("SMBLL Game -> World 5 (SMBLL)")
        world.set_rule(ent_w5_smbll, can_enter_w5_smbll)
        ent_w6_smbll = world.get_entrance("SMBLL Game -> World 6 (SMBLL)")
        world.set_rule(ent_w6_smbll, can_enter_w6_smbll)
        ent_w7_smbll = world.get_entrance("SMBLL Game -> World 7 (SMBLL)")
        world.set_rule(ent_w7_smbll, can_enter_w7_smbll)
        ent_w8_smbll = world.get_entrance("SMBLL Game -> World 8 (SMBLL)")
        world.set_rule(ent_w8_smbll, can_enter_w8_smbll)
        if world.options.fantasy_world_smbll.value != 0:
            ent_w9_smbll = world.get_entrance("SMBLL Game -> World 9 (SMBLL)")
            world.set_rule(ent_w9_smbll, can_enter_w9_smbll)
        if world.options.bonus_worlds_smbll.value != 0:
            ent_wa_smbll = world.get_entrance("SMBLL Game -> World A (SMBLL)")
            world.set_rule(ent_wa_smbll, can_enter_wa_smbll)
            ent_wb_smbll = world.get_entrance("SMBLL Game -> World B (SMBLL)")
            world.set_rule(ent_wb_smbll, can_enter_wb_smbll)
            ent_wc_smbll = world.get_entrance("SMBLL Game -> World C (SMBLL)")
            world.set_rule(ent_wc_smbll, can_enter_wc_smbll)
            ent_wd_smbll = world.get_entrance("SMBLL Game -> World D (SMBLL)")
            world.set_rule(ent_wd_smbll, can_enter_wd_smbll)
    if world.options.available_smb2.value != 0:
        ent_w1_smb2 = world.get_entrance("SMB2 Game -> World 1 (SMB2)")
        world.set_rule(ent_w1_smb2, can_enter_w1_smb2)
        ent_w2_smb2 = world.get_entrance("SMB2 Game -> World 2 (SMB2)")
        world.set_rule(ent_w2_smb2, can_enter_w2_smb2)
        ent_w3_smb2 = world.get_entrance("SMB2 Game -> World 3 (SMB2)")
        world.set_rule(ent_w3_smb2, can_enter_w3_smb2)
        ent_w4_smb2 = world.get_entrance("SMB2 Game -> World 4 (SMB2)")
        world.set_rule(ent_w4_smb2, can_enter_w4_smb2)
        ent_w5_smb2 = world.get_entrance("SMB2 Game -> World 5 (SMB2)")
        world.set_rule(ent_w5_smb2, can_enter_w5_smb2)
        ent_w6_smb2 = world.get_entrance("SMB2 Game -> World 6 (SMB2)")
        world.set_rule(ent_w6_smb2, can_enter_w6_smb2)
        ent_w7_smb2 = world.get_entrance("SMB2 Game -> World 7 (SMB2)")
        world.set_rule(ent_w7_smb2, can_enter_w7_smb2)
    if world.options.available_smb3.value != 0:
        ent_w1_smb3 = world.get_entrance("SMB3 Game -> World 1 (SMB3)")
        world.set_rule(ent_w1_smb3, can_enter_w1_smb3)
        ent_w2_smb3 = world.get_entrance("SMB3 Game -> World 2 (SMB3)")
        world.set_rule(ent_w2_smb3, can_enter_w2_smb3)
        ent_w3_smb3 = world.get_entrance("SMB3 Game -> World 3 (SMB3)")
        world.set_rule(ent_w3_smb3, can_enter_w3_smb3)
        ent_w4_smb3 = world.get_entrance("SMB3 Game -> World 4 (SMB3)")
        world.set_rule(ent_w4_smb3, can_enter_w4_smb3)
        ent_w5_smb3 = world.get_entrance("SMB3 Game -> World 5 (SMB3)")
        world.set_rule(ent_w5_smb3, can_enter_w5_smb3)
        ent_w6_smb3 = world.get_entrance("SMB3 Game -> World 6 (SMB3)")
        world.set_rule(ent_w6_smb3, can_enter_w6_smb3)
        ent_w7_smb3 = world.get_entrance("SMB3 Game -> World 7 (SMB3)")
        world.set_rule(ent_w7_smb3, can_enter_w7_smb3)
        ent_w8_smb3 = world.get_entrance("SMB3 Game -> World 8 (SMB3)")
        world.set_rule(ent_w8_smb3, can_enter_w8_smb3)
    
    # Some other Entrance Blockers
    if world.options.available_smb1.value != 0:
        # 2-2 and 7-2 both need Swim to complete
        ent_w2_2_smb1 = world.get_entrance("World 2-1 Tile (SMB1) -> World 2-2 Tile (SMB1)")
        world.set_rule(ent_w2_2_smb1, Has(item_name.ability_swim_smb1))
        ent_w7_2_smb1 = world.get_entrance("World 7-1 Tile (SMB1) -> World 7-2 Tile (SMB1)")
        world.set_rule(ent_w7_2_smb1, Has(item_name.ability_swim_smb1))
        # Same as above, but for World X2 and X7
        if world.options.hard_worlds_smb1.value != 0:
            ent_w2x2_smb1 = world.get_entrance("World 2x1 Tile (SMB1) -> World 2x2 Tile (SMB1)")
            world.set_rule(ent_w2x2_smb1, Has(item_name.ability_swim_smb1))
            ent_w7x2_smb1 = world.get_entrance("World 7x1 Tile (SMB1) -> World 7x2 Tile (SMB1)")
            world.set_rule(ent_w7x2_smb1, Has(item_name.ability_swim_smb1))
    if world.options.available_smbll.value != 0:
        # 3-2 and 6-2 both need Swim to complete
        ent_w3_2_smbll = world.get_entrance("World 3-1 Tile (SMBLL) -> World 3-2 Tile (SMBLL)")
        world.set_rule(ent_w3_2_smbll, Has(item_name.ability_swim_smbll))
        ent_w6_2_smbll = world.get_entrance("World 6-1 Tile (SMBLL) -> World 6-2 Tile (SMBLL)")
        world.set_rule(ent_w6_2_smbll, Has(item_name.ability_swim_smbll))
        # 8-2 requires Climb to reach the Sky Area with the Flagpole.
        ent_w8_2_smbll = world.get_entrance("World 8-1 Tile (SMBLL) -> World 8-2 Tile (SMBLL)")
        world.set_rule(ent_w8_2_smbll, Has(item_name.ability_climb_smbll))
        # Fantasy World requires Swim (this technically could have been alongside the World Key).
        if world.options.fantasy_world_smbll.value != 0:
            ent_w9_1_smbll = world.get_entrance("World 9 (SMBLL) -> World 9-1 Tile (SMBLL)")
            world.set_rule(ent_w9_1_smbll, Has(item_name.ability_swim_smbll))
        # B-2 also requires Swim.
        if world.options.bonus_worlds_smbll.value != 0:
            ent_wb_2_smbll = world.get_entrance("World B-1 Tile (SMBLL) -> World B-2 Tile (SMBLL)")
            world.set_rule(ent_wb_2_smbll, Has(item_name.ability_swim_smbll))
    if world.options.available_smb2.value != 0:
        # Character Select can only be enterable if Game is Unlocked (World Key Required)
        if world.options.char_select_checks_smb2.value != 0:
            ent_char_sel_smb2 = world.get_entrance("SMB2 Game -> Character Select (SMB2)")
            world.set_rule(ent_char_sel_smb2, HasFromList(item_name.key_world_1_smb2,item_name.key_world_2_smb2,item_name.key_world_3_smb2,item_name.key_world_4_smb2,item_name.key_world_5_smb2,item_name.key_world_6_smb2,item_name.key_world_7_smb2,item_name.key_prog_smb2))
        # SMB2 requires Grab for like 90% of things, and Climb is sometimes also needed for a lot of things
        # Since we don't have Entrance Rando yet, we can just force the earliest Level of a World to require them as needed.
        # Level 1-2 literally can't escape the starting screen without Grab
        ent_w1_lvl_smb2 = world.get_entrance("World 1-1 Tile (SMB2) -> World 1-2 Tile (SMB2)")
        world.set_rule(ent_w1_lvl_smb2, Has(item_name.ability_carry_smb2))
        # World 2 requires Grab to pick up sand in the first level
        ent_w2_lvl_smb2 = world.get_entrance("World 2 (SMB2) -> World 2-1 Tile (SMB2)")
        world.set_rule(ent_w2_lvl_smb2, Has(item_name.ability_carry_smb2))
        # World 3 has its first level require Grab to get out of the vertical section.
        ent_w3_lvl_smb2 = world.get_entrance("World 3 (SMB2) -> World 3-1 Tile (SMB2)")
        world.set_rule(ent_w3_lvl_smb2, Has(item_name.ability_carry_smb2))
        # Level 4-2 requires Climb to get out of the starting screen (as does 4-3).
        ent_w4_lvl_smb2 = world.get_entrance("World 4-1 Tile (SMB2) -> World 4-2 Tile (SMB2)")
        world.set_rule(ent_w4_lvl_smb2, Has(item_name.ability_climb_smb2))
        # 5-2 needs Climb to complete the Level, but also needs Grab for 5-1's Birdo.
        ent_w5_lvl_smb2 = world.get_entrance("World 5-1 Tile (SMB2) -> World 5-2 Tile (SMB2)")
        world.set_rule(ent_w5_lvl_smb2, Has(item_name.ability_climb_smb2))
        ent_w5_1_smb2 = world.get_entrance("World 5 (SMB2) -> World 5-1 Tile (SMB2)")
        world.set_rule(ent_w5_1_smb2, Has(item_name.ability_carry_smb2))
        # Note that 5-3 will need Grab anyway to remove the Mushroom Block to continue.
        # 6-1 needs Grab to get a Key from a sand-filled Vase, 6-3 needs Climb to beat.
        ent_w6_lvl_smb2 = world.get_entrance("World 6 (SMB2) -> World 6-1 Tile (SMB2)")
        world.set_rule(ent_w6_lvl_smb2, Has(item_name.ability_carry_smb2))
        ent_w6_3_smb2 = world.get_entrance("World 6-2 Tile (SMB2) -> World 6-3 Tile (SMB2)")
        world.set_rule(ent_w6_3_smb2, Has(item_name.ability_climb_smb2))
        # 7-1 requires both Climb *AND* Grab in order to beat.
        ent_w7_lvl_smb2 = world.get_entrance("World 7 (SMB2) -> World 7-1 Tile (SMB2)")
        world.set_rule(ent_w7_lvl_smb2, HasAll(item_name.ability_carry_smb2, item_name.ability_climb_smb2))
        # Handle some of the "Basic Grab Behavior" conditions.
        # 1-1 has a fairly well-known shortcut that is doable with just SuperJumps and some Grass-Plucking. Birdo's Eggs are also grabbable with Basic Grab.
        # The shortcut is a little difficult with Toad w/o Dash due to timing over the gap.
        ent_w1_1_smb2 = world.get_entrance("World 1 (SMB2) -> World 1-1 Tile (SMB2)")
        world.set_rule(ent_w1_1_smb2, can_basic_grab_smb2)
        # 4-1 similarly is doable with only a Basic Grab, as the Rocket required is inside Grass, and the Crystal is out in the open.
        ent_w4_1_smb2 = world.get_entrance("World 4 (SMB2) -> World 4-1 Tile (SMB2)")
        world.set_rule(ent_w4_1_smb2, can_basic_grab_smb2)
    if world.options.available_smb3.value != 0:
        # World 3's first level requires Swimming, which would be a problem if SMB3 is our only Start
        ent_w3_smb3 = world.get_entrance("World 3 (SMB3) -> World 3-1 Tile (SMB3)")
        world.set_rule(ent_w3_smb3, Has(item_name.ability_swim_smb3))
        # The Sky Tower needs Climb in order to reach the Sky World portion of World 5
        ent_5_twr_smb3 = world.get_entrance("World 5-Tower Tile (SMB3) -> World 5-4 Tile (SMB3)")
        world.set_rule(ent_5_twr_smb3, Has(item_name.ability_climb_smb3))
        # World 6 has a few levels that need abilities to progress
        ent_w6_5_smb3 = world.get_entrance("World 6-4 Tile (SMB3) -> World 6-5 Tile (SMB3)")
        ent_w6_6_smb3 = world.get_entrance("World 6-4 Tile (SMB3) -> World 6-6 Tile (SMB3)")
        world.set_rule(ent_w6_5_smb3, can_fly_smb3 & Has(item_name.ability_carry_smb3))
        world.set_rule(ent_w6_6_smb3, Has(item_name.ability_swim_smb3)) # TODO: Frog Power-Up Recycle Logic
        # 6-9 has a shortcut that *might* be doable w/ only regular flight, but I haven't tested/checked
        # The shortcut is easily doable with the P-Wings though!
        ent_w6_9_smb3 = world.get_entrance("World 6-8 Tile (SMB3) -> World 6-9 Tile (SMB3)")
        world.set_rule(ent_w6_9_smb3, Has(item_name.ability_swim_smb3)) # TODO: Refer to above TODO
        # World 7 requires a weird collection of abilities to get through
        # 7-2 needs some form of Swimming to beat, which is also needed for 7-4
        ent_w7_2_smb3 = world.get_entrance("World 7-1 Tile (SMB3) -> World 7-2 Tile (SMB3)")
        world.set_rule(ent_w7_2_smb3, Has(item_name.ability_swim_smb3)) # TODO: Refer to above TODO
        # Note that 7-5 needs Grab in order to reach the Mushroom House behind it
        # 7-Fort1 needs both P-Switch and Flight...
        ent_w7_f1_smb3 = world.get_entrance("World 7-4 Tile (SMB3) -> World 7-Fort1 Tile (SMB3)")
        world.set_rule(ent_w7_f1_smb3, can_fly_smb3 & Has(item_name.ability_pswitch_smb3))
        # 7-7 requires the Starman in order to reach 7-9, we can beat 7-8 instead without it
        # 7-8 might still be difficult without some higher Power-Up though...
        ent_w7_7_smb3 = world.get_entrance("World 7-6 Tile (SMB3) -> World 7-7 Tile (SMB3)")
        world.set_rule(ent_w7_7_smb3, Has(item_name.ability_starman_smb3))
        # 7-9 *needs* Grab
        ent_w7_9_from_7_smb3 = world.get_entrance("World 7-7 Tile (SMB3) -> World 7-9 Tile (SMB3)")
        ent_w7_9_from_8_smb3 = world.get_entrance("World 7-8 Tile (SMB3) -> World 7-9 Tile (SMB3)")
        world.set_rule(ent_w7_9_from_7_smb3, Has(item_name.ability_carry_smb3))
        world.set_rule(ent_w7_9_from_8_smb3, Has(item_name.ability_carry_smb3))
        # World 8 Logic, pretty strange here too, but not as much
        # 8-Fort needs the P-Switch, probably some others too but eh
        ent_w8_frt_smb3 = world.get_entrance("World 8-2 Tile (SMB3) -> World 8-Fort Tile (SMB3)")
        world.set_rule(ent_w8_frt_smb3, Has(item_name.ability_pswitch_smb3))

    


    ## Now, let's make some rules!
    ## First, let's handle the transition from the overworld to the bottom right room,
    ## which requires slashing a bush with the Sword.
    ## For this, we need a rule that says "player has a Sword".
    ## We can use a "Has"-type rule from the rule_builder module for this.
    #can_destroy_bush = Has("Sword")
    #
    ## Now we can set our "can_destroy_bush" rule to the entrance which requires slashing a bush to clear the path.
    ## The easiest way to do this is by calling world.set_rule, which works for both Locations and Entrances.
    #world.set_rule(overworld_to_bottom_right_room, can_destroy_bush)
    #
    ## Conditions can also depend on event items.
    #button_pressed = Has("Top Left Room Button Pressed")
    #world.set_rule(right_room_to_final_boss_room, button_pressed)
    #
    ## Some entrance rules may only apply if the player enabled certain options.
    ## In our case, if the hammer option is enabled, we need to add the Hammer requirement to the Entrance from
    ## Overworld to the Top Middle Room.
    #if world.options.hammer:
    #    overworld_to_top_middle_room = world.get_entrance("Overworld to Top Middle Room")
    #    can_smash_brick = Has("Hammer")
    #    world.set_rule(overworld_to_top_middle_room, can_smash_brick)
    #
    ## So far, we've been using "Has" from the Rule Builder to make our rules.
    ## There is another way to make rules that you will see in a lot of older worlds.
    ## A rule can just be  a function that takes a "state" argument and returns a bool.
    ## As a demonstration of what that looks like, let's do it with our final Entrance rule:
    #world.set_rule(overworld_to_top_left_room, lambda state: state.has("Key", world.player))
    ## This style is not really recommended anymore, though.
    ## Using Rule Builder allows the core AP code to do a lot of under-the-hood optimizations.
    ## Rule Builder is quite comprehensive, and even if you have really esoteric rules,
    ## you can make custom rules by subclassing CustomRule.
    ## Since Rule Builder is preferred, we'll re-set this rule to also use "Has" from the Rule Builder.
    #world.set_rule(overworld_to_top_left_room, Has("Key"))


def set_all_location_rules(world: SMASWWorld) -> None:
    ## Location rules work no differently from Entrance rules.
    ## Most of our locations are chests that can simply be opened by walking up to them.
    ## Thus, their logical requirements are covered by the Entrance rules of the Entrances that were required to
    ## reach the region that the chest sits in.
    ## However, our two enemies work differently.
    ## Entering the room with the enemy is not enough, you also need to have enough combat items to be able to defeat it.
    ## So, we need to set requirements on the Locations themselves.
    ## Since combat is a bit more complicated, we'll use this chance to cover some advanced access rule concepts.
    #
    ## In "set_all_entrance_rules", we had a rule for a location that doesn't always exist.
    ## In this case, we had to check for its existence (by checking the player's chosen options) before setting the rule.
    ## Other times, you may have a situation where a location can have two different rules depending on the options.
    ## In our case, the enemy in the right room has more health if hard mode is selected,
    ## so ontop of the Sword, the player will either need one more health or a Shield in hard mode.
    ## First, let's make our sword condition.
    #can_defeat_basic_enemy: Rule = Has("Sword")
    #
    ## Next, we'll check whether hard mode has been chosen in the player options.
    #if world.options.hard_mode:
    #    # We'll make the condition for "Has a Shield or a Health Upgrade".
    #    # We can chain two "Has" conditions together with the | operator to make "Has Shield or has Health Upgrade".
    #    can_withstand_a_hit = Has("Shield") | Has("Health Upgrade")
    #
    #    # Now, we chain this rule to our Sword rule.
    #    # Since we want both conditions to be true, in this case, we have to chain them in an "and" way.
    #    # For this, we can use the & operator.
    #    can_defeat_basic_enemy = can_defeat_basic_enemy & can_withstand_a_hit
    #
    ## Finally, we set our rule onto the Right Room Eney Drop location.
    #right_room_enemy = world.get_location("Right Room Enemy Drop")
    #world.set_rule(right_room_enemy, can_defeat_basic_enemy)
    #
    ## For the final boss, we also need to chain multiple conditions.
    ## First of all, you always need a Sword and a Shield.
    ## So far, we used the | and & operators to chain "Has" rules.
    ## Instead, we can also use HasAny for an or-chain of items, or HasAll for an and-chain of items.
    #has_sword_and_shield: Rule = HasAll("Sword", "Shield")
    #
    ## In hard mode, the player also needs both Health Upgrades to survive long enough to defeat the boss.
    ## For this, we can use the optional "count" parameter for "Has".
    #has_both_health_upgrades = Has("Health Upgrade", count=2)
    #
    ## Previously, we used an "if world.options.hard_mode" condition to check if we should apply the extra requirement.
    ## However, if you're comfortable with boolean logic, there is another way.
    ## OptionFilter is a rule which just resolves to True if the option has the specified value, or False otherwise.
    #hard_mode_is_off = OptionFilter(HardMode, False)
    #
    ## Now we can combine our rule as follows.
    #can_defeat_final_boss = has_sword_and_shield & (hard_mode_is_off | has_both_health_upgrades)
    ## If you're not as comfortable with boolean logic, it might be somewhat confusing why this is correct.
    ## There is nothing wrong with using "if" conditions to check for options, if you find that easier to understand.
    #
    ## Finally, we apply the rule to our "Final Boss Defeated" event location.
    #final_boss = world.get_location("Final Boss Defeated")
    #world.set_rule(final_boss, can_defeat_final_boss)
    
    # Handle SMB1 and SMBLL Goal Item
    if world.options.available_smb1.value != 0:
        rule_smb1_goal_loc = world.get_location(location_name.loc_goal_smb1)
        # Getting Goal Options
        if world.options.goal_smb1.value == GoalSmb1.option_final_bowser:
            world.set_rule(rule_smb1_goal_loc, Has(item_name.goal_smb1_part))
        elif world.options.goal_smb1.value == GoalSmb1.option_true_bowser:
            world.set_rule(rule_smb1_goal_loc, Has(item_name.goal_smb1_true))
        elif world.options.goal_smb1.value == GoalSmb1.option_both_bowsers:
            world.set_rule(rule_smb1_goal_loc, HasAll(item_name.goal_smb1_part,item_name.goal_smb1_true))
    if world.options.available_smbll.value != 0:
        rule_smbll_goal_loc = world.get_location(location_name.loc_goal_smbll)
        # Getting Goal Options
        if world.options.goal_smbll.value == GoalSmbll.option_final_bowser:
            world.set_rule(rule_smbll_goal_loc, Has(item_name.goal_smbll_part))
        elif world.options.goal_smbll.value == GoalSmbll.option_true_bowser:
            world.set_rule(rule_smbll_goal_loc, Has(item_name.goal_smbll_true))
        elif world.options.goal_smbll.value == GoalSmbll.option_both_bowsers:
            world.set_rule(rule_smbll_goal_loc, HasAll(item_name.goal_smbll_part,item_name.goal_smbll_true))
    
    # Note that the other Goal-Related Logics are handled by entrance logic instead
    # They will need to be split later when we get around to various other Extra Locations
    
    
    # Real Location Logics
    
    
    # TODO: SMB1 Logics
    
    
    # TODO: SMBLL Logics
    
    
    # SMB2 Logics
    if world.options.available_smb2.value != 0:
        # Handle Character Select Locations, if applicable
        if world.options.char_select_checks_smb2.value != 0:
            rule_loc_char_mario = world.get_location(location_name.loc_char_pick_mario_smb2)
            world.set_rule(rule_loc_char_mario, Has(item_name.unlock_char_mario))
            rule_loc_char_peach = world.get_location(location_name.loc_char_pick_peach_smb2)
            world.set_rule(rule_loc_char_peach, Has(item_name.unlock_char_peach))
            rule_loc_char_toad = world.get_location(location_name.loc_char_pick_toad_smb2)
            world.set_rule(rule_loc_char_toad, Has(item_name.unlock_char_toad))
            rule_loc_char_luigi = world.get_location(location_name.loc_char_pick_luigi_smb2)
            world.set_rule(rule_loc_char_luigi, Has(item_name.unlock_char_luigi))
        # Handle Mushroom Checks
        # World 1
        rule_loc_w1_1_mush_1 = world.get_location(location_name.loc_world_1_1_smb2_mush_1)
        world.set_rule(rule_loc_w1_1_mush_1, can_subspace_mushroom)
        rule_loc_w1_1_mush_2 = world.get_location(location_name.loc_world_1_1_smb2_mush_2)
        world.set_rule(rule_loc_w1_1_mush_2, can_subspace_mushroom)
        rule_loc_w1_2_mush_1 = world.get_location(location_name.loc_world_1_2_smb2_mush_1)
        world.set_rule(rule_loc_w1_2_mush_1, can_subspace_mushroom)
        rule_loc_w1_2_mush_2 = world.get_location(location_name.loc_world_1_2_smb2_mush_2)
        world.set_rule(rule_loc_w1_2_mush_2, can_subspace_mushroom)
        rule_loc_w1_3_mush_1 = world.get_location(location_name.loc_world_1_3_smb2_mush_1)
        world.set_rule(rule_loc_w1_3_mush_1, can_subspace_mushroom)
        rule_loc_w1_3_mush_2 = world.get_location(location_name.loc_world_1_3_smb2_mush_2)
        world.set_rule(rule_loc_w1_3_mush_2, can_subspace_mushroom)
        # World 2
        rule_loc_w2_1_mush_1 = world.get_location(location_name.loc_world_2_1_smb2_mush_1)
        world.set_rule(rule_loc_w2_1_mush_1, can_subspace_mushroom)
        rule_loc_w2_2_mush_1 = world.get_location(location_name.loc_world_2_2_smb2_mush_1)
        world.set_rule(rule_loc_w2_2_mush_1, can_subspace_mushroom)
        rule_loc_w2_2_mush_2 = world.get_location(location_name.loc_world_2_2_smb2_mush_2)
        world.set_rule(rule_loc_w2_2_mush_2, can_subspace_mushroom)
        rule_loc_w2_3_mush_1 = world.get_location(location_name.loc_world_2_3_smb2_mush_1)
        world.set_rule(rule_loc_w2_3_mush_1, can_subspace_mushroom)
        rule_loc_w2_3_mush_2 = world.get_location(location_name.loc_world_2_3_smb2_mush_2)
        world.set_rule(rule_loc_w2_3_mush_2, can_subspace_mushroom)
        # World 3
        rule_loc_w3_1_mush_1 = world.get_location(location_name.loc_world_3_1_smb2_mush_1)
        world.set_rule(rule_loc_w3_1_mush_1, can_subspace_mushroom)
        rule_loc_w3_1_mush_2 = world.get_location(location_name.loc_world_3_1_smb2_mush_2)
        world.set_rule(rule_loc_w3_1_mush_2, can_subspace_mushroom)
        rule_loc_w3_2_mush_1 = world.get_location(location_name.loc_world_3_2_smb2_mush_1)
        world.set_rule(rule_loc_w3_2_mush_1, can_subspace_mushroom)
        rule_loc_w3_2_mush_2 = world.get_location(location_name.loc_world_3_2_smb2_mush_2)
        world.set_rule(rule_loc_w3_2_mush_2, can_subspace_mushroom)
        rule_loc_w3_3_mush_1 = world.get_location(location_name.loc_world_3_3_smb2_mush_1)
        world.set_rule(rule_loc_w3_3_mush_1, can_subspace_mushroom)
        rule_loc_w3_3_mush_2 = world.get_location(location_name.loc_world_3_3_smb2_mush_2)
        world.set_rule(rule_loc_w3_3_mush_2, can_subspace_mushroom)
        # World 4
        rule_loc_w4_1_mush_1 = world.get_location(location_name.loc_world_4_1_smb2_mush_1)
        world.set_rule(rule_loc_w4_1_mush_1, can_subspace_mushroom)
        rule_loc_w4_1_mush_2 = world.get_location(location_name.loc_world_4_1_smb2_mush_2)
        world.set_rule(rule_loc_w4_1_mush_2, can_subspace_mushroom)
        rule_loc_w4_2_mush_1 = world.get_location(location_name.loc_world_4_2_smb2_mush_1)
        world.set_rule(rule_loc_w4_2_mush_1, can_subspace_mushroom)
        rule_loc_w4_2_mush_2 = world.get_location(location_name.loc_world_4_2_smb2_mush_2)
        world.set_rule(rule_loc_w4_2_mush_2, can_subspace_mushroom)
        rule_loc_w4_3_mush_1 = world.get_location(location_name.loc_world_4_3_smb2_mush_1)
        world.set_rule(rule_loc_w4_3_mush_1, can_subspace_mushroom)
        rule_loc_w4_3_mush_2 = world.get_location(location_name.loc_world_4_3_smb2_mush_2)
        world.set_rule(rule_loc_w4_3_mush_2, can_subspace_mushroom)
        # World 5
        rule_loc_w5_1_mush_1 = world.get_location(location_name.loc_world_5_1_smb2_mush_1)
        world.set_rule(rule_loc_w5_1_mush_1, can_subspace_mushroom)
        rule_loc_w5_1_mush_2 = world.get_location(location_name.loc_world_5_1_smb2_mush_2)
        world.set_rule(rule_loc_w5_1_mush_2, can_subspace_mushroom)
        rule_loc_w5_2_mush_1 = world.get_location(location_name.loc_world_5_2_smb2_mush_1)
        world.set_rule(rule_loc_w5_2_mush_1, can_subspace_mushroom)
        rule_loc_w5_2_mush_2 = world.get_location(location_name.loc_world_5_2_smb2_mush_2)
        world.set_rule(rule_loc_w5_2_mush_2, can_subspace_mushroom)
        rule_loc_w5_3_mush_1 = world.get_location(location_name.loc_world_5_3_smb2_mush_1)
        world.set_rule(rule_loc_w5_3_mush_1, can_subspace_mushroom)
        rule_loc_w5_3_mush_2 = world.get_location(location_name.loc_world_5_3_smb2_mush_2)
        world.set_rule(rule_loc_w5_3_mush_2, can_subspace_mushroom)
        # World 6
        rule_loc_w6_1_mush_1 = world.get_location(location_name.loc_world_6_1_smb2_mush_1)
        world.set_rule(rule_loc_w6_1_mush_1, can_subspace_mushroom)
        rule_loc_w6_1_mush_2 = world.get_location(location_name.loc_world_6_1_smb2_mush_2)
        world.set_rule(rule_loc_w6_1_mush_2, can_subspace_mushroom)
        rule_loc_w6_2_mush_1 = world.get_location(location_name.loc_world_6_2_smb2_mush_1)
        world.set_rule(rule_loc_w6_2_mush_1, can_subspace_mushroom)
        rule_loc_w6_3_mush_1 = world.get_location(location_name.loc_world_6_3_smb2_mush_1)
        world.set_rule(rule_loc_w6_3_mush_1, can_subspace_mushroom)
        rule_loc_w6_3_mush_2 = world.get_location(location_name.loc_world_6_3_smb2_mush_2)
        world.set_rule(rule_loc_w6_3_mush_2, can_subspace_mushroom)
        # World 7
        rule_loc_w7_1_mush_1 = world.get_location(location_name.loc_world_7_1_smb2_mush_1)
        world.set_rule(rule_loc_w7_1_mush_1, can_subspace_mushroom)
        rule_loc_w7_1_mush_2 = world.get_location(location_name.loc_world_7_1_smb2_mush_2)
        world.set_rule(rule_loc_w7_1_mush_2, can_subspace_mushroom)
        rule_loc_w7_2_mush_1 = world.get_location(location_name.loc_world_7_2_smb2_mush_1)
        world.set_rule(rule_loc_w7_2_mush_1, can_subspace_mushroom)
        rule_loc_w7_2_mush_2 = world.get_location(location_name.loc_world_7_2_smb2_mush_2)
        world.set_rule(rule_loc_w7_2_mush_2, can_subspace_mushroom)
        # TODO: Level Clears
        # World X
        
    
    temp = 0
    # TODO: SMB3 Logics
    
    
    
    
    
    


def set_completion_condition(world: SMASWWorld) -> None:
    ## Finally, we need to set a completion condition for our world, defining what the player needs to win the game.
    ## For this, we can use world.set_completion_rule.
    ## You can just set a completion condition directly like any other condition, referencing items the player receives:
    #world.set_completion_rule(HasAll("Sword", "Shield"))
    #
    ## In our case, we went for the Victory event design pattern (see create_events() in locations.py).
    ## So lets undo what we just did, and instead set the completion condition to:
    #world.set_completion_rule(Has("Victory"))
    world.set_completion_rule(Has(item_name.goal_smasw))


# One final comment about rules:
# If your world exclusively uses Rule Builder rules (like SMASW), it's worth trying CachedRuleBuilderWorld.
# CachedRuleBuilderWorld is a subclass of World that has a bunch of caching magic to make rules faster.
# Just have your world class subclass CachedRuleBuilderWorld instead of World:
#   class SMASWWorld(CachedRuleBuilderWorld): ...
# This may speed up your world, or it may make it slower.
# The exact factors are complex and not well understood, but there is no harm in trying it.
# Generate a few seeds and see if there is a noticeable difference!
# If you're wondering, author has checked: SMASW is too simple to see any benefits, so we'll stick with "World".
