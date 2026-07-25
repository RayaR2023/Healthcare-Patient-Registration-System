import customtkinter as ctk
from tkinter import messagebox
from src.gui.patient_search_frame import PatientSearchFrame
from src.gui.patient_info_frame import PatientInfoFrame
from src.services.patient_service import search_by_health_card
from src.gui.appointments_frame import AppointmentsFrame
from src.services.patient_service import get_patient_appointments
from src.gui.sidebar import Sidebar
from src.gui.referrals_frame import ReferralsFrame
from src.services.patient_service import get_patient_referrals
from src.gui.lab_results_frame import LabResultsFrame
from src.services.patient_service import get_patient_lab_results

class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.grid_columnconfigure(
            1,
            weight =1
        )
        self.grid_rowconfigure(
            0,
            weight =1
        )

        self.sidebar = Sidebar(
            self
        )
        self.sidebar.grid(
            row = 0,
            column =0,
            sticky = "ns"
        )

        self.content = ctk.CTkFrame(
            self
        )

        self.content.grid(
            row = 0,
            column = 1,
            sticky = "nsew",
            padx = 20,
            pady = 20
        )

        self.content.grid_columnconfigure(
            0,
            weight= 1
        )
        self.content.grid_rowconfigure(2, weight=1)
        self.content.grid_rowconfigure(3, weight=1)

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
            self.content,
            text = "Healthcare Patient Registration System",
            font = ("Segoe UI", 28,"bold")
        )
        title.grid(
            row = 0,
            column = 0,
            pady = 20
        )

        self.search_frame = PatientSearchFrame(
            self.content,
            self.search_patient
        )
        self.search_frame.grid(
            row = 1,
            column = 0,
            sticky = "ew",
            pady = 15
        )
        self.patient_info = PatientInfoFrame(
            self.content
        )

        self.patient_info.grid(
            row = 2,
            column = 0,
            sticky = "nsew",
            pady = 15
    
        )

        self.tabs = ctk.CTkTabview(
            self.content,
            height = 320
        )

        self.tabs.grid(
            row = 3,
            column = 0,
            sticky = "nsew",
            pady = 15
        )

        self.tabs.add("Appointments")
        self.tabs.add("Referrals")
        self.tabs.add("Lab Results")
        self.tabs.add("Documents")

        self.appointments= AppointmentsFrame(
            self.tabs.tab("Appointments")
        )
        self.appointments.pack(
            fill = "both",
            expand = True,
            padx = 10,
            pady = 10
        )

        self.referrals = ReferralsFrame(
            self.tabs.tab("Referrals")
        )

        self.referrals.pack(
            fill = "both",
            expand = True,
            padx =10,
            pady = 10
        )

        self.lab_results = LabResultsFrame(
            self.tabs.tab("Lab Results")
        )

        self.lab_results.pack(
            fill = "both",
            expand = True,
            padx =10,
            pady = 10
        )

        documents_label = ctk.CTkLabel(
            self.tabs.tab("Documents"),
            text = "Documents module coming soon",
            font = ("Segoe UI", 16)
        )

        documents_label.pack(pady = 40)
        
    def search_patient(self, health_card):
        patient = search_by_health_card(health_card)
        if patient is None:
            self.patient_info.clear_information()

            messagebox.showerror(
                "Patient Not Found",
                "No patient was found with that Health Card Number."
            ) 
            return
        self.patient_info.display_patient(patient)
        appointments = get_patient_appointments(
            patient.patient_id
        )
        self.appointments.display_appointments(
            appointments
        )

        referrals = get_patient_referrals(
            patient.patient_id
        )

        self.referrals.display_referrals(
            referrals
        )

        lab_results = get_patient_lab_results(
            patient.patient_id
        )
        self.lab_results.display_lab_results(
            lab_results
        )
