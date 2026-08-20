from __future__ import annotations

from typing import TYPE_CHECKING

from . import options
from .options import UnlockMario, AvailableFailsafe, AvailableSmb1, UnlockSmb1, AvailableSmbll, \
    UnlockSmbll, AvailableSmb2, UnlockSmb2, AvailableSmb3, UnlockSmb3, GoalSmb1, GoalSmbll, CharSelChecksSmb2, GoalSmb2, \
    GoalSmb3

if TYPE_CHECKING:
    from .world import SMASWWorld


# Yeah
def fix_options(world: SMASWWorld) -> None:
    # Consolidating various values for Allowed Games and Unlocked Characters
    # Unlocked Games are also in here, but they are purely hardcoding
    
    # First up, where we can play the given games
    allowed_game_smb1 = world.options.available_smb1.value
    allowed_game_smbll = world.options.available_smbll.value
    allowed_game_smb2 = world.options.available_smb2.value
    allowed_game_smb3 = world.options.available_smb3.value
    world.options.available_smw.value = 0 # TODO: SMW is not current available
    allowed_game_smw = world.options.available_smw.value
    allowed_game_failsafe = world.options.available_failsafe.value
    
    allowed_game_all = allowed_game_smb1 + allowed_game_smbll + allowed_game_smb2 + allowed_game_smb3 + allowed_game_smw
    
    # Set up games that are pre-unlocked for the slot
    unlocked_game_smb1 = world.options.unlocked_smb1.value
    unlocked_game_smbll = world.options.unlocked_smbll.value
    unlocked_game_smb2 = world.options.unlocked_smb2.value
    unlocked_game_smb3 = world.options.unlocked_smb3.value
    world.options.unlocked_smw.value = 0 # TODO: SMW is not current available
    unlocked_game_smw = world.options.unlocked_smw.value
    
    unlocked_game_all = unlocked_game_smb1 + unlocked_game_smbll + unlocked_game_smb2 + unlocked_game_smb3 + unlocked_game_smw
    
    # Get unlocked SMB2 Characters, if applicable
    unlocked_char_mario = world.options.unlocked_mario.value
    unlocked_char_luigi = world.options.unlocked_luigi.value
    unlocked_char_toad = world.options.unlocked_toad.value
    unlocked_char_peach = world.options.unlocked_peach.value
    
    unlocked_char_all = unlocked_char_mario + unlocked_char_luigi + unlocked_char_toad + unlocked_char_peach
    
    # Conditional Checking...
    if unlocked_char_all == 0: # Random Option rolled no characters
        world.options.unlocked_mario.value = UnlockMario.option_enable # Force Mario to always be unlocked
    if allowed_game_all == 0: # Random Option rolled all games unavailable
        if allowed_game_failsafe == AvailableFailsafe.option_smb1:
            world.options.available_smb1.value = AvailableSmb1.option_allow
            world.options.unlocked_smb1.value = UnlockSmb1.option_unlock
            allowed_game_smb1 = world.options.available_smb1.value
            unlocked_game_smb1 = world.options.unlocked_smb1.value
            allowed_game_all = allowed_game_smb1
            unlocked_game_all = unlocked_game_smb1
        elif allowed_game_failsafe == AvailableFailsafe.option_smbll:
            world.options.available_smbll.value = AvailableSmbll.option_allow
            world.options.unlocked_smbll.value = UnlockSmbll.option_unlock
            allowed_game_smbll = world.options.available_smbll.value
            unlocked_game_smbll = world.options.unlocked_smbll.value
            allowed_game_all = allowed_game_smbll
            unlocked_game_all = unlocked_game_smbll
        elif allowed_game_failsafe == AvailableFailsafe.option_smb2:
            world.options.available_smb2.value = AvailableSmb2.option_allow
            world.options.unlocked_smb2.value = UnlockSmb2.option_unlock
            allowed_game_smb2 = world.options.available_smb2.value
            unlocked_game_smb2 = world.options.unlocked_smb2.value
            allowed_game_all = allowed_game_smb2
            unlocked_game_all = unlocked_game_smb2
        elif allowed_game_failsafe == AvailableFailsafe.option_smb3:
            world.options.available_smb3.value = AvailableSmb3.option_allow
            world.options.unlocked_smb3.value = UnlockSmb3.option_unlock
            allowed_game_smb3 = world.options.available_smb3.value
            unlocked_game_smb3 = world.options.unlocked_smb3.value
            allowed_game_all = allowed_game_smb3
            unlocked_game_all = unlocked_game_smb3
    
    # Randomize which games are unlocked, if applicable
    reroll_attempt = 0
    while unlocked_game_all == 0: # Unlocked Games not pre-set from Failsafe
        # TODO: Allow rerolling if still invalid
        world.options.unlocked_smb1.value = (world.random.randint(0,1) << 0) & allowed_game_smb1
        world.options.unlocked_smbll.value = (world.random.randint(0,1) << 1) & allowed_game_smbll
        world.options.unlocked_smb2.value = (world.random.randint(0,1) << 2) & allowed_game_smb2
        world.options.unlocked_smb3.value = (world.random.randint(0,1) << 3) & allowed_game_smb3
        #world.options.unlocked_smw.value = (world.random.randint(0,1) << 4) & allowed_game_smw
        
        # Update with new randomized values
        unlocked_game_smb1 = world.options.unlocked_smb1.value
        unlocked_game_smbll = world.options.unlocked_smbll.value
        unlocked_game_smb2 = world.options.unlocked_smb2.value
        unlocked_game_smb3 = world.options.unlocked_smb3.value
        unlocked_game_smw = world.options.unlocked_smw.value
        
        unlocked_game_all = unlocked_game_smb1 + unlocked_game_smbll + unlocked_game_smb2 + unlocked_game_smb3 + unlocked_game_smw
        if reroll_attempt > 10:
            from Options import OptionError
            raise OptionError("Failed to reroll for Starting Game Unlock (Were you that unlucky?)")
        reroll_attempt = reroll_attempt + 1
    # Goals
    # Funnel Required Games to respective "options" (for later rule_builder stuff)
    world.options.required_smb1.value = (allowed_game_smb1 >> 8)
    world.options.required_smbll.value = (allowed_game_smbll >> 8)
    world.options.required_smb2.value = (allowed_game_smb2 >> 8)
    world.options.required_smb3.value = (allowed_game_smb3 >> 8)
    world.options.required_smw.value = (allowed_game_smw >> 8)
    # Get number of Playable Games and Required Games
    playable_games = allowed_game_all&0xFF
    playable_count = 0
    #required_games = (allowed_game_all>>8)&0xFF
    #required_count = 0
    
    while playable_games != 0:
        bitgame = playable_games&1
        playable_games = playable_games>>1
        if bitgame == 1:
            playable_count = playable_count + 1
    #while required_games != 0:
    #    bitgame = required_games&1
    #    required_games = required_games>>1
    #    if bitgame == 1:
    #        required_count++
    
    # SMASW Goal Count
    if world.options.goal_smasw_count.value > playable_count:
        world.options.goal_smasw_count.value = playable_count
    # Fixing SMB1's and SMBLL's Boss Coin Requirements
    # First up, we check if SMB1 has Hardmode Worlds enabled
    if world.options.hard_worlds_smb1.value == 0: # disabled
        world.options.goal_smb1.value = GoalSmb1.option_final_bowser
    if world.options.bosscoin_smb1.value > 7 and world.options.hard_worlds_smb1.value == 0:
        world.options.bosscoin_smb1.value = 7
    elif world.options.bosscoin_smb1.value == 15 and world.options.goal_smb1.value == GoalSmb1.option_both_bowsers:
        world.options.bosscoin_smb1.value = 14
    # Do the same for SMBLL's Bonus Worlds
    if world.options.bonus_worlds_smbll.value == 0: # disabled
        world.options.goal_smbll.value = GoalSmbll.option_final_bowser
    if world.options.bosscoin_smbll.value > 7 and world.options.bonus_worlds_smbll.value == 0:
        world.options.bosscoin_smbll.value = 7
    elif world.options.bosscoin_smbll.value == 11 and world.options.goal_smbll.value == GoalSmbll.option_both_bowsers:
        world.options.bosscoin_smb1.value = 10
    #DONE
    
    # Fix SMB2's Max Health if lower than Starting Health
    if world.options.start_health_smb2.value > world.options.max_health_smb2.value:
        world.options.max_health_smb2.value = world.options.start_health_smb2.value
    
    # Setup SMB2 Starting Game Fixes
    if unlocked_game_all == 4:
        world.options.char_select_checks_smb2.value = CharSelChecksSmb2.option_enable
        if world.options.grab_behavior_smb2.value == 1:
            world.options.grab_behavior_smb2.value = world.random.randint(0,1)<<1
        # TODO: Handle Early-Items here? Or in items.py?
    #DONE