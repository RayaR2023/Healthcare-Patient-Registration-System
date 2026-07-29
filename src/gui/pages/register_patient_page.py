import customtkinter as ctk
from tkinter import messagebox

from src.models.patient import Patient
from src.services.patient_service import add_patient

class RegisterPatientPage(ctk.CTkFrame):
    def __init__(self, parent):

        super().__init__(parent)

        self.fields = {}

        title = ctk.CTkLabel(
            self,
            text="Register New Patient",
            font=("Segoe UI", 28, "bold")
        )

        title.pack(
            pady=20
        )


        fields = [
            "First Name",
            "Last Name",
            "Date of Birth",
            "Sex",
            "Phone",
            "Email",
            "Address",
            "Health Card Number",
            "Emergency Contact",
            "Emergency Phone",
            "Family Doctor",
            "Blood Type",
            "Allergies"
        ]


        form = ctk.CTkScrollableFrame(
            self,
            width = 600,
            height = 450
            )

        form.pack(
            padx=40,
            pady=10,
            fill = "both",
            expand = True
        )


        for index, field in enumerate(fields):

            label = ctk.CTkLabel(
                form,
                text=field
            )

            label.grid(
                row=index,
                column=0,
                padx=10,
                pady=8
            )


            entry = ctk.CTkEntry(
                form,
                width=300
            )

            entry.grid(
                row=index,
                column=1,
                padx=10,
                pady=8
            )


            self.fields[field] = entry


        button = ctk.CTkButton(
            self,
            text="Register Patient",
            command=self.register
        )

        button.pack(
            pady=10
        )


    def register(self):

        patient = Patient(

            self.fields["First Name"].get(),
            self.fields["Last Name"].get(),
            self.fields["Date of Birth"].get(),
            self.fields["Sex"].get(),
            self.fields["Phone"].get(),
            self.fields["Email"].get(),
            self.fields["Address"].get(),
            self.fields["Health Card Number"].get(),
            self.fields["Emergency Contact"].get(),
            self.fields["Emergency Phone"].get(),
            self.fields["Family Doctor"].get(),
            self.fields["Blood Type"].get(),
            self.fields["Allergies"].get()

        )


        new_patient = add_patient(patient)


        messagebox.showinfo(
            "Success",
            f"Patient registered successfully!\n Patient ID: {new_patient.patient_id}"
        )