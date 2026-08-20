# Super Mario All\-Stars \+ Super Mario World AP Randomizer Setup Guide
Most of the set-up for the __Super Mario All\-Stars \+ Super Mario World Archipelao Randomizer__ is fairly similar to other Custom SNES Games. Feel free to follow those or stick around for some of the __SMASWAP__\-Specific Instructions.

## Required Software

- [Archipelago, preferably 0.6.7 or newer](https://github.com/ArchipelagoMW/Archipelago/releases).
    - Downloading Archipelago will also include [SNI](https://github.com/alttpo/sni/releases), but may not include a __Mesen\-Compatible__ LUA Script.
- Software or Hardware capable of loading and playing SNES ROM Files. Anything not listed here is not gauranteed to work.
    - [Mesen 2.1](https://github.com/SourMesen/Mesen2/releases) or [Mesen CE](https://github.com/nesdev-org/MesenCE/releases) (Recommended)
        - This will require a Mesen-Compatible LUA Script, see [Mesen Setup](#mesen-setup) for more information.
    - [snes9x-rr](https://github.com/gocha/snes9x-rr/releases)
- Your SMASW ROM File, probably named `Super Mario All-Stars + Super Mario World (USA).sfc`

## Playing Setup
### Mesen Setup
1. If you haven't yet, download the `MesenSConnector.lua` file from the [SNI Repo](https://github.com/alttpo/sni). This can be done by navigating to the file in the SNI Github Repo and clicking the `Download raw file` button.
    1. Make a copy of the Mesen LUA Script and rename it to `Mesen2Connector.lua`. ___It is important that you store this somewhere you can easily find later___.
    2. Once you have the LUA Script somewhere safe, open it in a text editor of your choice. You can alternatively open the Script in Mesen itself to make the required edits.
    3. Change all instances of `emu.memType.cpuDebug` into `emu.memType.snesDebug` and save your changes. ___You'll only have to do this once as long as the edits have been saved___.
2. Once you have Mesen, open it up and navigate to `Debug->Settings` on the Menu. You will need to change a few options before the Script can be properly used.
    1. Navigate to the `Script Window` tab within `Debugger Settings`.
    2. Enable `Allow access to I/O and OS functions` and `Allow network access` to allow the Connector Script to communicate to the Client.
    3. Select the `OK` button to save your Settings. ___You'll only need to do the above procedure once after saving your settings___.
3. If you haven't yet, load your Generated ROM File inside Mesen.
4. Open the Script Window by navigating to `Debug->Script Window`.
5. Once the Script Window is opened, you may see an Example Script that gets run by default. You can select the `Stop Script` Button to disable it.
6. Inside the Script Window, Open up your `Mesen2Connector` LUA Script.
7. Run the LUA Script if it isn't already, just select the `Run Script` Button in the Script Window.