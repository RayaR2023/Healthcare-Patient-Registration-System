import customtkinter as ctk

class PatientSearchFrame(ctk.CTkFrame):

    def __init__(
        self,
        parent,
        search_function
    ):
    
        super().__init__(
            parent
        )
        self.search_function = search_function

        self.label = ctk.CTkLabel(
            self,
            text = "Health Card Number"
        )
        self.label.grid(
            row = 0,
            column = 0,
            padx = 10,
            pady = 10
        )
        self.entry = ctk.CTkEntry(
            self,
            width = 250
        )
        self.entry.grid(
            row =0,
            column = 1,
            padx = 10,
            pady =10
        )
        self.button = ctk.CTkButton(
            self,
            text = "Search",
            command = self.search
        )
        self.button.grid(
            row = 0,
            column =2,
            padx = 10,
            pady = 10
        )

    def search(self):
        health_card = self.entry.get().strip()

        if health_card == "":
            return

        self.search_function(
            health_card
        )

    