import customtkinter as ctk

class Sidebar(ctk.CTkFrame):

    def __init__(self,parent):

        super().__init__(
            parent,
            width = 220,
            corner_radius=0
        )
        self.pack_propagate(False)

        title = ctk.CTkLabel(
            self,
            text="🏥 HPRMS",
            font=("Segoe UI", 22, "bold")
        )
        title.pack(
            pady = (25,35)
        )

        buttons = [
            "Dashboard",

            "Patients",

            "Appointments",

            "Referrals",

            "Lab Results",

            "Documents",

            "Reports"
        ]

        for name in buttons:
            button = ctk.CTkButton(
                self,
                text = name,
                height = 45,
                corner_radius=8
            )
            button.pack(
                fill = "x",
                padx =15,
                pady =8
            )