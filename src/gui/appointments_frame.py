import customtkinter as ctk

from tkinter import ttk

class AppointmentsFrame(ctk.CTkFrame):

    def __init__(
        self,
        parent,
        add_callback=None,
        edit_callback=None,
        delete_callback=None
    ):

        super().__init__(parent)
        self.appointments = []

        self.selected_appointment = None


        self.add_callback = add_callback
        self.edit_callback = edit_callback
        self.delete_callback = delete_callback


        # -------------------------
        # Title
        # -------------------------

        title = ctk.CTkLabel(
            self,
            text="Appointments",
            font=("Segoe UI",18,"bold")
        )

        title.pack(
            anchor="w",
            padx=20,
            pady=(15,10)
        )


        # -------------------------
        # Buttons
        # -------------------------

        self.button_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        self.button_frame.pack(
            fill="x",
            padx=20,
            pady=5
        )


        self.add_button = ctk.CTkButton(
            self.button_frame,
            text="Add Appointment",
            command=self.add_callback
        )

        self.add_button.pack(
            side="left",
            padx=5
        )


        self.edit_button = ctk.CTkButton(
            self.button_frame,
            text="Update Appointment",
            command=self.edit_callback
        )

        self.edit_button.pack(
            side="left",
            padx=5
        )


        self.delete_button = ctk.CTkButton(
            self.button_frame,
            text="Delete Appointment",
            command=self.delete_callback
        )

        self.delete_button.pack(
            side="left",
            padx=5
        )
        # =========================
        # Appointment Table
        # =========================

        columns = (
            "Date",
            "Time",
            "Reason",
            "Status",
            "Room"
        )

        self.table = ttk.Treeview(
            self,
            columns=columns,
            show="headings",
            height=10
        )

        for col in columns:

            self.table.heading(
                col,
                text=col
            )

            self.table.column(
                col,
                width=140,
                anchor="center"
            )

        self.table.column(
            "Reason",
            width=350
        )

        self.table.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0,20)
        )

        self.table.bind(
            "<<TreeviewSelect>>",
            self.select_appointment
        )

                # -------------------------
                # Appointment display
                # -------------------------

                



    def display_appointments(self, appointments):

        self.appointments = appointments

        self.selected_appointment = None

        for row in self.table.get_children():

            self.table.delete(row)

        for appointment in appointments:

            self.table.insert(
                "",
                "end",
                iid=str(appointment.appointment_id),
                values=(
                    appointment.appointment_date,
                    appointment.appointment_time,
                    appointment.appointment_reason,
                    appointment.appointment_status,
                    appointment.room_number
                )
            )

    def select_appointment(self, event):

        selection = self.table.selection()

        if not selection:

            self.selected_appointment = None
            return


        appointment_id = int(selection[0])


        for appointment in self.appointments:

            if appointment.appointment_id == appointment_id:

                self.selected_appointment = appointment

                print(
                    "Selected Appointment:",
                    appointment.appointment_id
                )

                return


    def get_selected_appointment(self):

       return self.selected_appointment

    
    