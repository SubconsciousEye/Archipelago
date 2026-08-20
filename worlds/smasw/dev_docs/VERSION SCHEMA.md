# SMASWAP Version Schema
## Quicklink
- [Version 1+ Schema](#v1-schema)
- [Version 0 Schema](#v0-schema)

## V1+ Schema
The Versioning Schema used for any formal Release Versions of v1.0 or higher will use the format `vXX.YY.ZZ_BUILD` for its fields.

The `XX` Field is considered the `Major` Version, and is usually updated only whenever there are large changes to the APWorld made, or if __Archipelago__ itself has any (breaking) changes/features in a future version that would warrant a Version Update. Compatibility with earlier and future `Major` Versions are not gauranteed to be preserved.

The `YY` Field is considered the `Minor` Version. Updating this number is only really used for new Features added into the APWorld, or if various Logic Changes are made that would warrant a Version Update. Compatibility with earlier `Minor` Versions and future `Minor` Versions should be preserved whenever possible.

The `ZZ` Field is considered the `Patch` Version. This will usually never get updated unless for any Bugfixes on either the Python-Side or the SNES-Side. Any changes here are fairly small, and should be both Backwards Compatible and Forwards Compatible with other Versions that only change the `Patch` Version.

The `BUILD` Field is special, it usually refers to `Pre-release` Versions, but can also be used to refer to `Unofficial` Custom Versions. The `BUILD` Field contains two digits as an Identifier, with the leftmost digit generally identifying the `Build Type` and the rightmost digit identifying the `Build Number` in a `Base32-like` format. The following table contains a listing of "Reserved" `Build Types` that may be used in Versioning:

| Digit Identifier | Primary Purpose |
| :---: | :---: |
| `A-` | Used for `Alpha Pre-releases` |
| `B-` | Used for `Beta Pre-releases` |
| `C-` | Used for `Release Candidates` |
| `R-` | Reserved Identifier |
| `U-` | Reserved Identifier |
| `W-` | Reserved Identifier |
| `X-` | Reserved Identifier |

Any Identifiers not listed in the above table are free to use, and may make use of the full two-digit identifier.

If the `BUILD` Field is left empty, you can assume that it's an __Official Release__ Version of SMASWAP. This Field is only really for visibility on the SMASW Title Screen.


## V0 Schema
The Versioning System for Pre-v1 Versions acts a little differently the the formal versioning system. Rather than being denoted as `vXX.YY.ZZ_BUILD`, this system uses `v00.XX.YY_ZZ` as its format. Version 0 is intended to be a __Permanent Alpha__ State of the SMASWAP Project, at least until it can be Formally Released as `v1.0.0`.

The `ZZ` Field takes the place of the `BUILD` Field, being identified with two digits of alphanumeric characters. Since it is unknown exactly how many `Alpha` Builds are needed for Version 0, ___the entire field makes use of the Base32-like identifiers___.

The remaining Fields act similarly to their original counterparts.