from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle, DefaultOnToggle, Visibility

# Goal Related Stuff
class GoalCount(Range):
    """
    How many games must be completed in order to consider SMASW as Goaled.
    NOTE: This value gets adjusted depending on how many games are available to be played.
    """

    display_name = "SMASW Goal Requirements"

    range_start = 1
    range_end = 4
    default = 4

class AvailableFailsafe(Choice):
    """
    Acts as a failsafe in the case that "Random" rolls a Disallow on all games, does nothing otherwise.
    """

    display_name = "Game Availability Failsafe"
    option_smb1 = 0x01
    option_smbll = 0x02
    option_smb2 = 0x04
    option_smb3 = 0x08
    default = option_smb1

class GoalSmb1(Choice):
    """
    Sets the Goal condition for SMB1.
    Final Bowser - Player must defeat World 8-4's Bowser to Goal
    True Bowser - Player must defeat World 8x4's Bowser to Goal
    Both Bowsers - Player must defeat both 8-4 and 8x4's Bowsers to Goal
    """

    display_name = "Goal (SMB1)"
    option_final_bowser = 0x01
    option_true_bowser = 0x02
    option_both_bowsers = 0x03
    default = option_final_bowser

class AvailableSmb1(Choice):
    """
    Determines if SMB1 is allowed to be played for this seed.
    Disallow - Game is locked and never playable
    Allow - Game may be accessible
    Required - Game is required to for SMASW's Goal
    """

    display_name = "Game Availability (SMB1)"
    option_disallow = 0
    option_allow = 0x01
    option_required = 0x0101
    default = option_allow

class BosscoinSmb1(Range):
    """
    Determines how many Boss Coins the Player requires in order to unlock the corresponding Final Level(s).
    NOTE: This option automatically gets clamped depending on Goal and Hardmode Worlds Options.
    """

    display_name = "Boss Coin Requirements (SMB1)"

    range_start = 0
    range_end = 15
    default = 7

class GoalSmbll(Choice):
    """
    Sets the Goal condition for SMBLL.
    Final Bowser - Player must defeat World 8-4's Bowser to Goal
    True Bowser - Player must defeat World D-4's Bowser to Goal
    Both Bowsers - Player must defeat both 8-4 and D-4's Bowsers to Goal
    """

    display_name = "Goal (SMBLL)"
    option_final_bowser = 0x08
    option_true_bowser = 0x10
    option_both_bowsers = 0x18
    default = option_final_bowser

class AvailableSmbll(Choice):
    """
    Determines if SMBLL is allowed to be played for this seed.
    Disallow - Game is locked and never playable
    Allow - Game may be accessible
    Required - Game is required to for SMASW's Goal
    """

    display_name = "Game Availability (SMBLL)"
    option_disallow = 0
    option_allow = 0x02
    option_required = 0x0202
    default = option_allow

class BosscoinSmbll(Range):
    """
    Determines how many Boss Coins the Player requires in order to unlock the corresponding Final Level(s).
    NOTE: This option automatically gets clamped depending on Goal and Bonus Worlds Options.
    """

    display_name = "Boss Coin Requirements (SMBLL)"

    range_start = 0
    range_end = 11
    default = 7

class GoalSmb2(Choice):
    """
    Sets the Goal condition for SMB2.
    (Egg Hunt isn't currently implemented at this time)
    """

    display_name = "Goal (SMB2)"
    option_wart = 0x40
    default = option_wart

class AvailableSmb2(Choice):
    """
    Determines if SMB2 is allowed to be played for this seed.
    Disallow - Game is locked and never playable
    Allow - Game may be accessible
    Required - Game is required to for SMASW's Goal
    """

    display_name = "Game Availability (SMB2)"
    option_disallow = 0
    option_allow = 0x04
    option_required = 0x0404
    default = option_allow

class BosscoinSmb2(Range):
    """
    Determines how many Boss Coins the Player requires in order to unlock Wart's Castle.
    """

    display_name = "Boss Coin Requirements (SMB2)"

    range_start = 0
    range_end = 6
    default = 6

class GoalSmb3(Choice):
    """
    Sets the Goal condition for SMB3.
    (Egg Hunt isn't currently implemented at this time)
    """

    display_name = "Goal (SMB3)"
    option_bowser = 0x0100
    default = option_bowser

