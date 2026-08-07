import customtkinter as ctk
from tkinter import messagebox

from src.services.patient_service import (
    get_all_departments,
    update_referral
)


class EditReferralWindow(ctk.CTkToplevel):

    def __init__(self, parent, referral, refresh_callback):

        super().__init__(parent)

        self.referral = referral
        self.refresh_callback = refresh_callback

        self.title("Edit Referral")
        self.geometry("550x650")

        self.transient(parent)
        self.grab_set()

        # =====================================
        # Departments
        # =====================================

        departments = get_all_departments()

        self.department_map = {}
        self.id_to_name = {}

        department_names = []

        for dept in departments:

            self.department_map[dept.DepartmentName] = dept.DepartmentID
            self.id_to_name[dept.DepartmentID] = dept.DepartmentName

            department_names.append(
                dept.DepartmentName
            )

        # =====================================
        # Referring Clinic
        # =====================================

        ctk.CTkLabel(
            self,
            text="Referring Clinic"
        ).pack(pady=(15, 5))

        self.clinic = ctk.CTkEntry(
            self,
            width=350
        )

        self.clinic.pack()

        # =====================================
        # Referral Date
        # =====================================

        ctk.CTkLabel(
            self,
            text="Referral Date (YYYY-MM-DD)"
        ).pack(pady=(15, 5))

        self.date = ctk.CTkEntry(
            self,
            width=350
        )

        self.date.pack()

        # =====================================
        # Department
        # =====================================

        ctk.CTkLabel(
            self,
            text="Department"
        ).pack(pady=(15, 5))

        self.department = ctk.CTkComboBox(
            self,
            values=department_names,
            width=350
        )

        self.department.pack()

        # =====================================
        # Status
        # =====================================

        ctk.CTkLabel(
            self,
            text="Status"
        ).pack(pady=(15, 5))

        self.status = ctk.CTkEntry(
            self,
            width=350
        )

        self.status.pack()

        # =====================================
        # Notes
        # =====================================

        ctk.CTkLabel(
            self,
            text="Notes"
        ).pack(pady=(15, 5))

        self.notes = ctk.CTkTextbox(
            self,
            width=350,
            height=120
        )

        self.notes.pack()

        # =====================================
        # Load Existing Data
        # =====================================

        self.clinic.insert(
            0,
            referral.referring_clinic
        )

        self.date.insert(
            0,
            str(referral.referral_date)
        )

        # Use department name if available,
        # otherwise convert DepartmentID -> name.

        if hasattr(referral, "department_name"):

            self.department.set(
                referral.department_name
            )

        else:

            self.department.set(
                self.id_to_name.get(
                    referral.department_id,
                    ""
                )
            )

        self.status.insert(
            0,
            referral.status
        )

        self.notes.insert(
            "1.0",
            referral.notes
        )

        # =====================================
        # Save Button
        # =====================================

        ctk.CTkButton(
            self,
            text="Save Changes",
            command=self.save
        ).pack(
            pady=25
        )

    def save(self):

        department_name = self.department.get().strip()

        if department_name == "":

            messagebox.showwarning(
                "Missing Information",
                "Please select a department."
            )

            return

        self.referral.referring_clinic = (
            self.clinic.get().strip()
        )

        self.referral.referral_date = (
            self.date.get().strip()
        )

        self.referral.department_id = (
            self.department_map[department_name]
        )

        self.referral.department_name = (
            department_name
        )

        self.referral.status = (
            self.status.get().strip()
        )

        self.referral.notes = (
            self.notes.get(
                "1.0",
                "end"
            ).strip()
        )

        try:

            update_referral(
                self.referral
            )

            self.destroy()

            self.refresh_callback()

            messagebox.showinfo(
                "Success",
                "Referral updated successfully."
            )

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )