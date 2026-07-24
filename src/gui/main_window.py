import customtkinter as ctk

from src.gui.patient_search_frame import PatientSearchFrame
from src.gui.patient_info_frame import PatientInfoFrame


class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title(
            "Healthcare Patient Registration System"
        )

        self.geometry(
            "1200x750"
        )
        self.resizable(
            False,
            False
        )

        title = ctk.CTkLabel(
            self,
            text = "Healthcare Patient Registration System",
            font = ("Segoe UI", 28,"bold")
        )
        title.pack(
            pady = 20
        )

        self.search_frame = PatientSearchFrame(
            self,
            self.search_patient
        )
        self.search_frame.pack(
            padx = 30,
            pady = 20
        )
        self.patient_info = PatientInfoFrame(
            self
        )

        self.patient_info.pack(
            fill = "both",
            expand = True,
            padx =30,
            pady = 20
    
        )

    def search_patient(self, health_card):
        print(
            "Searching:",
            health_card
        )