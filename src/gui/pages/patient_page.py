import customtkinter as ctk

from src.gui.patient_search_frame import PatientSearchFrame
from src.gui.patient_info_frame import PatientInfoFrame
from src.gui.appointments_frame import AppointmentsFrame
from src.gui.referrals_frame import ReferralsFrame
from src.gui.lab_results_frame import LabResultsFrame
from src.gui.documents_frame import DocumentsFrame

from src.services.patient_service import (
    search_by_health_card,
    get_patient_appointments,
    get_patient_referrals,
    get_patient_lab_results,
    get_patient_documents
)


class PatientPage(ctk.CTkFrame):

    def __init__(self, parent, search_function):

        super().__init__(parent)

        # Main layout
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=1)

        self.grid_columnconfigure(0, weight=1)


        # -------------------------
        # Search
        # -------------------------

        self.search_frame = PatientSearchFrame(
            self,
            search_function
        )

        self.search_frame.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=20,
            pady=20
        )


        # -------------------------
        # Patient info
        # -------------------------

        self.patient_info = PatientInfoFrame(
            self,
            edit_callback=self.open_edit_window
        )

        self.patient_info.grid(
            row=1,
            column=0,
            sticky="ew",
            padx=20,
            pady=10
        )


        # -------------------------
        # Tabs area
        # -------------------------

        self.tabs = ctk.CTkTabview(
            self
        )

        self.tabs.configure(
            height = 500
        )
        self.tabs.grid(
            row=2,
            column=0,
            sticky="nsew",
            padx=20,
            pady=20
        )


        self.tabs.add("Appointments")
        self.tabs.add("Referrals")
        self.tabs.add("Lab Results")
        self.tabs.add("Documents")


        # -------------------------
        # Create frames
        # -------------------------

        self.appointments = AppointmentsFrame(
            self.tabs.tab("Appointments")
        )

        self.appointments.pack(
            fill="both",
            expand=True,
            padx = 10,
            pady = 10
        )


        self.referrals = ReferralsFrame(
            self.tabs.tab("Referrals")
        )

        self.referrals.pack(
            fill="both",
            expand=True
        )


        self.lab_results = LabResultsFrame(
            self.tabs.tab("Lab Results")
        )

        self.lab_results.pack(
            fill="both",
            expand=True
        )


        self.documents = DocumentsFrame(
            self.tabs.tab("Documents")
        )

        self.documents.pack(
            fill="both",
            expand=True
        )


        self.current_patient = None



    # ============================
    # Display patient information
    # ============================

    def display_patient(self, patient):

        self.current_patient = patient


        self.patient_info.display_patient(
            patient
        )


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


        labs = get_patient_lab_results(
            patient.patient_id
        )

        self.lab_results.display_lab_results(
            labs
        )


        documents = get_patient_documents(
            patient.patient_id
        )

        self.documents.display_documents(
            documents
        )



    # ============================
    # Clear page
    # ============================

    def clear_information(self):

        self.patient_info.clear_information()

        self.appointments.display_appointments([])

        self.referrals.display_referrals([])

        self.lab_results.display_lab_results([])

        self.documents.display_documents([])



    # ============================
    # Edit
    # ============================

    def open_edit_window(self):

        if self.current_patient is None:
            return

        from src.gui.edit_patient_window import EditPatientWindow

        EditPatientWindow(
            self,
            self.current_patient,
            self.refresh_patient
        )



    def refresh_patient(self):

        patient = search_by_health_card(
            self.current_patient.health_card_number
        )

        self.display_patient(
            patient
        )