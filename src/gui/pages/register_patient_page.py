import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime

from src.models.patient import Patient
from src.services.patient_service import add_patient, health_card_exists


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
            width=600,
            height=450
        )

        form.pack(
            padx=40,
            pady=10,
            fill="both",
            expand=True
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

        # ==============================
        # Validate required fields
        # ==============================

        required = [

            "First Name",
            "Last Name",
            "Date of Birth",
            "Health Card Number"

        ]


        for field in required:

            if self.fields[field].get().strip() == "":

                messagebox.showwarning(
                    "Missing Information",
                    f"{field} is required."
                )

                return



        # ==============================
        # Validate DOB
        # ==============================

        try:

            dob = datetime.strptime(
                self.fields["Date of Birth"].get(),
                "%Y-%m-%d"
            ).date()


        except ValueError:

            messagebox.showerror(
                "Invalid Date",
                "Date of Birth must use format YYYY-MM-DD."
            )

            return



        # ==============================
        # Create Patient Object
        # ==============================


        patient = Patient(

            self.fields["First Name"].get(),
            self.fields["Last Name"].get(),
            dob,
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

        if health_card_exists(
            self.fields["Health Card Number"].get()
        ):

            messagebox.showerror(
                "Duplicate Health Card",
                "A patient with this Health Card Number already exists."
            )

            return

        try:

            new_patient = add_patient(
                patient
            )


            self.clear_form()


            # update dashboard if available
            if hasattr(
                self.winfo_toplevel(),
                "refresh_dashboard"
            ):

                self.winfo_toplevel().refresh_dashboard()



            messagebox.showinfo(
                "Success",
                f"Patient registered successfully!\n\nPatient ID: {new_patient.patient_id}"
            )



        except Exception as e:

            messagebox.showerror(
                "Registration Failed",
                str(e)
            )



    def clear_form(self):

        for entry in self.fields.values():

            entry.delete(
                0,
                "end"
            )