class AvailableSmb3(Choice):
    """
    Determines if SMB3 is allowed to be played for this seed.
    Disallow - Game is locked and never playable
    Allow - Game may be accessible
    Required - Game is required to for SMASW's Goal
    """

    display_name = "Game Availability (SMB3)"
    option_disallow = 0
    option_allow = 0x08
    option_required = 0x0808
    default = option_allow

class BosscoinSmb3(Range):
    """
    Determines how many Boss Coins the Player requires in order to unlock Bowser's Castle.
    """

    display_name = "Boss Coin Requirements (SMB3)"

    range_start = 0
    range_end = 7
    default = 7

############

# Other Global SMASW Logic Options
class EasyPool(Toggle):
    """
    Dictates whether the Itempool gets an extra set of Progression Items.
    This can help make it easier for the Player to progress through their Game.
    Recommended for Players new to Multiworld Randomizers or new to SMASW's Randomizer.
    NOTE: This option takes priority over each Sub-Game's "Easy Itempool" Option if enabled!
    """

    display_name = "Easy Itempool (SMASW)"


# SMB1 Logic Options
class HardWorldsSmb1(DefaultOnToggle):
    """
    Enables Hardmode Worlds if active (e.g. World X1 thru X8).
    """

    display_name = "Enable Hardmode Worlds (SMB1)"

class ProgPowersSmb1(DefaultOnToggle):
    """
    Determines if Power-Ups are Progressive or Separate.
    Progressive Power-Ups go Super Mushroom -> Fire Flower
    """

    display_name = "Enable Progressive Power-Ups (SMB1)"

class ProgKeysSmb1(Toggle):
    """
    Determines if World Keys are Progressive or Unique.
    """

    display_name = "Enable Progressive World Keys (SMB1)"

class DupeswapKeysSmb1(Choice):
    """
    Dictates the behavior of picking up Duplicate World Keys, does nothing if Progressive World Keys is enabled.
    This also affects how the World Keys are populated into the Item Pool.
    Disable - Picking up an extra World Key does nothing.
    Dupeswap, Similar - Picking up an extra World Key unlocks the corresponding World of the other Difficulty. Hardmode World Keys are replaced with Normal World Keys.
    Dupeswap, Unique - Picking up an extra World Key unlocks the corresponding World of the other Difficulty. Hardmode World Keys are separate from Normal World Keys.
    """

    display_name = "Dupeswap World Key Behavior (SMB1)"
    option_disable = 0
    option_dupeswap_similar = 1
    option_dupeswap_unique = 2
    default = option_dupeswap_similar


class EasyPoolSmb1(Toggle):
    """
    Dictates whether the Itempool gets an extra set of Progression Items.
    This can help make it easier for the Player to progress through their Game.
    Recommended for Players new to Multiworld Randomizers or new to SMASW's Randomizer.
    NOTE: This option is superseded by the Global "Easy Itempool" Option if that's activated!
    """

    display_name = "Easy Itempool (SMB1)"


# SMBLL Logic Options
class BonusWorldsSmbll(DefaultOnToggle):
    """
    Enables Bonus Worlds if active (e.g. World A thru D).
    """

    display_name = "Enable Bonus Worlds (SMBLL)"

class FantasyWorldSmbll(Toggle):
    """
    Enables the Fantasy World (World 9) if active.
    """

    display_name = "Enable Fantasy World (SMBLL)"

class ProgPowersSmbll(DefaultOnToggle):
    """
    Determines if Power-Ups are Progressive or Separate.
    Progressive Power-Ups go Super Mushroom -> Fire Flower
    """

    display_name = "Enable Progressive Power-Ups (SMBLL)"

class ProgKeysSmbll(Toggle):
    """
    Determines if World Keys are Progressive or Unique.
    """

    display_name = "Enable Progressive World Keys (SMBLL)"


class EasyPoolSmbll(Toggle):
    """
    Dictates whether the Itempool gets an extra set of Progression Items.
    This can help make it easier for the Player to progress through their Game.
    Recommended for Players new to Multiworld Randomizers or new to SMASW's Randomizer.
    NOTE: This option is superseded by the Global "Easy Itempool" Option if that's activated!
    """

    display_name = "Easy Itempool (SMBLL)"


