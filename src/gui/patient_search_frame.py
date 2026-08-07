import customtkinter as ctk

from src.gui.styles import *


class PatientSearchFrame(ctk.CTkFrame):

    def __init__(
        self,
        parent,
        search_function
    ):

        super().__init__(parent)

        self.search_function = search_function

        self.configure(
            corner_radius=12
        )

        # --------------------------
        # Title
        # --------------------------

        title = ctk.CTkLabel(
            self,
            text="Patient Search",
            font=TITLE_FONT
        )

        title.pack(
            pady=(15, 5)
        )

        subtitle = ctk.CTkLabel(
            self,
            text="Search by Ontario Health Card Number",
            font=BODY_FONT
        )

        subtitle.pack(
            pady=(0, 15)
        )

        # --------------------------
        # Search Row
        # --------------------------

        search_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        search_frame.pack(
            pady=(0, 20)
        )

        self.entry = ctk.CTkEntry(
            search_frame,
            width=350,
            placeholder_text="Example: HC123456789"
        )

        self.entry.pack(
            side="left",
            padx=(0, 15)
        )

        self.entry.bind(
            "<Return>",
            lambda event: self.search()
        )

        self.button = ctk.CTkButton(
            search_frame,
            text="Search",
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            command=self.search
        )

        self.button.pack(
            side="left"
        )

    def search(self):

        health_card = self.entry.get().strip()

        if not health_card:
            return

        self.search_function(
            health_card
        )