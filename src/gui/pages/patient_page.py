import customtkinter as ctk
from tkinter import messagebox



from src.gui.patient_search_frame import PatientSearchFrame
from src.gui.patient_info_frame import PatientInfoFrame

from src.gui.appointments_frame import AppointmentsFrame
from src.gui.referrals_frame import ReferralsFrame
from src.gui.lab_results_frame import LabResultsFrame
from src.gui.documents_frame import DocumentsFrame


from src.gui.add_appointment_window import AddAppointmentWindow
from src.gui.add_lab_result_window import AddLabResultWindow
from src.gui.edit_lab_result_window import EditLabResultWindow
from src.gui.add_document_window import AddDocumentWindow


from src.services.patient_service import (
    search_by_health_card,
    get_patient_appointments,
    get_patient_referrals,
    get_patient_lab_results,
    get_patient_documents,
    delete_appointment,
    delete_referral,
    delete_document,
    delete_lab_result,
    delete_patient
)


from src.gui.scrollable_frame import ScrollableFrame
from src.gui.edit_referral_window import EditReferralWindow
from src.services.report_service import generate_patient_report

class PatientPage(ctk.CTkFrame):


    def __init__(self,parent,search_function):

        super().__init__(parent)


        self.current_patient = None


        # layout

        self.grid_columnconfigure(
            0,
            weight=1
        )

        self.grid_rowconfigure(
            0,
            weight=0
        )

        self.grid_rowconfigure(
            1,
            weight=0
        )

        self.grid_rowconfigure(
            2,
            weight=1
        )



        # ==========================
        # Search
        # ==========================

        self.search_frame = PatientSearchFrame(
            self,
            search_function
        )


        self.search_frame.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=20,
            pady=10
        )



        # ==========================
        # Patient Info
        # ==========================

        self.patient_info = PatientInfoFrame(
            self,
            self.open_edit_window,
            self.delete_current_patient,
            self.export_patient_report
        )


        self.patient_info.grid(
            row=1,
            column=0,
            sticky="ew",
            padx=20,
            pady=5
        )



        # ==========================
        # Tabs
        # ==========================


        self.tabs = ctk.CTkTabview(
            self
        )


        self.tabs.grid(
            row=2,
            column=0,
            sticky="nsew",
            padx=20,
            pady=10
        )


        for tab in [
            "Appointments",
            "Referrals",
            "Lab Results",
            "Documents"
        ]:
            self.tabs.add(tab)



        # ==========================
        # Appointment Tab
        # ==========================


        self.appointments_scroll = ScrollableFrame(
            self.tabs.tab("Appointments")
        )


        self.appointments_scroll.pack(
            fill="both",
            expand=True
        )


        self.appointments = AppointmentsFrame(
            self.appointments_scroll,
            self.open_add_appointment,
            self.open_edit_appointment,
            self.delete_selected_appointment
        )


        self.appointments.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )



        # ==========================
        # Referral Tab
        # ==========================


        self.referrals_scroll = ScrollableFrame(
            self.tabs.tab("Referrals")
        )


        self.referrals_scroll.pack(
            fill="both",
            expand=True
        )


        self.referrals = ReferralsFrame(
            self.referrals_scroll,
            self.open_add_referral,
            self.open_edit_referral,
            self.delete_selected_referral
        )


        self.referrals.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )



        # ==========================
        # Lab Tab
        # ==========================


        self.lab_scroll = ScrollableFrame(
            self.tabs.tab("Lab Results")
        )


        self.lab_scroll.pack(
            fill="both",
            expand=True
        )


        self.lab_results = LabResultsFrame(
            self.lab_scroll,
            self.open_add_lab_result,
            self.open_edit_lab_result,
            self.delete_selected_lab_result
        )


        self.lab_results.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )



        # ==========================
        # Documents Tab
        # ==========================


        self.documents_scroll = ScrollableFrame(
            self.tabs.tab("Documents")
        )


        self.documents_scroll.pack(
            fill="both",
            expand=True
        )


        self.documents = DocumentsFrame(
            self.documents_scroll,
            self.open_add_document,
            self.open_edit_document,
            self.delete_selected_document
        )


        self.documents.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )
        # ============================================
        # Disable all buttons until a patient is loaded
        # ============================================

        self.set_patient_loaded(False)



    # ==================================================
    # DISPLAY PATIENT
    # ==================================================


    def display_patient(self,patient):

        self.current_patient = patient


        self.patient_info.display_patient(
            patient
        )


        self.appointments.display_appointments(
            get_patient_appointments(
                patient.patient_id
            )
        )


        self.referrals.display_referrals(
            get_patient_referrals(
                patient.patient_id
            )
        )


        self.lab_results.display_lab_results(
            get_patient_lab_results(
                patient.patient_id
            )
        )


        self.documents.display_documents(
            get_patient_documents(
                patient.patient_id
            )
        )

        self.set_patient_loaded(True)



    def clear_information(self):

        self.patient_info.clear_information()

        self.appointments.display_appointments([])

        self.referrals.display_referrals([])

        self.lab_results.display_lab_results([])

        self.documents.display_documents([])

        self.current_patient = None
        self.set_patient_loaded(False)


    # ==================================================
    # PATIENT EDIT
    # ==================================================


    def open_edit_window(self):

        if self.current_patient is None:

            messagebox.showwarning(
                "No Patient",
                "Please search for and select a patient first."
            )

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

        if patient is None:

            self.clear_information()
            return


        self.display_patient(
            patient
        )



    # ==================================================
    # APPOINTMENTS
    # ==================================================


    def open_add_appointment(self):

        if self.current_patient is None:

            messagebox.showwarning(
                "No Patient",
                "Please search for a patient first."
            )

            return

        AddAppointmentWindow(
            self,
            self.current_patient.patient_id,
            self.refresh_appointments
        )


    def refresh_appointments(self):

        self.appointments.display_appointments(
            get_patient_appointments(
                self.current_patient.patient_id
            )
        )
        self.winfo_toplevel().refresh_dashboard()


    def open_edit_appointment(self):

        appointment = self.appointments.get_selected_appointment()


        if appointment is None:

            messagebox.showwarning(
                "No Appointment",
                "Select an appointment first."
            )

            return


        from src.gui.edit_appointment_window import EditAppointmentWindow


        EditAppointmentWindow(
            self,
            appointment,
            self.refresh_appointments
        )



    def delete_selected_appointment(self):

        appointment = self.appointments.get_selected_appointment()


        if appointment is None:

            messagebox.showwarning(
                "No Appointment",
                "Select an appointment first."
            )

            return


        confirm = messagebox.askyesno(
            "Delete Appointment",
            "Are you sure you want to delete this appointment?"
        )


        if not confirm:
            return


        delete_appointment(
            appointment.appointment_id
        )


        self.refresh_appointments()


        messagebox.showinfo(
            "Deleted",
            "Appointment deleted successfully."
        )



    # ==================================================
    # REFERRALS
    # ==================================================


    def open_add_referral(self):

        if self.current_patient is None:

            messagebox.showwarning(
                "No Patient",
                "Please search for a patient first."
            )

            return

        from src.gui.add_referral_window import AddReferralWindow

        AddReferralWindow(
            self,
            self.current_patient.patient_id,
            self.refresh_referrals
        )

    def refresh_referrals(self):

        self.referrals.display_referrals(
            get_patient_referrals(
                self.current_patient.patient_id
            )
        )
        self.winfo_toplevel().refresh_dashboard()


    def open_edit_referral(self):

        referral = self.referrals.get_selected_referral()

        if referral is None:

            messagebox.showwarning(
                "No Referral Selected",
                "Please select a referral first."
            )

            return

        EditReferralWindow(
            self,
            referral,
            self.refresh_referrals
        )


    def delete_selected_referral(self):

        referral = self.referrals.get_selected_referral()


        if referral is None:

            messagebox.showwarning(
                "No Referral",
                "Select a referral first."
            )

            return


        confirm = messagebox.askyesno(
            "Delete Referral",
            "Are you sure you want to delete this referral?"
        )


        if not confirm:
            return


        delete_referral(
            referral.referral_id
        )


        self.refresh_referrals()


        messagebox.showinfo(
            "Deleted",
            "Referral deleted successfully."
        )


    # ==================================================
    # LAB RESULTS
    # ==================================================


    def open_add_lab_result(self):

        if self.current_patient is None:

            messagebox.showwarning(
                "No Patient",
                "Please search for a patient first."
            )

            return

        AddLabResultWindow(
            self,
            self.current_patient.patient_id,
            self.refresh_lab_results
        )


    def refresh_lab_results(self):

        self.lab_results.display_lab_results(
            get_patient_lab_results(
                self.current_patient.patient_id
            )
        )
        self.winfo_toplevel().refresh_dashboard()


    def open_edit_lab_result(self):

        lab = self.lab_results.get_selected_lab()

        if lab is None:

            messagebox.showwarning(
                "No Lab Result",
                "Please select a lab result first."
            )

            return

        EditLabResultWindow(
            self,
            lab,
            self.refresh_lab_results
        )


    def delete_selected_lab_result(self):

        lab = self.lab_results.get_selected_lab()


        if lab is None:

            messagebox.showwarning(
                "No Lab Result",
                "Select a lab result first."
            )

            return


        confirm = messagebox.askyesno(
            "Delete Lab Result",
            "Are you sure you want to delete this lab result?"
        )


        if not confirm:
            return


        delete_lab_result(
            lab.result_id
        )


        self.refresh_lab_results()


        messagebox.showinfo(
            "Deleted",
            "Lab result deleted successfully."
        )



    # ==================================================
    # DOCUMENTS
    # ==================================================


    def open_add_document(self):

        if self.current_patient is None:

            messagebox.showwarning(
                "No Patient",
                "Please search for a patient first."
            )

            return

        AddDocumentWindow(
            self,
            self.current_patient.patient_id,
            self.refresh_documents
        )


    def refresh_documents(self):

        self.documents.display_documents(
            get_patient_documents(
                self.current_patient.patient_id
            )
        )
        self.winfo_toplevel().refresh_dashboard()


    def open_edit_document(self):

        document = self.documents.get_selected_document()

        if document is None:

            messagebox.showwarning(
                "No Document",
                "Please select a document first."
            )

            return

        from src.gui.edit_document_window import EditDocumentWindow

        EditDocumentWindow(
            self,
            document,
            self.refresh_documents
        )



    def delete_selected_document(self):

        document = self.documents.get_selected_document()


        if document is None:

            messagebox.showwarning(
                "No Document",
                "Select a document first."
            )

            return


        confirm = messagebox.askyesno(
            "Delete Document",
            "Are you sure you want to delete this document?"
        )


        if not confirm:
            return


        delete_document(
            document.document_id
        )


        self.refresh_documents()


        messagebox.showinfo(
            "Deleted",
            "Document deleted successfully."
        )

    def set_patient_loaded(self, loaded):

        state = "normal" if loaded else "disabled"

        #
        # Appointments
        #

        self.appointments.add_button.configure(state=state)
        self.appointments.edit_button.configure(state=state)
        self.appointments.delete_button.configure(state=state)

        #
        # Referrals
        #

        self.referrals.add_button.configure(state=state)
        self.referrals.edit_button.configure(state=state)
        self.referrals.delete_button.configure(state=state)

        #
        # Labs
        #

        self.lab_results.add_button.configure(state=state)
        self.lab_results.edit_button.configure(state=state)
        self.lab_results.delete_button.configure(state=state)

        #
        # Documents
        #

        self.documents.add_button.configure(state=state)
        self.documents.edit_button.configure(state=state)
        self.documents.delete_button.configure(state=state)

        #
        # Patient button
        #

        self.patient_info.edit_button.configure(state=state)
        self.patient_info.delete_button.configure(state=state)
        self.patient_info.export_button.configure(state=state)

    def delete_current_patient(self):

        if self.current_patient is None:

            messagebox.showwarning(
                "No Patient",
                "No patient is currently loaded."
            )

            return


        confirm = messagebox.askyesno(
            "Delete Patient",
            "Are you sure you want to delete this patient?\n\n"
            "This will permanently remove:\n"
            "- Patient information\n"
            "- Appointments\n"
            "- Referrals\n"
            "- Lab Results\n"
            "- Documents"
        )


        if not confirm:

            return


        try:

            delete_patient(
                self.current_patient.patient_id
            )


            # Clear current patient reference

            self.current_patient = None


            # Clear all UI information

            self.clear_information()


            # Disable buttons again

            self.set_patient_loaded(False)
            self.winfo_toplevel().refresh_dashboard()


            messagebox.showinfo(
                "Success",
                "Patient deleted successfully."
            )


        except Exception as e:

            messagebox.showerror(
                "Delete Error",
                str(e)
            )

    def export_patient_report(self):

        if self.current_patient is None:

            messagebox.showwarning(
                "No Patient",
                "Please search for a patient first."
            )

            return


        from src.services.report_service import generate_patient_report


        try:

            file_path = generate_patient_report(
                self.current_patient
            )


            messagebox.showinfo(
                "Report Exported",
                f"Patient report saved successfully.\n\nLocation:\n{file_path}"
            )


        except Exception as e:

            messagebox.showerror(
                "Export Failed",
                str(e)
            )