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

        pages = {
            "Dashboard": "dashboard",
            "Patients": "patients",
            "Register Patient": "register_patient"
        }

        for text,page in pages.items():
            button = ctk.CTkButton(
                self,
                text = text,
                command = lambda p = page:
                    parent.show_page(p)
            )
            button.pack(
                fill = "x",
                padx =15,
                pady =8
            )