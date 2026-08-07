import customtkinter as ctk
from tkinter import messagebox

from src.services.patient_service import add_appointment

class AddAppointmentWindow(ctk.CTkToplevel):
    def  __init__(self,parent,patient_id,refresh_callback):
        super().__init__(parent)
        self.transient(parent)
        self.grab_set()
        self.patient_id = patient_id
        self.refresh_callback = refresh_callback
        self.title("Add Appointment")
        self.geometry("450x700")

        title = ctk.CTkLabel(
            self,
            text = "Add Appointment",
            font= ("Segoe UI", 22,"bold")
        )

        title.pack(
            pady = 20
        )
        self.entries= {}
        fields = [
            "Date",
            "Time",
            "Reason",
            "Status",
            "Room"
        ]
        for field in fields:

            label = ctk.CTkLabel(
                self,
                text=field
            )

            label.pack(
                pady=(5,0)
            )


            entry = ctk.CTkEntry(
                self,
                width=250
            )

            entry.pack(
                pady=3
            )

            self.entries[field] = entry



        save_button = ctk.CTkButton(
            self,
            text="Save Appointment",
            command=self.save
        )

        save_button.pack(
            pady=25
        )



    def save(self):

        date = self.entries["Date"].get().strip()
        time = self.entries["Time"].get().strip()
        reason = self.entries["Reason"].get().strip()
        status = self.entries["Status"].get().strip()
        room = self.entries["Room"].get().strip()


        if not date or not time or not reason:

            messagebox.showwarning(
                "Missing Information",
                "Date, Time, and Reason are required."
            )

            return


        try:

            add_appointment(

                self.patient_id,

                date,

                time,

                reason,

                status,

                room

            )


            self.destroy()


            self.refresh_callback()


            messagebox.showinfo(
                "Success",
                "Appointment added successfully."
            )


        except Exception as e:

            messagebox.showerror(
                "Error",
                f"Could not add appointment.\n\n{e}"
            )