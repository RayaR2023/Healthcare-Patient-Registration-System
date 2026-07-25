import customtkinter as ctk


class ReferralsFrame(ctk.CTkFrame):

    def __init__(self,parent):

        super().__init__(parent)

        title = ctk.CTkLabel(
            self,
            text = "Referrals",
            font = ("Segoe UI", 18, "bold")
        )

        title.pack(
            fill = "both",
            expand = True,
            padx = 20,
            pady = (0,20)
        )