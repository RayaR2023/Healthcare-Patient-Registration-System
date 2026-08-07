import customtkinter as ctk
from tkinter import messagebox

from src.services.patient_service import update_lab_result


class EditLabResultWindow(ctk.CTkToplevel):

    def __init__(self, parent, lab_result, refresh_callback):

        super().__init__(parent)


        self.lab_result = lab_result
        self.refresh_callback = refresh_callback


        self.title("Edit Lab Result")
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

        self.test_name.insert(
            0,
            lab_result.test_name
        )



        # Test Date

        ctk.CTkLabel(
            self,
            text="Test Date"
        ).pack(
            pady=(15,0)
        )


        self.test_date = ctk.CTkEntry(
            self,
            width=350
        )

        self.test_date.pack()


        self.test_date.insert(
            0,
            str(lab_result.test_date)
        )



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


        self.result.insert(
            0,
            lab_result.result
        )



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


        self.notes.insert(
            "1.0",
            lab_result.notes
        )



        ctk.CTkButton(
            self,
            text="Save Changes",
            command=self.save
        ).pack(
            pady=25
        )



    def save(self):

        self.lab_result.test_name = self.test_name.get()

        self.lab_result.test_date = self.test_date.get()

        self.lab_result.result = self.result.get()

        self.lab_result.notes = self.notes.get(
            "1.0",
            "end"
        ).strip()


        update_lab_result(
            self.lab_result
        )


        messagebox.showinfo(
            "Success",
            "Lab result updated."
        )

        self.destroy()

        self.refresh_callback()