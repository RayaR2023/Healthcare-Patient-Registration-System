import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime

from src.services.patient_service import update_document



class EditDocumentWindow(ctk.CTkToplevel):

    def __init__(
        self,
        parent,
        document,
        refresh_callback
    ):

        super().__init__(parent)


        self.document = document
        self.refresh_callback = refresh_callback


        self.title("Edit Document")
        self.geometry("550x650")


        self.grab_set()



        # DOCUMENT TYPE

        ctk.CTkLabel(
            self,
            text="Document Type"
        ).pack(
            pady=(15,0)
        )


        self.document_type = ctk.CTkEntry(
            self,
            width=350
        )

        self.document_type.pack()


        self.document_type.insert(
            0,
            document.document_type
        )



        # FILE NAME

        ctk.CTkLabel(
            self,
            text="File Name"
        ).pack(
            pady=(15,0)
        )


        self.file_name = ctk.CTkEntry(
            self,
            width=350
        )

        self.file_name.pack()


        self.file_name.insert(
            0,
            document.file_name
        )



        # UPLOAD DATE

        ctk.CTkLabel(
            self,
            text="Upload Date (YYYY-MM-DD)"
        ).pack(
            pady=(15,0)
        )


        self.upload_date = ctk.CTkEntry(
            self,
            width=350
        )

        self.upload_date.pack()


        # only show date, not time

        if document.upload_date:

            self.upload_date.insert(
                0,
                str(document.upload_date)[:10]
            )



        # UPLOADED BY

        ctk.CTkLabel(
            self,
            text="Uploaded By"
        ).pack(
            pady=(15,0)
        )


        self.uploaded_by = ctk.CTkEntry(
            self,
            width=350
        )

        self.uploaded_by.pack()


        self.uploaded_by.insert(
            0,
            document.uploaded_by
        )



        # BUTTON

        ctk.CTkButton(
            self,
            text="Save Changes",
            command=self.save
        ).pack(
            pady=30
        )




    def save(self):


        try:

            upload_date = datetime.strptime(
                self.upload_date.get(),
                "%Y-%m-%d"
            )


        except ValueError:


            messagebox.showerror(
                "Invalid Date",
                "Please enter date as YYYY-MM-DD"
            )

            return



        self.document.document_type = (
            self.document_type.get()
        )


        self.document.file_name = (
            self.file_name.get()
        )


        self.document.upload_date = upload_date


        self.document.uploaded_by = (
            self.uploaded_by.get()
        )



        update_document(
            self.document
        )

        messagebox.showinfo(
            "Success",
            "Document updated."
        )

        self.destroy()

        self.refresh_callback()