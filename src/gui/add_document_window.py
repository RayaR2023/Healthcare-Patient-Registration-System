import customtkinter as ctk
from tkinter import messagebox

from src.services.patient_service import add_document


class AddDocumentWindow(ctk.CTkToplevel):

    def __init__(self, parent, patient_id, refresh_callback):

        super().__init__(parent)

        self.patient_id = patient_id
        self.refresh_callback = refresh_callback

        self.title("Add Document")
        self.geometry("520x600")

        self.grab_set()


        # Document Type

        ctk.CTkLabel(
            self,
            text="Document Type"
        ).pack(pady=(20,5))


        self.document_type = ctk.CTkEntry(
            self,
            width=350
        )

        self.document_type.pack()



        # File Name

        ctk.CTkLabel(
            self,
            text="File Name"
        ).pack(pady=(20,5))


        self.file_name = ctk.CTkEntry(
            self,
            width=350
        )

        self.file_name.pack()



        # Upload Date

        ctk.CTkLabel(
            self,
            text="Upload Date (YYYY-MM-DD)"
        ).pack(pady=(20,5))


        self.upload_date = ctk.CTkEntry(
            self,
            width=350
        )

        self.upload_date.pack()



        # Uploaded By

        ctk.CTkLabel(
            self,
            text="Uploaded By"
        ).pack(pady=(20,5))


        self.uploaded_by = ctk.CTkEntry(
            self,
            width=350
        )

        self.uploaded_by.pack()



        # Button

        ctk.CTkButton(
            self,
            text="Save Document",
            command=self.save
        ).pack(pady=35)



    def save(self):

        if (
            self.document_type.get() == ""
            or self.file_name.get() == ""
            or self.upload_date.get() == ""
            or self.uploaded_by.get() == ""
        ):

            messagebox.showwarning(
                "Missing Information",
                "Please complete all fields."
            )

            return



        add_document(

            self.patient_id,

            self.document_type.get(),

            self.file_name.get(),

            self.upload_date.get(),

            self.uploaded_by.get()

        )


        self.refresh_callback()


        messagebox.showinfo(
            "Success",
            "Document added successfully."
        )


        self.destroy()