# SMB2 Logic Options
class UnlockMario(Choice):
    """
    Determines if Mario is already Unlocked as a Selectable Character for SMB2.
    NOTE: In the event that "Random" rolls Off for all Characters, this option will always turn on.
    """

    display_name = "Start With Mario (SMB2)"
    option_disable = 0
    option_enable = 1
    default = option_enable

class UnlockLuigi(Choice):
    """
    Determines if Luigi is already Unlocked as a Selectable Character for SMB2.
    """

    display_name = "Start With Luigi (SMB2)"
    option_disable = 0
    option_enable = 2
    default = option_enable

class UnlockToad(Choice):
    """
    Determines if Toad is already Unlocked as a Selectable Character for SMB2.
    """

    display_name = "Start With Toad (SMB2)"
    option_disable = 0
    option_enable = 4
    default = option_enable

class UnlockPeach(Choice):
    """
    Determines if Peach is already Unlocked as a Selectable Character for SMB2.
    """

    display_name = "Start With Peach (SMB2)"
    option_disable = 0
    option_enable = 8
    default = option_enable

class CharSelChecksSmb2(Choice):
    """
    Determines if a Character on the Character Select Screen will grant a Location Check.
    Disable - Characters on the Character Select Screen do not hold Items.
    Highlight Only - Highlighting a Character acts as a Location.
    Select Only - Selecting a Character acts as a Location.
    Enable - Highlighting and Selecting a Character acts as Locations.
    Activating this will add a Location to each Character.
    NOTE: If SMB2 is the only Game Unlocked from the start, this option will automatically be enabled.
    """

    display_name = "Character Select Checks (SMB2)"
    option_disable = 0
    option_highlight = 1
    option_select = 2
    option_enable = 3
    default = option_enable

class GrabBehaviorSmb2(Choice):
    """
    Determines how Grabbing and Throwing functions if the Player doesn't have their Grab Ability.
    Basic - Player can Pluck Grass, Grab Birdo's Eggs and Crystals, and Throw Eggs and Veggies without the Grab Ability. Grabbing and Throwing other Items still requires finding Grab.
    Standard - The Player must find their Grab Ability in order to Grab and Throw.
    Start With - The Player starts with the Grab Ability already available.
    NOTE: If SMB2 is the only Game Unlocked from the start, this option will be forced to either Basic or Start With.
    """

    display_name = "Grab Behavior (SMB2)"
    option_basic = 0
    option_standard = 1
    option_start_with = 2
    default = option_standard

class ProgHealthSmb2(Toggle):
    """
    Determines if Health Pickup Items are separate to each World or if they follow into the next World.
    Activating this will do the latter.
    """

    display_name = "Enable Global Progressive Health (SMB2)"

class MaxHealthSmb2(Range):
    """
    The Maximum amount of Health the Player can have per World.
    This, along with Starting Health, determines how many Health Upgrades are placed in the Item Pool.
    """

    display_name = "Maximum Health (SMB2)"
    range_start = 1
    range_end = 4
    default = 4

class StartHealthSmb2(Range):
    """
    How much Health the Player starts with per World.
    This, along with Maximum Health, determines how many Health Upgrades are placed in the Item Pool.
    """

    display_name = "Starting Health (SMB2)"
    range_start = 1
    range_end = 4
    default = 1

class ProgKeysSmb2(Toggle):
    """
    Determines if World Keys are Progressive or Unique.
    """

    display_name = "Enable Progressive World Keys (SMB2)"


class EasyPoolSmb2(Toggle):
    """
    Dictates whether the Itempool gets an extra set of Progression Items.
    This can help make it easier for the Player to progress through their Game.
    Recommended for Players new to Multiworld Randomizers or new to SMASW's Randomizer.
    NOTE: This option is superseded by the Global "Easy Itempool" Option if that's activated!
    """

    display_name = "Easy Itempool (SMB2)"


# SMB3 Logic Options
class ProgKeysSmb3(Toggle):
    """
    Determines if World Keys are Progressive or Unique.
    """

    display_name = "Enable Progressive World Keys (SMB3)"


class EasyPoolSmb3(Toggle):
    """
    Dictates whether the Itempool gets an extra set of Progression Items.
    This can help make it easier for the Player to progress through their Game.
    Recommended for Players new to Multiworld Randomizers or new to SMASW's Randomizer.
    NOTE: This option is superseded by the Global "Easy Itempool" Option if that's activated!
    """

    display_name = "Easy Itempool (SMB3)"


