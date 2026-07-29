import customtkinter as ctk
from src.gui.patient_search_frame import PatientSearchFrame
from src.gui.patient_info_frame import PatientInfoFrame
from src.gui.appointments_frame import AppointmentsFrame
from src.gui.referrals_frame import ReferralsFrame
from src.gui.lab_results_frame import LabResultsFrame
from src.gui.documents_frame import DocumentsFrame
from src.services.patient_service import search_by_health_card

from src.services.patient_service import(
    get_patient_appointments,
    get_patient_referrals,
    get_patient_lab_results,
    get_patient_documents
)

class PatientPage(ctk.CTkFrame):

    def __init__(self, parent, search_function):

        super().__init__(parent)

        self.grid_columnconfigure(
            0,
            weight = 1
        )
        self.grid_rowconfigure(
            0, 
            weight= 0
        )

        self.grid_rowconfigure(
            1,
            weight=0
        )

        self.grid_rowconfigure(
            2,
            weight=1
        )
        self.search_frame = PatientSearchFrame(
            self,
            search_function
        )
        self.search_frame.grid(
            row = 0,
            column = 0,
            sticky = "ew",
            padx = 20,
            pady = 20
        )

        self.patient_info = PatientInfoFrame(
            self,
            edit_callback = self.open_edit_window
        )
        self.patient_info.grid(
            row =1,
            column =0,
            sticky = "ew",
            padx =20,
            pady = 10
        )
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=1)

        self.configure(fg_color="red")

        # -----------------------------
        # Tabs
        # -----------------------------

        self.tabs = ctk.CTkTabview(
            self
        )

        self.tabs.grid(
            row=2,
            column=0,
            sticky="nsew",
            padx=20,
            pady=20
        )

        print("PatientPage size:", self.winfo_width(), self.winfo_height())

        self.after(
            1000,
            lambda: print(
                "Tabs height:",
                self.tabs.winfo_height()
            )
        )

        # force tabview expansion
        self.tabs.grid_rowconfigure(
            0,
            weight=1
        )

        self.tabs.grid_columnconfigure(
            0,
            weight=1
        )


        self.tabs.add("Appointments")
        self.tabs.add("Referrals")
        self.tabs.add("Lab Results")
        self.tabs.add("Documents")

        appointment_tab = self.tabs.tab("Appointments")
        appointment_tab.grid_rowconfigure(
            0,
            weight=1
        )
        appointment_tab.grid_columnconfigure(
            0,
            weight=1
        )

        self.appointments = AppointmentsFrame(
            appointment_tab
        )

        self.appointments.grid(
            row=0,
            column=0,
            sticky="nsew"
        )



        # =============================
        # Referral Tab
        # =============================

        referral_tab = self.tabs.tab("Referrals")

        referral_tab.grid_rowconfigure(
            0,
            weight=1
        )

        referral_tab.grid_columnconfigure(
            0,
            weight=1
        )


        self.referrals = ReferralsFrame(
            referral_tab
        )

        self.referrals.grid(
            row=0,
            column=0,
            sticky="nsew"
        )



        # =============================
        # Lab Tab
        # =============================

        lab_tab = self.tabs.tab("Lab Results")

        lab_tab.grid_rowconfigure(
            0,
            weight=1
        )

        lab_tab.grid_columnconfigure(
            0,
            weight=1
        )


        self.lab_results = LabResultsFrame(
            lab_tab
        )

        self.lab_results.grid(
            row=0,
            column=0,
            sticky="nsew"
        )



        # =============================
        # Documents Tab
        # =============================

        documents_tab = self.tabs.tab("Documents")

        documents_tab.grid_rowconfigure(
            0,
            weight=1
        )

        documents_tab.grid_columnconfigure(
            0,
            weight=1
        )


        self.documents = DocumentsFrame(
            documents_tab
        )

        self.documents.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

            # =====================================
            # Display everything
            # =====================================

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
        
        print(self.tabs.get())
        self.lab_results.display_lab_results(
            labs
        )

        documents = get_patient_documents(
            patient.patient_id
        )

        self.documents.display_documents(
            documents
        )

    # =====================================
    # Clear everything
    # =====================================

    def clear_information(self):

        self.patient_info.clear_information()

        self.appointments.display_appointments([])

        self.referrals.display_referrals([])

        self.lab_results.display_lab_results([])

        self.documents.display_documents([])

    def open_edit_window(self):
        if not hasattr(self,"current_patient"):
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
        self.display_patient(patient)