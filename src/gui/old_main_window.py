import customtkinter as ctk

from src.services.patient_service import (
    search_by_health_card,
    get_patient_appointments
)
from tkinter import messagebox 
from src.gui.patient_info_frame import PatientInfoFrame

class MainWindow(ctk.CTk):

    def search_patient(self):
        health_card = self.health_card_entry.get().strip()
        #ignore blank searches
        if health_card == "":
            return
        #search SQL Server
        patient = search_by_health_card(health_card)

        #if no patient exists, clear display
        if patient is None:
            self.clear_patient_information()
            messagebox.showerror(
                "Patient Not Found",
                "No patient was found with that Health Card Number. "
            )
            return
        #otherwise display patient
        self.display_patient(patient)

    def display_patient(self, patient):
        self.patient_info.display_patient(patient)
        appointments = get_patient_appointments(patient.patient_id)
        self.appointments_box.delete(
            "1.0",
            "end"
        )
        for appointment in appointments:
            line = (
                f"{appointment.AppointmentDate}"
                f"{appointment.AppointmentTime}  "
                f"{appointment.AppointmentReason}  "
                f"({appointment.AppointmentStatus})\n"

            )
            self.appointments_box.insert(
                "end",
                line
            )

    def clear_patient_information(self):
        self.patient_info.clear_information()

    def __init__(self):
        super().__init__()
        self.title("Healthcare Patient Registration System")
        self.geometry("1200x700")
        self.resizable(False, False)

        title = ctk.CTkLabel(
            self,
            text = "Healthcare Patient Registration System",
            font = ("Segoe UI", 28, "bold"),
            text_color= "red"
        )
        title.pack(pady=20)
        search_frame = ctk.CTkFrame(self)
        search_frame.pack(fill = "x", padx = 30, pady = 20)
        label = ctk.CTkLabel(
            search_frame,
            text = "Health Card Number"
        )
        label.grid(row=0, column=0, padx =15, pady = 20)

        self.health_card_entry= ctk.CTkEntry(
            search_frame,
            width = 250
        )
        self.health_card_entry.grid(row=0,column=1)

        search_button = ctk.CTkButton(
            search_frame,
            text = "Search",
            #telling Tkinter when user clicks search button, run the search_patient method
            command = self.search_patient
        )
        search_button.grid(row=0,column=2,padx=20)

        patient_frame = ctk.CTkFrame(self)
        #creates a large grey section underneath search bar
        patient_frame.pack(
            fill = "both",
            expand = True,
            padx=30,
            pady=20
        )
        patient_title = ctk.CTkLabel(
            patient_frame, 
            text = "Patient Information",
            font = ("Segoe UI", 22, "bold")
        )
        patient_title.grid(
            row = 0,
            column = 0,
            columnspan = 2,
            pady = (20,30)
        )

        #instead of manually writing every label, python will generate them:

        
        #we need labels whose text will change after a search:
        #create a dictionary:
        self.patient_labels = {}
        fields = [
            "Patient ID", 
            "First Name",
            "Last Name",
            "Date of Birth",
            "Sex",
            "Phone",
            "Email",
            "Address",
            "Health Card",
            "Emergency Contact",
            "Emergency Phone",
            "Family Doctor",
            "Blood Type",
            "Allergies"
        ] 

        for index, field in enumerate(fields):
            label = ctk.CTkLabel(
                patient_frame,
                text = field + ":",
                font = ("Segoe UI", 14, "bold"),
                anchor = "w"
            )
            label.grid(
                row = index+1,
                column = 0,
                sticky = "w",
                padx = 30,
                pady = 8
            )

            value = ctk.CTkLabel(
                patient_frame,
                text="",
                font = ("Segoe UI", 14),
                anchor = "w"
            )

            value.grid(
                row = index+1,
                column = 1,
                sticky = "w",
                padx = 20,
                pady=8
            )
            self.patient_labels[field] = value

        #self.patient_info = PatientInfoFrame(self)

        appointments_title = ctk.CTkLabel(
            patient_frame,
            text = "Appointments",
            font = ("Segoe UI", 20, "bold")
        )
        appointments_title.grid(
            row = 16,
            column = 0,
            sticky = "w",
            padx = 30,
            pady= (30,10)
        )

    #textbox:
        self.appointments_box = ctk.CTkTextbox(
            patient_frame,
            width = 600,
            height = 140
        )
        self.appointments_box.grid(
            row = 17,
            column = 0,
            columnspan = 2,
            padx = 30,
            pady =10
        )
        