# QOL Stuff
class StartLivesSmb1(Range):
    """
    How many lives the Player starts with, also affects Game Over.
    """

    display_name = "Starting Lives (SMB1)"
    range_start = 1
    range_end = 100
    default = 5

class SaveLivesSmb1(DefaultOnToggle):
    """
    Determine if the Player's Current Lives gets saved to the File.
    """

    display_name = "Save Current Lives (SMB1)"

class SavePowersSmb1(Toggle):
    """
    Determine if the Player's Current Power-Up gets saved to the File.
    """

    display_name = "Save Current Power-Up (SMB1)"

class SaveCoinsSmb1(Toggle):
    """
    Determine if the Player's Current Coins gets saved to the File.
    """

    display_name = "Save Current Coins (SMB1)"

class StartLivesSmbll(Range):
    """
    How many lives the Player starts with, also affects Game Over.
    """

    display_name = "Starting Lives (SMBLL)"
    range_start = 1
    range_end = 100
    default = 5

class SaveLivesSmbll(DefaultOnToggle):
    """
    Determine if the Player's Current Lives gets saved to the File.
    """

    display_name = "Save Current Lives (SMBLL)"

class SavePowersSmbll(Toggle):
    """
    Determine if the Player's Current Power-Up gets saved to the File.
    """

    display_name = "Save Current Power-Up (SMBLL)"

class SaveCoinsSmbll(Toggle):
    """
    Determine if the Player's Current Coins gets saved to the File.
    """

    display_name = "Save Current Coins (SMBLL)"

class StartLivesSmb2(Range):
    """
    How many lives the Player starts with, also affects Game Over.
    """

    display_name = "Starting Lives (SMB2)"
    range_start = 1
    range_end = 100
    default = 5

class SaveLivesSmb2(DefaultOnToggle):
    """
    Determine if the Player's Current Lives gets saved to the File.
    """

    display_name = "Save Current Lives (SMB2)"

class SaveCoinsSmb2(Toggle):
    """
    Determine if the Player's Current Coins gets saved to the File.
    """

    display_name = "Save Current Coins (SMB2)"

class StartLivesSmb3(Range):
    """
    How many lives the Player starts with, also affects Game Over.
    """

    display_name = "Starting Lives (SMB3)"
    range_start = 1
    range_end = 100
    default = 5

class SaveLivesSmb3(DefaultOnToggle):
    """
    Determine if the Player's Current Lives gets saved to the File.
    """

    display_name = "Save Current Lives (SMB3)"

class SavePowersSmb3(Toggle):
    """
    Determine if the Player's Current Power-Up gets saved to the File.
    """

    display_name = "Save Current Power-Up (SMB3)"

class SaveCoinsSmb3(Toggle):
    """
    Determine if the Player's Current Coins gets saved to the File.
    """

    display_name = "Save Current Coins (SMB3)"



# Hardcoded Options, gets auto-adjusted in-code
class UnlockSmb1(Choice):
    """
    You know what this is.
    """

    display_name = "Unlock SMB1"
    option_lock = 0
    option_unlock = 0x01
    default = option_lock
    visibility = Visibility.spoiler

class UnlockSmbll(Choice):
    """
    You know what this is.
    """

    display_name = "Unlock SMBLL"
    option_lock = 0
    option_unlock = 0x02
    default = option_lock
    visibility = Visibility.spoiler

class UnlockSmb2(Choice):
    """
    You know what this is.
    """

    display_name = "Unlock SMB2"
    option_lock = 0
    option_unlock = 0x04
    default = option_lock
    visibility = Visibility.spoiler

class UnlockSmb3(Choice):
    """
    You know what this is.
    """

    display_name = "Unlock SMB3"
    option_lock = 0
    option_unlock = 0x08
    default = option_lock
    visibility = Visibility.spoiler

class RequireSmb1(Choice):
    """
    You know what this is.
    """

    display_name = "Require SMB1"
    option_normal = 0
    option_require = 0x01
    default = option_normal
    visibility = Visibility.spoiler

class RequireSmbll(Choice):
    """
    You know what this is.
    """

    display_name = "Require SMBLL"
    option_normal = 0
    option_require = 0x02
    default = option_normal
    visibility = Visibility.spoiler

