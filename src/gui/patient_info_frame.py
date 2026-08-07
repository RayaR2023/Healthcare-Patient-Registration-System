import customtkinter as ctk

from src.gui.styles import *


class PatientInfoFrame(ctk.CTkFrame):

    def __init__(
        self,
        parent,
        edit_callback=None,
        delete_callback=None,
        export_callback = None
    ):

        super().__init__(parent)

        self.edit_callback = edit_callback
        self.delete_callback = delete_callback
        self.export_callback = export_callback

        self.configure(height=150)
        self.grid_propagate(False)

        self.patient_labels = {}

        # ==========================
        # Title
        # ==========================

        title = ctk.CTkLabel(
            self,
            text="Patient Information",
            font=TITLE_FONT
        )

        title.pack(
            pady=(5, 5)
        )

        content = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        content.pack(
            fill="both",
            expand=True,
            padx=20
        )

        fields = [

            ("Patient ID", "patient_id"),
            ("Name", "name"),
            ("DOB", "dob"),
            ("Sex", "sex"),
            ("Blood Type", "blood"),
            ("Phone", "phone"),
            ("Email", "email"),
            ("Health Card", "health"),
            ("Doctor", "doctor")

        ]

        for i, (label, key) in enumerate(fields):

            row = i // 3
            col = (i % 3) * 2

            ctk.CTkLabel(
                content,
                text=label + ":",
                font=LABEL_FONT
            ).grid(
                row=row,
                column=col,
                padx=5,
                pady=3,
                sticky="w"
            )

            value = ctk.CTkLabel(
                content,
                text="-",
                font=BODY_FONT
            )

            value.grid(
                row=row,
                column=col + 1,
                padx=5,
                pady=3,
                sticky="w"
            )

            self.patient_labels[key] = value

        # ==========================
        # Buttons
        # ==========================

        button_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        button_frame.pack(
            pady=8
        )


        # --------------------------
        # Edit Patient Button
        # --------------------------

        self.edit_button = ctk.CTkButton(
            button_frame,
            text="Edit Patient",
            width=120,
            height=30,
            command=self.edit_callback
        )

        self.edit_button.pack(
            side="left",
            padx=5
        )


        # --------------------------
        # Delete Patient Button
        # --------------------------

        self.delete_button = ctk.CTkButton(
            button_frame,
            text="Delete Patient",
            width=120,
            height=30,
            fg_color="#C62828",
            hover_color="#8E0000",
            command=self.delete_callback
        )

        self.delete_button.pack(
            side="left",
            padx=5
        )

        #Export patient report button:

        self.export_button = ctk.CTkButton(
            button_frame,
            text="Export Report",
            width=120,
            height=30,
            fg_color="#2E7D32",
            hover_color="#1B5E20",
            command=self.export_callback
        )

        self.export_button.pack(
            side="left",
            padx=5
        )

    def display_patient(self, patient):

        data = {

            "patient_id": patient.patient_id,
            "name": f"{patient.first_name} {patient.last_name}",
            "dob": patient.date_of_birth,
            "sex": patient.sex,
            "blood": patient.blood_type,
            "phone": patient.phone,
            "email": patient.email,
            "health": patient.health_card_number,
            "doctor": patient.family_doctor

        }

        for key, value in data.items():

            self.patient_labels[key].configure(
                text=value
            )

    def clear_information(self):

        for label in self.patient_labels.values():

            label.configure(
                text="-"
            )