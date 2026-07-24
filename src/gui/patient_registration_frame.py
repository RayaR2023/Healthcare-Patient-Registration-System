#directly mirrors a hospital registration workflow:

import customtkinter as ctk

class PatientRegistrationFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.pack(
            fill = "both",
            expand = True
        )

        title = ctk.CTkLabel(
            self,
            text = "Register New Patient",
            font = ("Segoe UI", 24, "bold")
        )
        title.pack(pady =20)