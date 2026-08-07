import customtkinter as ctk
from tkinter import ttk


class ReferralsFrame(ctk.CTkFrame):
    print("LOADED REFERRALS FRAME")
    def __init__(
        self,
        parent,
        add_callback=None,
        edit_callback=None,
        delete_callback=None
    ):

        super().__init__(parent)

        self.referrals = []
        self.selected_referral = None

        self.add_callback = add_callback
        self.edit_callback = edit_callback
        self.delete_callback = delete_callback

        # ==================================
        # Title
        # ==================================

        title = ctk.CTkLabel(
            self,
            text="Referrals",
            font=("Segoe UI", 18, "bold")
        )

        title.pack(
            anchor="w",
            padx=20,
            pady=(15, 10)
        )

        # ==================================
        # Buttons
        # ==================================

        button_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        button_frame.pack(
            fill="x",
            padx=20,
            pady=5
        )

        # ----------------------------
        # Add Button
        # ----------------------------

        self.add_button = ctk.CTkButton(
            button_frame,
            text="Add Referral",
            command=self.add_callback
        )

        self.add_button.pack(
            side="left",
            padx=5
        )

        # ----------------------------
        # Edit Button
        # ----------------------------

        self.edit_button = ctk.CTkButton(
            button_frame,
            text="Edit Referral",
            command=self.edit_callback
        )

        self.edit_button.pack(
            side="left",
            padx=5
        )

        # ----------------------------
        # Delete Button
        # ----------------------------

        self.delete_button = ctk.CTkButton(
            button_frame,
            text="Delete Referral",
            command=self.delete_callback
        )

        self.delete_button.pack(
            side="left",
            padx=5
        )

        # ==================================
        # Table
        # ==================================

        columns = (
            "ID",
            "Clinic",
            "Date",
            "Department",
            "Status",
            "Notes"
        )

        self.table = ttk.Treeview(
            self,
            columns=columns,
            show="headings",
            height=12
        )

        headings = {
            "ID": "ID",
            "Clinic": "Referring Clinic",
            "Date": "Referral Date",
            "Department": "Department",
            "Status": "Status",
            "Notes": "Notes"
        }

        widths = {
            "ID": 70,
            "Clinic": 220,
            "Date": 120,
            "Department": 180,
            "Status": 120,
            "Notes": 420
        }

        for column in columns:

            self.table.heading(
                column,
                text=headings[column]
            )

            self.table.column(
                column,
                width=widths[column],
                anchor="center"
            )

        self.table.column(
            "Notes",
            anchor="w"
        )

        self.table.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(5, 20)
        )

        self.table.bind(
            "<<TreeviewSelect>>",
            self.select_referral
        )

    # ==================================
    # Display
    # ==================================

    def display_referrals(self, referrals):

        for row in self.table.get_children():
            self.table.delete(row)

        self.selected_referral = None

        for referral in referrals:

            print("INSERTING:")
            print("Clinic:", referral.referring_clinic)
            print("Department ID:", referral.department_id)
            print("Department Name:", getattr(referral, "department_name", None))

            self.table.insert(
                "",
                "end",
                values=(
                    referral.referral_id,
                    referral.referring_clinic,
                    referral.referral_date,
                    referral.department_name,
                    referral.status,
                    referral.notes
                )
            )
            item = self.table.get_children()[-1]
            print("TREEVIEW VALUES:", self.table.item(item)["values"])
    # ==================================
    # Selection
    # ==================================

    def select_referral(self, event):

        selected = self.table.selection()

        if not selected:
            self.selected_referral = None
            return

        values = self.table.item(selected[0])["values"]

        from src.models.referral import Referral
        from src.services.patient_service import get_all_departments

        referral = Referral(
            values[0],      # ReferralID
            None,           # PatientID
            values[1],      # Referring Clinic
            values[2],      # Referral Date
            None,           # DepartmentID (filled below)
            values[4],      # Status
            values[5]       # Notes
        )

        # Save the department name
        referral.department_name = values[3]

        # Convert department name back to department ID
        departments = get_all_departments()

        for dept in departments:
            if dept.DepartmentName == values[3]:
                referral.department_id = dept.DepartmentID
                break

        self.selected_referral = referral
    # ==================================
    # Selected object
    # ==================================

    def get_selected_referral(self):

        return self.selected_referral