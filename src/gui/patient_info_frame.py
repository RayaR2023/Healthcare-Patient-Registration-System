import customtkinter as ctk

class PatientInfoFrame(ctk.CTkFrame):
    def __init__(self, parent, edit_callback = None):

        super().__init__(parent)
        self.configure(
            height = 360
        )
        self.grid_propagate(False)
        self.edit_callback = edit_callback
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=2)


        self.patient_labels = {}

    

        title = ctk.CTkLabel(
            self,
            text="Patient Information",
            font=("Segoe UI", 22, "bold")
        )

        title.grid(
            row=0,
            column=0,
            columnspan=4,
            pady=(10,10)
        )

        left_fields = [

            ("Patient ID","Patient ID"),

            ("Name","Name"),

            ("Date of Birth","Date of Birth"),

            ("Sex","Sex"),

            ("Blood Type","Blood Type"),

            ("Family Doctor","Family Doctor")

        ]

        right_fields = [

            ("Phone","Phone"),

            ("Email","Email"),

            ("Address","Address"),

            ("Health Card","Health Card"),

            ("Emergency Contact","Emergency Contact"),

            ("Emergency Phone","Emergency Phone"),

            ("Allergies","Allergies")

        ]

        for row, (display_text, key) in enumerate(left_fields):

            label = ctk.CTkLabel(

                self,
                text= display_text + ":",
                font=("Segoe UI", 14, "bold"),
                anchor = "w"

            )

            label.grid(

                row=row + 1,

                column=0,

                sticky = "w",

                padx =(40,15),

                pady = 3

            )

            value = ctk.CTkLabel(

                self,

                text="",

                font=("Segoe UI", 14),

                anchor = "w"

            )

            value.grid(

                row=row + 1,

                column=1,

                sticky="w",

                padx = (0,40),

                pady = 3

            )

            self.patient_labels[key] = value

            #----Right Side-------------

        for row, (display_text, key) in enumerate(right_fields):

            label = ctk.CTkLabel(
                self,
                text=display_text + ":",
                font=("Segoe UI", 14, "bold"),
                anchor="w"
            )

            label.grid(
                row=row + 1,
                column=2,
                sticky="w",
                padx=(40, 15),
                pady=3
            )

            value = ctk.CTkLabel(
                self,
                text="",
                font=("Segoe UI", 14),
                anchor="w"
            )

            value.grid(
                row=row + 1,
                column=3,
                sticky="w",
                padx=(0, 40),
                pady=3
            )

            self.patient_labels[key] = value
        self.edit_button = ctk.CTkButton(
            self,
            text = "Edit Patient",
            command = self.edit_callback
        )
        self.edit_button.grid(
            row = 20,
            column = 0,
            columnspan = 4,
            pady = 5
        )

        


    def display_patient(self, patient):

        self.patient_labels["Patient ID"].configure(
            text = patient.patient_id
        )

        self.patient_labels["Name"].configure(
            text=f"{patient.first_name} {patient.last_name}"
        )

        self.patient_labels["Date of Birth"].configure(
            text=patient.date_of_birth
        )

        self.patient_labels["Sex"].configure(
            text=patient.sex
        )

        self.patient_labels["Blood Type"].configure(
            text=patient.blood_type
        )

        self.patient_labels["Family Doctor"].configure(
            text=patient.family_doctor
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

        self.patient_labels["Allergies"].configure(
            text=patient.allergies
        )

    def clear_information(self):
        for label in self.patient_labels.values():
            label.configure(text="")