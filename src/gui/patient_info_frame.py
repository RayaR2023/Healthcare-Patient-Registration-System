import customtkinter as ctk

class PatientInfoFrame(ctk.CTkFrame):
    def __init__(self, parent):

        super().__init__(parent)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(3, weight=1)

        self.patient_labels = {}

    

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

        field_pairs = [

            ("Patient ID", "Phone"),

            ("First Name", "Email"),

            ("Last Name", "Address"),

            ("Date of Birth", "Health Card"),

            ("Sex", "Blood Type"),

            ("Emergency Contact", "Family Doctor"),

            ("Emergency Phone", "Allergies")

        ]

        for row, (left_field, right_field) in enumerate(field_pairs):

            left_label = ctk.CTkLabel(

                self,

                text=left_field + ":",

                font=("Segoe UI", 14, "bold")

            )

            left_label.grid(

                row=row + 1,

                column=0,

                padx=(30,10),

                pady=10,

                sticky="w"

            )

            left_value = ctk.CTkLabel(

                self,

                text="",

                font=("Segoe UI", 14)

            )

            left_value.grid(

                row=row + 1,

                column=1,

                sticky="w"

            )

            self.patient_labels[left_field] = left_value

            right_label = ctk.CTkLabel(
                self,
                text = right_field + ":",
                font = ("Segoe UI", 14, "bold")
            )

            right_label.grid(
                row = row +1,
                column = 2,
                padx = (50,10),
                pady = 10,
                sticky = "w"
            )
            right_value = ctk.CTkLabel(
                self,
                text = "",
                font = ("Segoe UI", 14)
            )
            right_value.grid(
                row = row+1,
                column = 3,
                sticky = "w"
            )
            self.patient_labels[right_field] = right_value

        


    def display_patient(self, patient):

        self.patient_labels["Patient ID"].configure(
            text = patient.patient_id
        )

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