import customtkinter as ctk
from tkinter import messagebox

from src.services.patient_service import (
    add_referral,
    get_all_departments
)


class AddReferralWindow(ctk.CTkToplevel):

    def __init__(self, parent, patient_id, refresh_callback):
        
        super().__init__(parent)

        self.patient_id = patient_id
        self.refresh_callback = refresh_callback

        self.title("Add Referral")
        self.geometry("550x650")

        self.transient(parent)
        self.grab_set()


        # =========================
        # Clinic
        # =========================

        ctk.CTkLabel(
            self,
            text="Referring Clinic"
        ).pack(pady=(15,5))


        self.clinic = ctk.CTkEntry(
            self,
            width=350
        )

        self.clinic.pack()



        # =========================
        # Date
        # =========================

        ctk.CTkLabel(
            self,
            text="Referral Date (YYYY-MM-DD)"
        ).pack(pady=(15,5))


        self.date = ctk.CTkEntry(
            self,
            width=350
        )

        self.date.pack()



        # =========================
        # Department
        # =========================

        ctk.CTkLabel(
            self,
            text="Department"
        ).pack(pady=(15,5))


        departments = get_all_departments()


        self.department_map = {}


        department_names = []


        for dept in departments:

            self.department_map[
                dept.DepartmentName
            ] = dept.DepartmentID


            department_names.append(
                dept.DepartmentName
            )


        self.department = ctk.CTkComboBox(
            self,
            values=department_names,
            width=350
        )

        self.department.pack()



        # =========================
        # Status
        # =========================

        ctk.CTkLabel(
            self,
            text="Status"
        ).pack(pady=(15,5))


        self.status = ctk.CTkEntry(
            self,
            width=350
        )

        self.status.pack()



        # =========================
        # Notes
        # =========================

        ctk.CTkLabel(
            self,
            text="Notes"
        ).pack(pady=(15,5))


        self.notes = ctk.CTkTextbox(
            self,
            width=350,
            height=100
        )

        self.notes.pack()



        # =========================
        # Save
        # =========================

        ctk.CTkButton(
            self,
            text="Save Referral",
            command=self.save
        ).pack(
            pady=25
        )



    def save(self):

        clinic = self.clinic.get().strip()

        referral_date = self.date.get().strip()

        department_name = self.department.get()

        status = self.status.get().strip()

        notes = self.notes.get(
            "1.0",
            "end"
        ).strip()



        if (
            clinic == ""
            or referral_date == ""
            or department_name == ""
        ):

            messagebox.showwarning(
                "Missing Information",
                "Please complete all required fields."
            )

            return



        try:

            add_referral(

                self.patient_id,

                clinic,

                referral_date,

                self.department_map[department_name],

                status,

                notes

            )


            self.refresh_callback()


            messagebox.showinfo(
                "Success",
                "Referral added successfully."
            )


            self.destroy()



        except Exception as e:

            messagebox.showerror(
                "Error",
                f"Could not add referral.\n\n{e}"
            )

    