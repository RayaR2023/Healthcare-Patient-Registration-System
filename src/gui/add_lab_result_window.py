import customtkinter as ctk
from tkinter import messagebox

from src.services.patient_service import add_lab_result


class AddLabResultWindow(ctk.CTkToplevel):

    def __init__(self, parent, patient_id, refresh_callback):

        super().__init__(parent)


        self.patient_id = patient_id
        self.refresh_callback = refresh_callback


        self.title("Add Lab Result")
        self.geometry("550x650")


        self.grab_set()


        # Test Name

        ctk.CTkLabel(
            self,
            text="Test Name"
        ).pack(
            pady=(15,0)
        )


        self.test_name = ctk.CTkEntry(
            self,
            width=350
        )

        self.test_name.pack()



        # Test Date

        ctk.CTkLabel(
            self,
            text="Test Date (YYYY-MM-DD)"
        ).pack(
            pady=(15,0)
        )


        self.test_date = ctk.CTkEntry(
            self,
            width=350
        )

        self.test_date.pack()



        # Result

        ctk.CTkLabel(
            self,
            text="Result"
        ).pack(
            pady=(15,0)
        )


        self.result = ctk.CTkEntry(
            self,
            width=350
        )

        self.result.pack()



        # Notes

        ctk.CTkLabel(
            self,
            text="Notes"
        ).pack(
            pady=(15,0)
        )


        self.notes = ctk.CTkTextbox(
            self,
            width=350,
            height=120
        )

        self.notes.pack()



        # Save button

        ctk.CTkButton(
            self,
            text="Save Lab Result",
            command=self.save
        ).pack(
            pady=25
        )



    def save(self):

        add_lab_result(

            self.patient_id,

            self.test_name.get(),

            self.test_date.get(),

            self.result.get(),

            self.notes.get(
                "1.0",
                "end"
            ).strip()

        )


        self.refresh_callback()


        messagebox.showinfo(
            "Success",
            "Lab result added."
        )


        self.destroy()