import customtkinter as ctk

class PatientInfoFrame(ctk.CTkFrame):
    def __init__(self, parent):

        super().__init__(parent)

        self.patient_labels = {}

        self.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=20
        )

        title = ctk.CTkLabel(
            self,
            text="Patient Information",
            font=("Segoe UI", 22, "bold")
        )

        title.grid(
            row=0,
            column=0,
            columnspan=2,
            pady=(20, 30)
        )

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

                self,

                text=field + ":",

                font=("Segoe UI", 14, "bold"),

                anchor="w"

            )

            label.grid(

                row=index + 1,

                column=0,

                sticky="w",

                padx=30,

                pady=8

            )

            value = ctk.CTkLabel(

                self,

                text="",

                font=("Segoe UI", 14),

                anchor="w"

            )

            value.grid(

                row=index + 1,

                column=1,

                sticky="w",

                padx=20,

                pady=8

            )

            self.patient_labels[field] = value


    def display_patient(self, patient):

        self.patient_labels["First Name"].configure(
            text=patient.first_name
        )

        self.patient_labels["Last Name"].configure(
            text=patient.last_name
        )

        self.patient_labels["Date of Birth"].configure(
            text=patient.date_of_birth
        )

        self.patient_labels["Sex"].configure(
            text=patient.sex
        )

        self.patient_labels["Phone"].configure(
            text=patient.phone
        )

        self.patient_labels["Email"].configure(
            text=patient.email
        )

        self.patient_labels["Address"].configure(
            text=patient.address
        )

        self.patient_labels["Health Card"].configure(
            text=patient.health_card_number
        )

        self.patient_labels["Emergency Contact"].configure(
            text=patient.emergency_contact
        )

        self.patient_labels["Emergency Phone"].configure(
            text=patient.emergency_phone
        )

        self.patient_labels["Family Doctor"].configure(
            text=patient.family_doctor
        )

        self.patient_labels["Blood Type"].configure(
            text=patient.blood_type
        )

        self.patient_labels["Allergies"].configure(
            text=patient.allergies
        )

    def clear_information(self):
        for label in self.patient_labels.values():
            label.configure(text="")