# src/gui/styles.py

# ===========================
# Application Colour Palette
# ===========================

PRIMARY = "#2E86AB"          # Healthcare blue
PRIMARY_DARK = "#1B4F72"

SECONDARY = "#5DADE2"

BACKGROUND = "#F4F6F7"

CARD_BACKGROUND = "#FFFFFF"

SUCCESS = "#58D68D"

WARNING = "#F5B041"

DANGER = "#E74C3C"

TEXT = "#1C2833"

TEXT_LIGHT = "#566573"


# ===========================
# Fonts
# ===========================

TITLE_FONT = (
    "Segoe UI",
    28,
    "bold"
)

HEADER_FONT = (
    "Segoe UI",
    20,
    "bold"
)

SUBTITLE_FONT = (
    "Segoe UI",
    15
)

BODY_FONT = (
    "Segoe UI",
    14
)

CARD_TITLE_FONT = (
    "Segoe UI",
    17,
    "bold"
)

CARD_VALUE_FONT = (
    "Segoe UI",
    32,
    "bold"
)

# ===========================
# Button Defaults
# ===========================

BUTTON_WIDTH = 140

BUTTON_HEIGHT = 35

BUTTON_RADIUS = 10

# ===========================
# Backwards Compatibility Fonts
# ===========================

LABEL_FONT = (
    "Segoe UI",
    13,
    "bold"
)

ENTRY_FONT = (
    "Segoe UI",
    13
)

BUTTON_FONT = (
    "Segoe UI",
    13,
    "bold"
)

# ===========================
# CustomTkinter Theme
# ===========================

def apply_theme():

    import customtkinter as ctk

    ctk.set_appearance_mode(
        "light"
    )

    ctk.set_default_color_theme(
        "blue"
    )