class RequireSmb2(Choice):
    """
    You know what this is.
    """

    display_name = "Require SMB2"
    option_normal = 0
    option_require = 0x04
    default = option_normal
    visibility = Visibility.spoiler

class RequireSmb3(Choice):
    """
    You know what this is.
    """

    display_name = "Require SMB3"
    option_normal = 0
    option_require = 0x08
    default = option_normal
    visibility = Visibility.spoiler

# SMW Stuff

class GoalSmw(Choice):
    """
    You know what this is.
    """

    display_name = "Goal (SMW)"
    option_invalid = 0
    option_bowser = 0x0400
    option_egghunt = 0x0800
    default = option_invalid
    visibility = Visibility.none

class AvailableSmw(Choice):
    """
    You know what this is.
    """

    display_name = "Available Game SMW"
    option_disallow = 0
    option_allow = 0x10
    option_required = 0x1010
    default = option_disallow
    visibility = Visibility.none

class UnlockSmw(Choice):
    """
    You know what this is.
    """

    display_name = "Unlock SMW"
    option_lock = 0
    option_unlock = 0x10
    default = option_lock
    visibility = Visibility.none

class RequireSmw(Choice):
    """
    You know what this is.
    """

    display_name = "Require SMW"
    option_normal = 0
    option_require = 0x1000
    default = option_normal
    visibility = Visibility.none


# We must now define a dataclass inheriting from PerGameCommonOptions that we put all our options in.
# This is in the format "option_name_in_snake_case: OptionClassName".
@dataclass
class SMASWOptions(PerGameCommonOptions):
    goal_smasw_count: GoalCount
    available_failsafe: AvailableFailsafe
    easy_itempool_smasw: EasyPool
    
    # SMB1
    goal_smb1: GoalSmb1
    available_smb1: AvailableSmb1
    bosscoin_smb1: BosscoinSmb1
    
    hard_worlds_smb1: HardWorldsSmb1
    prog_powerups_smb1: ProgPowersSmb1
    prog_keys_smb1: ProgKeysSmb1
    dupeswap_keys_smb1: DupeswapKeysSmb1

    easy_itempool_smb1: EasyPoolSmb1
    
    starting_lives_smb1: StartLivesSmb1
    save_lives_smb1: SaveLivesSmb1
    save_powers_smb1: SavePowersSmb1
    save_coins_smb1: SaveCoinsSmb1
    
    # SMBLL
    goal_smbll: GoalSmbll
    available_smbll: AvailableSmbll
    bosscoin_smbll: BosscoinSmbll
    
    bonus_worlds_smbll: BonusWorldsSmbll
    fantasy_world_smbll: FantasyWorldSmbll
    prog_powerups_smbll: ProgPowersSmbll
    prog_keys_smbll: ProgKeysSmbll

    easy_itempool_smbll: EasyPoolSmbll
    
    starting_lives_smbll: StartLivesSmbll
    save_lives_smbll: SaveLivesSmbll
    save_powers_smbll: SavePowersSmbll
    save_coins_smbll: SaveCoinsSmbll
    
    # SMB2
    goal_smb2: GoalSmb2
    available_smb2: AvailableSmb2
    bosscoin_smb2: BosscoinSmb2
    
    # Characters
    unlocked_mario: UnlockMario
    unlocked_luigi: UnlockLuigi
    unlocked_toad: UnlockToad
    unlocked_peach: UnlockPeach
    char_select_checks_smb2: CharSelChecksSmb2
    # Regular Stuff
    grab_behavior_smb2: GrabBehaviorSmb2
    prog_health_smb2: ProgHealthSmb2
    max_health_smb2: MaxHealthSmb2
    start_health_smb2: StartHealthSmb2
    prog_keys_smb2: ProgKeysSmb2

    easy_itempool_smb2: EasyPoolSmb2
    
    starting_lives_smb2: StartLivesSmb2
    save_lives_smb2: SaveLivesSmb2
    save_coins_smb2: SaveCoinsSmb2
    
    # SMB3
    goal_smb3: GoalSmb3
    available_smb3: AvailableSmb3
    bosscoin_smb3: BosscoinSmb3
    
    prog_keys_smb3: ProgKeysSmb3

    easy_itempool_smb3: EasyPoolSmb3
    
    starting_lives_smb3: StartLivesSmb3
    save_lives_smb3: SaveLivesSmb3
    save_powers_smb3: SavePowersSmb3
    save_coins_smb3: SaveCoinsSmb3
    
    # Hardcoded (Invisible in most cases)
    goal_smw: GoalSmw
    available_smw: AvailableSmw
    
    unlocked_smb1: UnlockSmb1
    unlocked_smbll: UnlockSmbll
    unlocked_smb2: UnlockSmb2
    unlocked_smb3: UnlockSmb3
    unlocked_smw: UnlockSmw
    required_smb1: RequireSmb1
    required_smbll: RequireSmbll
    required_smb2: RequireSmb2
    required_smb3: RequireSmb3
    required_smw: RequireSmw


