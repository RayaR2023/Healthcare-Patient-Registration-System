import customtkinter as ctk
from tkinter import messagebox

from src.services.patient_service import update_appointment


class EditAppointmentWindow(ctk.CTkToplevel):

    def __init__(self, parent, appointment, refresh_callback):

        super().__init__(parent)

        self.appointment = appointment
        self.refresh_callback = refresh_callback

        self.title("Edit Appointment")
        self.geometry("450x420")

        self.grab_set()

        labels = [
            "Date",
            "Time",
            "Reason",
            "Status",
            "Room"
        ]

        values = [
            appointment.appointment_date,
            appointment.appointment_time,
            appointment.appointment_reason,
            appointment.appointment_status,
            appointment.room_number
        ]

        self.entries = {}

        for i, (label, value) in enumerate(zip(labels, values)):

            ctk.CTkLabel(
                self,
                text=label
            ).grid(
                row=i,
                column=0,
                padx=15,
                pady=10,
                sticky="w"
            )

            entry = ctk.CTkEntry(
                self,
                width=250
            )

            entry.grid(
                row=i,
                column=1,
                padx=15,
                pady=10
            )

            entry.insert(
                0,
                str(value)
            )

            self.entries[label] = entry

        save = ctk.CTkButton(
            self,
            text="Save Changes",
            command=self.save
        )

        save.grid(
            row=6,
            column=0,
            columnspan=2,
            pady=20
        )

    def save(self):

        try:

            self.appointment.appointment_date = (
                self.entries["Date"].get().strip()
            )


            self.appointment.appointment_time = (
                self.entries["Time"].get().strip()
            )


            self.appointment.appointment_reason = (
                self.entries["Reason"].get().strip()
            )


            self.appointment.appointment_status = (
                self.entries["Status"].get().strip()
            )


            self.appointment.room_number = (
                self.entries["Room"].get().strip()
            )


            update_appointment(
                self.appointment
            )


            self.destroy()


            self.refresh_callback()


            messagebox.showinfo(
                "Success",
                "Appointment updated successfully."
            )


        except Exception as e:


            messagebox.showerror(
                "Error",
                f"Could not update appointment.\n\n{e}"
            )