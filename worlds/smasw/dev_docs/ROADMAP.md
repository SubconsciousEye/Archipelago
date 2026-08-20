# SMASWAP Roadmap
This document contains a listing of __Features__, which holds various information such as _Status_ and _Descriptions_ and such. Additional Features may be added and changed as time goes by.
## V1.0.0 Requirements
- [ ] [Proper APWorld Logic](#proper-apworld-logic)
- [ ] [APWorld Python Cleanup](#apworld-python-cleanup)
- [ ] [SMW Implementation](#smw-implementation)
- [ ] [Base SMAS Randomizer Core](#base-smas-randomizer-core)
- [ ] [Poptracker Pack \& Features](#poptracker-pack--features)
## Additional Features
- [ ] [SMASU \/ SMASR Patching](#smasu--smasr-patching)
- [ ] Warp Zone Logic and Shuffle Options
- [ ] World \/ Level Shuffle
- [ ] Egghunt Goals
- [ ] Red Coins \(Non-SMW\) \/ Dragon Coins \(SMW Only\)
- [ ] Other Miscellaneous SMW Checks \(Moon\, Bonus Blocks\, etc\)
- [ ] Blocksanity \/ Grass-sanity
- [ ] \-Sanities \(Various\)
- [ ] Luigi Game \(SMB1 \/ SMBLL\)
- [ ] SMB1\-SMBLL Parity
- [ ] Custom Palettes
- [ ] Custom Player Graphics \& Palettes

# Features
This section contains a list of __Features__ and various fields related to how difficult implementing it would be.

- __Priority__ - Priority of the Feature, V1 Features are considered _two-levels higher_ than Additional Features.
- __Difficulty__ - A rough measure of how much effort and code (if any) this feature requires for implementation.
- __STATUS__ - Self-Explanatory. Either `Unimplemented`, `Researching`, `Works In Progress`, or `DONE`

__Priorities__ range from `Very High`, `High`, `Medium`, `Low`, and `Very Low`

__Difficulties__ range from `Very Hard`, `High`, `Medium`, `Easy`, and `Very Easy`

## Proper APWorld Logic
| Priority | Difficulty | STATUS |
| :---: | :---: | :---: |
| Very High | Hard | Unimplemented |

As of the ___First Public Alpha Build___, __Power-Ups Logic__ and __Health Logic__ are bare-bones and not fully implemented.

So far, only ___hard requirements___ are currently implemented, which corresponds to the **Super Star** Logic Difficulty Setting.
It is quite important to get some more-refined Logic implemented so we can extend the playerbase.

While adding new logic rules wouldn't be too difficult, we may also want to implement __Logic Tricks__ per Sub-Game to allow for more robust settings to the Player.

For the sake of ease, we'll focus on a set amount of __Difficulty Choices__ for the YAML Options.

- __Mushroom__ - Fairly easy Logic, recommended for those new to __SMASWAP__ or __Randomizers__.
- __Flower__ - Corresponds to "Low-Intermediate" Logic, this difficulty expects the Player to have played Mario Games to some degree of proficiency (e.g. SMW's Spinjump usage on non-standard enemies).
- __Feather__ - Corresponds to "Intermediate" Logic, this difficulty usually expects some obscure-but-easy-to-execute tricks or some amount of damage-boosting.
- __Super Star__ - Corresponds to "Advanced" Logic, this difficulty is generally for Super Players as it may involve a lot of deaths or near-frame-perfect execution.

Each Sub-Game will have its own `Difficulty Option`, which will determine how the logic behaves, as well as automatically enabling any (future) Tricks corresponding to that Difficulty Tag.

The main `SMASW Difficulty` Option will take precedence over individual Sub-Games if it is set at a Logic Difficulty higher than the one in the given Sub-Game's Option.


## APWorld Python Cleanup
| Priority | Difficulty | STATUS |
| :---: | :---: | :---: |
| Very High | Hard | Unimplemented |

The current Pre-V1 version of the APWorld's Python is a huge mess, all things considered.

Things *work*, but it's either a lot of copy-pasted/duplicated code, or written in strange ways to allow for data to be written for the SNES Patch.

This process will likely take a long while until everything is refactored.

Should anybody wish to tackle sections of this, they should ensure that __Generated Outputs__ should at least match pre-refactor, ***ESPECIALLY*** in regards to determinism.


## SMW Implementation
| Priority | Difficulty | STATUS |
| :---: | :---: | :---: |
| High | Medium | Researching |

There's technically a lot that needs to be done for this.

A lot of Subfeatures are needed to be implemented before this can fully take off.

### Decompressed Graphics (GFX)
| Priority | Difficulty | STATUS |
| :---: | :---: | :---: |
| Medium | Medium | Researching |

This is more of a Python-Side process than it is an SNES-Side one.

Decompressing the GFX is needed for a number of Subfeatures, and will especially be needed for SMW's Custom Players and Pause-Tracker Menus.

Some Mode7 stuff is a bit more difficult to figure out, and we need to slightly adjust the Vanilla SMW Decompressor to account for any (de)compressed GFX.

### Starting Area Location
| Priority | Difficulty | STATUS |
| :---: | :---: | :---: |
| Medium | Medium | Researching |

SMW will get a `World Key Progression` Option that will determine how unlocking the Sub-Game is handled.
| Name | Value | Behavior |
| :---: | :---: | :---: |
| `Game Unlock` | 0 | A single Key will lock SMW, picking it up unlocks it. |
| `World Area Keys` | 4 | Each World has its own Starting Location that can be unlocked. |
| `Progressive World Keys` | 6 | Starting Locations are unlocked sequentially. |

With this, Players can choose to either Start at a specified World from the Game Select Menu, or Return to their last saved Location.

Some modifications to the World Maps will be necessary in order to properly handle this.

The Layer 2 Tilemap is compressed, whereas the Layer 1 Tilemap is uncompressed. We can "cheat" for the Layer 2 Tilemap by utilizing Event ID 0, which is effectively unused in SMW. Event Tiles for Layer 2 is stored uncompressed, so it really is just a matter of finding the correct location(s) to store the newer tiles to update the Tilemaps.

Beyond just updating the Tilemapping, we'll also allow the Player to access the `Top Secret Area` Level at these designated locations, which will require some additional work due to how the game handles assigning Level IDs for the Level Tiles.

Further notes to be transferred to here later, some scratchpad ASM has already been written.

### Pause-Tracker Menus
| Priority | Difficulty | STATUS |
| :---: | :---: | :---: |
| Medium | Hard | Researching |

#### Levels
Figuring out the Pause Menu for In-Level processing is a bit tricky, in part due to Mode 7 Bosses existing.

SMAS usually clears out the OAM whenever the Pause Menu is pulled up, we can perform a similar operation for SMW's In-Level Pause Menu.

Unfortunately, the various Mode 7 Boss Levels may use the OAM for "Backgrounds" and sometimes even "Foregrounds" since Mode 7 is a Background Layer itself.

As a result, we may need to restructure OAM a little for these cases, as well as needing to define a range of OAM Slots to clear out for the Menu.

Even with some of these tricks, there may not be enough free OAM Slots to draw our Pause Menu in some Mode 7 Arenas.

For these cases, we can probably get around this by using the Layer 3 (2BPP) mode to handle our tiling. This will involve needing to mess with some cases where the game will switch between SNES Video Mode 1 to Video Mode 7. We'll also need to deal with the Palette for the Layer 3 stuff.

The other hurdle we would need to overcome is how to handle the Windowing for this, we can probably Python-Copy snippets from SMW's "Display Message" operation to handle our own special-case stuff for the Pause Menu.

Some (old) notes, may need to be updated later:
```
b282a6: ldy.w #$00e4
b282b6: cpy.w #$0104

Reznor, Iggy, Larry: $0200 OAM (Full Erase for Reznor)
Morton, Ludwig, Roy: $0300 OAM (start at like $0310)
Wendy, Lemmy: Normal Level OAM, Full Erase as always
Bowser: Start at $0240 OAM, end at $03bc
```

Implementing a Tracker Menu isn't possible with the VRAM Restrictions that we have.

#### Overworld Map
Tackling the Pause Menu for the Overworld Map is actually super easy, especially since, technically, it already exists in the SMASW Game! We'll just need to readjust a few tilemapping and options to encompass the traditional SMAS Pause Menu stuff, but it's pretty much all there.

We may also want to remove/repurpose the "Save Prompt" that appears after completing certain Levels, since it'll be a bit redundant with our new Pause Menu.

The Tracker Menu, on the other hand, can simply repurpose the "Lives Exchange" Menu that only exists in 2-Player Games, which is no longer possible with our Randomizer. We could probably also use OAM Slots for a more easily visible Tracker, like how we handle the SMAS In-Game Trackers.

The only real difficulty here is needing to use Python to handle the GFX stuff and *maybe* the Tracker Palette.

### Everything Else
| Priority | Difficulty | STATUS |
| :---: | :---: | :---: |
| Medium | Hard | Unimplemented |

The remaining stuff for the V1 SMW Implementation is primarily just things such as Items and Locations stuff, general Randomizer-related aspects. It shouldn't be too difficult to get them into the game, aside from writing the Logic.

Location IDs should follow a similar structure to how the other Sub-Games handle their Locations, particularly __SMB2\/SMB3__.

Like the other Sub-Games, the Ending Credits should also allow the player to bring up the Pause Menu and be able to resume playing. Handling the Menu there isn't too difficult since there isn't much going on.

Proposed Location IDs, assuming each Byte is a Level ID, and each Level ID has up to 8 Bits:
| Offset | Purpose |
| :---: | :---: |
| Bit 0 | Level Clear (Normal Exit) |
| Bit 1 | Level Clear (Secret Exit) |
| Bit 2 | All Dragon Coins Collected |
| Bit 3 | 3-Up Moon Collected |
| Bit 4 | Secret 1-Up Mushroom Collected |
| Bit 5 | 30-Coin Bonus Block Collected |

`Switch Palace Switches Pressed` will be considered `Normal Exits`, and `Special World Autumn Koopa Change` will be considered the `30-Coin Bonus Block` Check on `Yoshi's House`.


## Base SMAS Randomizer Core
| Priority | Difficulty | STATUS |
| :---: | :---: | :---: |
| Very High | Medium | Works In Progress |

This is mainly here for posterity purposes, as most of the __Randomizer Core__ has already been figured out and implemented to some degree.

There are, however, still a few SNES-Side things that needs to be covered, as well as a couple other Randomizer Features.

- [ ] [Filler Items Handling (SNES-Side)](#filler-items-handling)
- [ ] [Erase / Resync File Data (SNES and Client)](#erase--resync-file-data)
- [ ] [Title Screen Sub-Game Demos (Option for Hiding or Showing, Available Sub-Games Only)](#title-screen-sub-game-demos)
- [ ] [SMB3 Non-Essential Treasure Chests (Bro Fights, Mushroom Houses, Secret Chests...)](#smb3-non-essential-treasure-chests)
- [ ] [Warp Zone Behavior Options and Fixes](#warp-zone-behavior-options-and-fixes)
- [ ] [Proper "Require N Boss Coins" Message for all Sub-Games](#proper-require-n-boss-coins-message)
- [ ] [Ensure AP Core Functionalities (Item Links, Same-Slot Co-Op, Remote Items...)](#ensure-ap-core-functionalities)

### Filler Items Handling
| Priority | Difficulty | STATUS |
| :---: | :---: | :---: |
| Very High | Medium | Works In Progress |

As of the ___First Public Alpha Build___, no __Filler Items__ are properly implemented into the Game, being replaced by __Empty Item__.

Part of the difficulty with this is figuring out what to do when receiving an Item while a certain Sub-Game is not in play. This isn't much of an issue for certain Fillers such as the __1\-Ups__ and __Reserve Inventory Items__, but other Items such as the __Coins__ can be a little annoying.

We fortunately do have a __Unified Save File Buffer__ to handle some of these, but it may not be applicable depending on how we want to handle things. Trap Items are another consideration for concern.

What kind of Filler Items are available is subject to change.

### Erase / Resync File Data
| Priority | Difficulty | STATUS |
| :---: | :---: | :---: |
| Very High | Very Hard | Researching |

Figuring out a decent system to handle "Refreshing" the Save File is quite difficult. Since all Sub-Games share and handle the same Items Received protocols, this can be somewhat volatile to necessitate a rebuild.

Both the SNES and the SNI Client will need to communicate with each other for each step of the Resync Process. We would need to reset the Save File to its Initial State, then handle the Items, then any Locations we need to set.

### Title Screen Sub-Game Demos
| Priority | Difficulty | STATUS |
| :---: | :---: | :---: |
| High | Hard | Researching |

It is intended that the __Title Screen Demos__ are shown while the player waits on the __SMASW Title Screen__. This does not currently happen as of the __First Public Alpha Build__ due to a few minor intricacies.

The way these Demos work in Vanilla is that it loads up the respective Sub-Game to run the sequence. It also treats the "Currently Selected File" as if it were brand new during this stage. We will also need to prevent items from being received during the Title Screen sequence, and additionally fix up any other requirements in order to get it to function correctly.

__SMB1__ and __SMBLL__ both have a Playback that works by loading _the actual level_ into the scene, which can pose an issue if we do Level Shuffle. Additionally, the Demo Playback is too short for the music to play in full.

__SMB2__ and __SMB3__ both have their Title Screens handled in a completely self-contained manner, so we don't need to make any real adjustments to them beyond making sure they work.

__SMW__ also have a Demo Playback Sequence like __SMB1LL__. Unlike __SMB1LL__, the level that is loaded is completely unique to the Title Screen itself.

Beyond the SNES-Side implementation, we will also provide the Option to `Disable` these `Title Screen Sequences`. This is mainly for those that want to play in a "Mystery Seed" setting. Furthermore, we will only allow the `Available Sub-Games` to have their sequences run.

### SMB3 Non-Essential Treasure Chests
| Priority | Difficulty | STATUS |
| :---: | :---: | :---: |
| Very High | Medium | Works In Progress |

__SMB3__ has quite a few places where the player can receive a Treasure from a Chest. Opening a Chest technically counts as a Level Clear, causing the current Panel or Map Sprite to be destroyed. Ther are a few spots where these Chests are ***hard required*** for completing the Level, usually only in Worlds 7 and 8.

Currently in the __First Public Alpha Build__, only the **Essential Treasure Chests** are implemented.

The biggest challenge is getting all the Chests to fit within the designated area for __SMB3__'s Level IDs, especially with how the __Map Hammer Bros__ can move around the map (for `Bro-Sanity` Checks). Some Level IDs are reserved for Secret Chests (such as 1-3's Whistle) or World-Specific checks (Blue Mushroom Houses shared with the Koopaling Airship Levels). We should ideally not need more than 100 Hammer Bro Spots, even less if we decide to properly contain these Bros within certain areas of the Map (see World 6).

We can also repurpose the 4 Secret Chest Levels for the Whistle Fire Bro (World 2) Spots, since the Bros can never cross the Palm Tree Tile, while the Player *can*.

There are only 22 Regular Mushroom Houses, which can also limit how many Bro Spots we actually have. Refer to `_smb3_bro_panelspots` for more information on both.

Although not Chests themselves, the Princess Letters can also give the Player a Treasure, which should also be implemented into v1 of the Randomizer.

### Warp Zone Behavior Options and Fixes
| Priority | Difficulty | STATUS |
| :---: | :---: | :---: |
| High | Medium | Researching |

As of the __First Public Alpha Build__, Warp Zones don't function correctly.

For __SMB1__ and __SMBLL__, the way the Warp Zones are handled is super weird, there are a bunch of conditions and other identifiers that determine what kind of Warp Zone it is and where it sends you to. Some of these Warp Zones can even repeat with another Warp Zone. We would need to create a new Warp Zone System to allow for proper handling in the future for `Warp Zone Shuffle` and `Warp Zone Logic`.

The Warp Zones in __SMB2__ are thankfully a lot simpler, although they are limited to 7 entries, 1 per World.

__SMB3__ makes use of the Warp Whistle to take the Player to the Warp Zone in World 9. The way it is handled there is fairly self-contained, so nothing new really needs to happen.

`Warp Zone Behavior` Options dictate what __World Keys__ are needed to actually use the Warp Zone. The options available are `Unrestricted`, `Source Key Only`, `Destination Key Only`, and `Source and Destination Keys` as requirements to utilize a Warp. Not having the required Key will simply warp you back to the original World you came from.

### Proper "Require N Boss Coins" Message
| Priority | Difficulty | STATUS |
| :---: | :---: | :---: |
| Very High | Medium | Researching |

The difficulty mainly boils down to finding a good spot to place the message.

__SMB1__, __SMBLL__, and __SMB2__ all have a Level Preview that we could slot a message inside, although it may be tricky to do with how little space there is.

__SMB3__ doesn't really have a good way to show a dedicated message beyond forcing the Player to enter a "Level" and booting them out after the message is displayed (kind of like the World Castle messages after a Koopaling Airship is on the Map). We fortunately have an Unused Map Sprite we can repurpose for this, and we'll just need to find space for a Level to be taken to.

__SMW__ has an Intro Level we can repurpose for its `Boss Coins` requirement message, nothing new there beyond a couple fixes and forcing the level load.

### Ensure AP Core Functionalities
| Priority | Difficulty | STATUS |
| :---: | :---: | :---: |
| Very High | Medium | Works In Progress |

Pretty self-explanatory here. `Same-Slot Co-Op` and `Remote Items` technically rely on the same thing to generally function properly.


## Poptracker Pack \& Features
| Priority | Difficulty | STATUS |
| :---: | :---: | :---: |
| Very High | Very Hard | Unimplemented |

Creating a Poptracker Pack will likely take a huge amount of effort and time to complete. Autotracking will require some work to the Game to handle SNES\<\-\>Client related procedures.


## SMASU \/ SMASR Patching
| Priority | Difficulty | STATUS |
| :---: | :---: | :---: |
| High | Very Hard | Unimplemented |

While a lot of the SNES ASM can be easily down-ported for the Non-SMW Versions of the SMAS Family, there are still a number of hurdles that will need to be overcome. In our case, __SMASU__ will refer to the original, USA Version of `Super Mario All-Stars` released for the SNES; whereas __SMASR__ will refer to the 25th Anniversary Version released for the Wii.

Currently, the main developer, SubconsciousEye, only possesses the USA Version of `Super Mario All-Stars + Super Mario World` and the Wii Re-Release Version of `Super Mario All-Stars`.

Figuring out how to extract and restore the SNES Game from the Wii Version will take some time and effort in order to make it ready for Patching.

__SMASW__ and __SMAS__ both have different Base-Filesizes, with __SMASW__ being 2.5MB and __SMAS__ being 2MB respectively. This also means that anything that exists in the upper 0.5MB Range of __SMASW__ likely either doesn't exist (such as SMW-Specific stuff), or has been moved\/modified from its original placement in __SMAS__.