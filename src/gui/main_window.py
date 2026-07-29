import customtkinter as ctk
from tkinter import messagebox

from src.gui.sidebar import Sidebar
from src.gui.pages.dashboard_frame import DashboardFrame
from src.gui.pages.patient_page import PatientPage

from src.services.patient_service import (
    search_by_health_card,
    get_dashboard_statistics
)
from src.gui.pages.register_patient_page import RegisterPatientPage
from src.gui.edit_patient_window import EditPatientWindow
class MainWindow(ctk.CTk):

    def __init__(self):
        super().__init__()

        # ----------------------------
        # Window
        # ----------------------------

        self.title("Healthcare Patient Registration System")
        self.geometry("1400x850")
        self.resizable(True, True)

        # ----------------------------
        # Layout
        # ----------------------------

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # ----------------------------
        # Sidebar
        # ----------------------------

        self.sidebar = Sidebar(self)

        self.sidebar.grid(
            row=0,
            column=0,
            sticky="ns"
        )

        # ----------------------------
        # Content Area
        # ----------------------------

        self.content = ctk.CTkFrame(
            self,
            corner_radius=0
        )

        self.content.grid(
            row=0,
            column=1,
            sticky="nsew"
        )
        self.content.grid_rowconfigure(
            0,
            weight=1
        )

        self.content.grid_columnconfigure(
            0,
            weight=1
        )

        # ----------------------------
        # Pages
        # ----------------------------

        self.pages = {}

        self.pages["dashboard"] = DashboardFrame(
            self.content
        )

        self.pages["patients"] = PatientPage(
            self.content,
            self.search_patient
        )

        self.pages["register_patient"] = RegisterPatientPage(
            self.content
        )

        # ----------------------------
        # Dashboard Statistics
        # ----------------------------

        stats = get_dashboard_statistics()

        self.pages["dashboard"].load_statistics(
            stats
        )

        # ----------------------------
        # Show Dashboard
        # ----------------------------

        self.show_page("dashboard")

        

    # ==================================================
    # Page Navigation
    # ==================================================

    def show_page(self, page_name):

        for page in self.pages.values():
            page.pack_forget()

        self.pages[page_name].pack(
            fill="both",
            expand=True
        )

        self.update()

        print("WINDOW:", self.winfo_width(), self.winfo_height())
        print("CONTENT:", self.content.winfo_width(), self.content.winfo_height())
        print("PAGE:", self.pages[page_name].winfo_width(), self.pages[page_name].winfo_height())
    # ==================================================
    # Patient Search
    # ==================================================

    def search_patient(self, health_card):

        patient = search_by_health_card(
            health_card
        )

        if patient is None:

            self.pages["patients"].clear_information()

            messagebox.showerror(
                "Patient Not Found",
                "No patient was found with that Health Card Number."
            )

            return

        self.pages["patients"].display_patient(
            patient
        )
        self.current_patient = patient