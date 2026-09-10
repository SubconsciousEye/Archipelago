# Super Mario All-Stars + Super Mario World
This information page contains various descriptions of the Features and Randomization of a __Super Mario All\-Stars \+ Super Mario World__, shorthanded to __SMASWAP__, Game.

Index:
- [Goaling SMASWAP](#what-is-the-goal-to-beat-smaswap)
- [Available SMASWAP Locations](#what-locations-are-currently-available-for-the-pool)
- [Available SMASWAP Items](#what-items-are-currently-available-for-the-pool)
- [Changes from Vanilla SMASW](#what-are-some-changes-from-the-vanilla-game)
- [Additional SMASWAP Features](#what-are-some-additional-features-of-smaswap)
- [FAQ and Known Issues](#faq-and-known-issues)


## What is the goal to beat SMASWAP?
The goal to beating __SMASWAP__ is highly configurable in the Player's YAML Options. Maybe you will need to beat any 1 Sub-Game, or perhaps you need to complete a number of Sub-Games. There amy also even be a chance you have to do a certain specified list of Sub-Games before you can Goal.

Each Sub-Game additionally has options to further determine which required Sub-Goal is necessary in order to win! Currently, it's simply defeating a `Final Boss` of the Respective Sub-Game, which may require some amount of `Boss Coins` to unlock the corresponding level.

## What Locations are currently available for the Pool?
Regardless of Options, __Level Clears__ are always available in the Location Pool for each available Sub-Game. Defeating (Final) Bosses also counts as a __Level Clear__. Some Sub-Games, such as __SMB2__ have additional Locations that are always on.

Here is a list of all the (Current) Locations that can be in the Pool:
- __Level Clears__
- __Subspace Mushrooms (SMB2 Only)__
- __Character Select Checks (SMB2 Only; Option)__

More Locations will be added to the list as they come around.


## What Items are currently available for the Pool?
Sub-Games each have a subset of Items that they need in order for certain actions to occur. This can be Ability Unlocks or Power-Up Unlocks or even World Keys.

Here is a list of all the (Current) Items that can be in the Pool:
- __World Keys__
    - __Progressive Keys__ can be enabled for each Sub-Game
    - __SMB1__ specifically may have unique __World X Keys__ that unlock the Hardmode Worlds
    - __SMBLL__ will have a unique Key for __World 9__ due to its quirks
- __Power-Up Unlocks__
    - __Progressive Power-Ups__ can be enabled for Sub-Games that have the Option
    - __Super Mushroom States__ for all __Non\-SMB2__ Sub-Games
    - __Fire Flower States__ for all __Non\-SMB2__ Sub-Games
    - __Super Leaf State__ for __SMB3__
    - __Frog Suit State__ for __SMB3__
    - __Hammer Suit State__ for __SMB3__
    - __Tanooki Suit State__ for __SMB3__
    - __P-Wing State__ for __SMB3__
    - __Progressive World Health__ for __SMB2__
        - These can be replaced with __Progressive Health__ that applies to the lowest World first, up to the maximum for the final World.
- __Ability Unlocks__
    - __Dash__
    - __Climb__
    - __Swim__ for all __Non\-SMB2__ Sub-Games
    - __Grab__ for all __Non\-SMB1\/SMBLL__ Sub-Games
        - __SMB2__ has an Option to allow for __Basic Grab__ due to its insistence of the ability.
    - __Starman__
    - __Clock__ for __SMB2__
    - __P-Switch__ for __SMB3__
    - __Kuribo Shoe__ for __SMB3__
    - __Potion__ for __SMB2__
- __Character Unlocks__ for __SMB2__

More Items will be added to the list as they get implemented.


## What are some changes from the Vanilla Game?
__SMASWAP__ changes a lot of things under the hood in order to make it ready for Randomization. Here are a few that may interest you:
- __Single Save File__
    - __SMASW__ has been heavily reworked to allow all Sub-Games to act as one unified Save. This is to allow the Player to be able to receive Items for Sub-Games they aren't current playing, providing a more smooth __SMASWAP__ Experience.
- __Save Power-Ups, Lives, and Coins__
    - If the Player allows for it, they are able to save any of their __Current Lives__, __Current Coins__, and __Current Power-Ups__ to the Save File. This helps ease the Player during play sessions.
- __Re-enter Previously Played Levels__
    - This works two-fold for different Sub-Games; __SMB1__, __SMBLL__, and __SMB2__ can freely select the Level through the Game Select Menu; __SMB3__ can freely re-enter completed Levels.
    - In addition to the above, you can freely __Exit__ the current Level for __SMB2__ and __SMB3__, which will return you to the __Character Select__ and the __Map__ respectively. This is done through the Pause Menu whenever inside a Level.
- __Overhauled Menu Controls__
    - Various Menus have been slightly reworked to provide better controls using the D-Pad. This allows the Player to be able to "Rollover" from opposite ends of the options list.
    - Similarly, the __Area Select__ Menu when Selecting a Sub-Game now allows both increasing and decreasing the World/Level Number separately.
- __In-Game Tracker Menus__
    - Each Sub-Game has its own Tracker that can display/list certain Items they have collected/unlocked. This can be done by pressing the `Select` Button on the controller to bring up the Tracker Menu, similarly to how pressing the `Start` Button brings up the Pause Menu.
    - A Tracker is also shown when selecting a Sub-Game on the Game Select Screen, which can display additional information such as __Boss Coins__ collected.
- __Continue Playing After World Boss__
    - Each Sub-Game now allows you to continue playing after having gone through the Ending Credits. __SMB1__ and __SMBLL__ already does this natively in some capacity, but other Sub-Games are now able to do the same.
    - Adjacently to the above, defeating a World Boss will roll you over to the next Available World Unlocked.
- __Final Level Locks__
    - The Final Level(s) for each Sub-Game is locked behind a Sub-Goal condition, which will require you to need to collect a certain number of `Boss Coins`. Attempting to enter a Final Level that is locked will boot the Player to the previous Level.
- __Titlescreen Skip__
    - Selecting a Sub-Game will immediately take you to the Play-Field, skipping the Titlescreen altogether.


## What are some additional Features of SMASWAP?
Currently, aside from everything previously described in the above sections, the only other Feature of __SMASWAP__ that is implemented is the ability to do __Offline Play__. This means that Items local to the Game that are placed locally in the Game's Locations are embedded into the Game. In other words, Local Items.


## FAQ and Known Issues

### FAQs
- Where is SMW?
    - Not currently implemented at this time. It *is* planned, it'll just take a while.
- Is \[Feature\] Implemented?
    - If it isn't listed in the above sections, you can assume it's either not implemented, or has been considered and put into the `ROADMAP` Dev File.
- Is there an External Tracker?
    - A Poptracker Pack has not yet been made, feel free to make one yourself, though. Additonally, there is currently no Universal Tracker support, so it had been disabled for now.
- What about the Non-SMW Versions of SMAS?
    - Other versions are considered, but not implemented. Refer to the `ROADMAP` for additional information.
- Can I bring this to an Archipelago Session?
    - Seeing as this is still an Alpha, I'd strongly recommend you don't, it'd make me and others feel bad if you do.
- I'm stuck in SMB2's 1-1 without Climb!
    - You can reach the Upper Cave Entrance with a well-placed Super Jump. You can further reach the Birdo Shortcut with a well-timed Jump even without Dash. Playing as Toad does make these maneuvers trickier, but they are still doable.

### Known Issues
- Due to the way the Transition from `Game Select Screen->Sub-Game Initialization` works under the hood, some tiles related to the Tracker may "disappear" during the fadeout.
- There *may* be some RAM that didn't get initialized properly due to Titlescreen Skipping.
- __Level Previews__ in __SMB1__ *might* be broken, this is due to the various shenanigans involved having to decouple the Hardmode Worlds and provide a "Princess-less" Final Level. There may be other factors that caused the Previews to break.
- Some Hardmode Levels may not be 1:1 accurate to the Vanilla Game, please report if you come across some. For example, 1x1 has Piranha Plants.
- Returning to the __Character Select Screen__ in __SMB2__ through __Exiting__ the Level may cause a little bit of weirdness. Still need to look into what RAM Addresses need to be accounted for.
- A minor graphical glitch may occur when pulling up the Pause Menu duing __SMB2__'s Credits, this is a vanilla bug, and only really happens for like one frame.
- Pulling up the Pause Menu or Tracker Menu in __SMB3__ may cause some black bars to appear at the top of the screen, this is just a side effect of a lot of code being run behind the scenes.
- The background for __Bowser's Castle__ in __SMB3__ can hitch during the insta-exit from not having enough __Boss Coins__. A proper locking mechanism is considered, but not yet implemented due to needing more research.