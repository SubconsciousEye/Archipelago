from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld

from .options import option_groups #, option_presets


class SMASWWebWorld(WebWorld):
    game = "Super Mario All-Stars + Super Mario World"

    theme = "partyTime"
    setup_en = Tutorial(
        "Setup Guide for Multiworld",
        "An Expansive Guide for Setting Up Your SMAS+SMW Game for Randomization in The Archipelago MultiWorld!",
        "English",
        "setup_en.md",
        "setup/en",
        ["SubconsciousEye"],
    )

    tutorials = [setup_en]

    option_groups = option_groups
    #options_presets = option_presets
