# SMASW/SMASU/SMASR Bank Addressing
A general overview of the SNES Banks and their purposes in the overall Randomizer.

It isn't exactly the most comprehensive.

| Bank Range | Purposes |
| :---: | :---: |
| `$80-$BF` | General Randomizer Infrastructure (Code/Data); General Vanilla Code/Data |
| `$C0-$CF` | Reserved for SMASW's Vanilla Data (GFX); SMW GFX and Music |
| `$D0-$D7` | SMW Decompressed GFX (Includes Mode7 and 2BPP GFX) |
| `$D6-$D7` | Potential other SMW GFX/Data Stuff |
| `$D8-$D9` | SMB1 Custom Level Palettes (8wlds\*4lvls\*2hrd\*2subs) |
| `$DA-$DB` | SMBLL Custom Level Palettes (Same as above, except less) |
| `$DC-$DF` | SMB2 Custom Level Palettes (10\*20 Rooms) |
| `$E0-$E3` | SMB3 Custom Level Palettes (Buffer for 96\*2 Levels) |
| `$E8-$EF` | SMW Custom Level Palettes (Full 0x200 Levels) |
| `$E4-$E7` | Reserved for potential other Randomizer Data |
| `$F0-$FF` | Not recommended for use |