import customtkinter as ctk


class ScrollableFrame(ctk.CTkScrollableFrame):

    def __init__(self,parent):

        super().__init__(
            parent,
            orientation="vertical"
        )

        self.grid_columnconfigure(
            0,
            weight=1
        )