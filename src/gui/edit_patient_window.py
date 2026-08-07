import customtkinter as ctk
from tkinter import messagebox
from src.models.patient import Patient
from src.services.patient_service import (
    update_patient, 
    delete_patient as remove_patient
)
from src.utils.validators import (
    is_valid_date,
    is_valid_email,
    is_valid_phone,
    is_not_empty
)

class EditPatientWindow(ctk.CTkToplevel):

    def __init__(self, parent, patient, refresh_callback):
        super().__init__(parent)
        self.patient = patient
        self.refresh_callback = refresh_callback
        self.title("Edit Patient")
        self.geometry("600x720")
        self.resizable(False,False)
        self.grab_set()

        title = ctk.CTkLabel(
            self,
            text = "Edit Patient",
            font = ("Segoe UI", 24, "bold")
        )
        title.pack(pady = 20)

        self.entries = {}
        form = ctk.CTkScrollableFrame(
            self,
            width = 520,
            height = 520
        )

        form.pack(
            fill = "both",
            expand = True,
            padx = 20
        )
        fields = [
            ("First Name", patient.first_name),

            ("Last Name", patient.last_name),

            ("Date of Birth", patient.date_of_birth),

            ("Sex", patient.sex),

            ("Phone", patient.phone),

            ("Email", patient.email),

            ("Address", patient.address),

            ("Health Card Number", patient.health_card_number),

            ("Emergency Contact", patient.emergency_contact),

            ("Emergency Phone", patient.emergency_phone),

            ("Family Doctor", patient.family_doctor),

            ("Blood Type", patient.blood_type),

            ("Allergies", patient.allergies)
        ]

        for row, (label_text, value) in enumerate(fields):
            label = ctk.CTkLabel(
                form,
                text = label_text
            )
            label.grid(
                row = row,
                column =0,
                padx =10,
                pady = 8,
                sticky = "w"
            )

            entry = ctk.CTkEntry(
                form,
                width = 300
            )
            entry.insert(
                0,
                "" if value is None else str(value)
            )

            entry.grid(
                row =row,
                column = 1,
                padx =10,
                pady =8
            )
            self.entries[label_text] = entry
        save_button = ctk.CTkButton(
            self,
            text = "Save Changes",
            command = self.save
        )
        save_button.pack(
            pady = 20
        )
        delete_button = ctk.CTkButton(
            self,
            text = "Delete Patient",
            fg_color="darkred",
            hover_color="red",
            command = self.delete_patient
        )
        delete_button.pack(
            pady = (0,20)
        )

    def save(self):

        first_name = self.entries["First Name"].get().strip()
        last_name = self.entries["Last Name"].get().strip()
        dob = self.entries["Date of Birth"].get().strip()
        sex = self.entries["Sex"].get().strip()
        phone = self.entries["Phone"].get().strip()
        email = self.entries["Email"].get().strip()
        address = self.entries["Address"].get().strip()
        health_card = self.entries["Health Card Number"].get().strip()
        emergency_contact = self.entries["Emergency Contact"].get().strip()
        emergency_phone = self.entries["Emergency Phone"].get().strip()
        family_doctor = self.entries["Family Doctor"].get().strip()
        blood_type = self.entries["Blood Type"].get().strip()
        allergies = self.entries["Allergies"].get().strip()

        # ==========================
        # Required fields
        # ==========================

        if (
            not is_not_empty(first_name)
            or not is_not_empty(last_name)
            or not is_not_empty(dob)
            or not is_not_empty(health_card)
        ):

            messagebox.showwarning(
                "Missing Information",
                "First Name, Last Name, Date of Birth, and Health Card Number are required."
            )

            return

        # ==========================
        # Date
        # ==========================

        if not is_valid_date(dob):

            messagebox.showwarning(
                "Invalid Date",
                "Date of Birth must be in YYYY-MM-DD format."
            )

            return

        # ==========================
        # Email
        # ==========================

        if email != "" and not is_valid_email(email):

            messagebox.showwarning(
                "Invalid Email",
                "Please enter a valid email address."
            )

            return

        # ==========================
        # Phone
        # ==========================

        if phone != "" and not is_valid_phone(phone):

            messagebox.showwarning(
                "Invalid Phone",
                "Phone number must contain 10 digits."
            )

            return

        if emergency_phone != "" and not is_valid_phone(emergency_phone):

            messagebox.showwarning(
                "Invalid Emergency Phone",
                "Emergency phone number must contain 10 digits."
            )

            return

        updated_patient = Patient(

            first_name=first_name,
            last_name=last_name,
            date_of_birth=dob,
            sex=sex,
            phone=phone,
            email=email,
            address=address,
            health_card_number=health_card,
            emergency_contact=emergency_contact,
            emergency_phone=emergency_phone,
            family_doctor=family_doctor,
            blood_type=blood_type,
            allergies=allergies,
            patient_id=self.patient.patient_id

        )

        update_patient(updated_patient)

        messagebox.showinfo(
            "Success",
            "Patient updated successfully."
        )

        self.refresh_callback()

        self.destroy()

    def delete_patient(self):
        answer = messagebox.askyesno(
            "Delete Patient",
            "Are you sure you want to permanently delete this patient?"
        )
        if not answer:
            return

        try:
            remove_patient(
                self.patient.patient_id
            )
            messagebox.showinfo(
                "Deleted",
                "Patient deleted successfully"
            )
            self.destroy()
            self.refresh_callback()
            self.master.winfo_toplevel().refresh_dashboard()
        except Exception as e:
            messagebox.showerror(
                "Delete Failed",
                str(e)
            )