# If we want to group our options by similar type, we can do so as well. This looks nice on the website.
option_groups = [
    #OptionGroup(
    #    "Gameplay Options",
    #    [HardMode, Hammer, ExtraStartingChest, StartWithOneConfettiCannon, TrapChance],
    #),
    #OptionGroup(
    #    "Aesthetic Options",
    #    [ConfettiExplosiveness, PlayerSprite],
    #),
    OptionGroup(
        "SMASW Main Options",
        [GoalCount, AvailableFailsafe, EasyPool],
    ),
    OptionGroup(
        "SMB1 Goal",
        [GoalSmb1, AvailableSmb1, BosscoinSmb1],
    ),
    OptionGroup(
        "SMB1 Logic",
        [HardWorldsSmb1, ProgPowersSmb1, ProgKeysSmb1, DupeswapKeysSmb1, EasyPoolSmb1],
    ),
    OptionGroup(
        "SMB1 QOL",
        [StartLivesSmb1, SaveLivesSmb1, SavePowersSmb1, SaveCoinsSmb1],
    ),
    OptionGroup(
        "SMBLL Goal",
        [GoalSmbll, AvailableSmbll, BosscoinSmbll],
    ),
    OptionGroup(
        "SMBLL Logic",
        [BonusWorldsSmbll, FantasyWorldSmbll, ProgPowersSmbll, ProgKeysSmbll, EasyPoolSmbll],
    ),
    OptionGroup(
        "SMBLL QOL",
        [StartLivesSmbll, SaveLivesSmbll, SavePowersSmbll, SaveCoinsSmbll],
    ),
    OptionGroup(
        "SMB2 Goal",
        [GoalSmb2, AvailableSmb2, BosscoinSmb2],
    ),
    OptionGroup(
        "SMB2 Logic",
        [UnlockMario, UnlockLuigi, UnlockToad, UnlockPeach, CharSelChecksSmb2, GrabBehaviorSmb2, ProgHealthSmb2, MaxHealthSmb2, StartHealthSmb2, ProgKeysSmb2, EasyPoolSmb2],
    ),
    OptionGroup(
        "SMB2 QOL",
        [StartLivesSmb2, SaveLivesSmb2, SaveCoinsSmb2],
    ),
    OptionGroup(
        "SMB3 Goal",
        [GoalSmb3, AvailableSmb3, BosscoinSmb3],
    ),
    OptionGroup(
        "SMB3 Logic",
        [ProgKeysSmb3, EasyPoolSmb3],
    ),
    OptionGroup(
        "SMB3 QOL",
        [StartLivesSmb3, SaveLivesSmb3, SavePowersSmb3, SaveCoinsSmb3],
    ),
]

# TODO: Actually set up
## Finally, we can define some option presets if we want the player to be able to quickly choose a specific "mode".
#option_presets = {
#    "boring": {
#        "hard_mode": False,
#        "hammer": False,
#        "extra_starting_chest": False,
#        "start_with_one_confetti_cannon": False,
#        "trap_chance": 0,
#        "confetti_explosiveness": ConfettiExplosiveness.range_start,
#        "player_sprite": PlayerSprite.option_human,
#    },
#    "the true way to play": {
#        "hard_mode": True,
#        "hammer": True,
#        "extra_starting_chest": True,
#        "start_with_one_confetti_cannon": True,
#        "trap_chance": 50,
#        "confetti_explosiveness": ConfettiExplosiveness.range_end,
#        "player_sprite": PlayerSprite.option_duck,
#    },
#}
