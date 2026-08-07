import customtkinter as ctk
from tkinter import ttk


class DocumentsFrame(ctk.CTkFrame):

    def __init__(
        self,
        parent,
        add_callback=None,
        edit_callback=None,
        delete_callback=None
    ):

        super().__init__(parent)


        self.add_callback = add_callback
        self.edit_callback = edit_callback
        self.delete_callback = delete_callback


        self.documents = []
        self.selected_document = None


        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)



        # TITLE

        ctk.CTkLabel(
            self,
            text="Documents",
            font=("Segoe UI",18,"bold")
        ).grid(
            row=0,
            column=0,
            sticky="w",
            padx=20,
            pady=(15,5)
        )

        # BUTTONS

        button_frame = ctk.CTkFrame(self)

        button_frame.grid(
            row=0,
            column=1,
            padx=20,
            pady=10
        )


        # -------------------------
        # Add Button
        # -------------------------

        self.add_button = ctk.CTkButton(
            button_frame,
            text="Add Document",
            command=self.add_callback
        )

        self.add_button.pack(
            side="left",
            padx=5
        )


        # -------------------------
        # Edit Button
        # -------------------------

        self.edit_button = ctk.CTkButton(
            button_frame,
            text="Edit Document",
            command=self.edit_callback
        )

        self.edit_button.pack(
            side="left",
            padx=5
        )


        # -------------------------
        # Delete Button
        # -------------------------

        self.delete_button = ctk.CTkButton(
            button_frame,
            text="Delete Document",
            command=self.delete_callback
        )

        self.delete_button.pack(
            side="left",
            padx=5
        )

                


        # TABLE FRAME

        table_frame = ctk.CTkFrame(self)

        table_frame.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky="nsew",
            padx=20,
            pady=10
        )


        table_frame.grid_rowconfigure(0,weight=1)
        table_frame.grid_columnconfigure(0,weight=1)



        columns = (
            "Document ID",
            "Type",
            "File Name",
            "Upload Date",
            "Uploaded By"
        )



        self.table = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings"
        )



        for col in columns:

            self.table.heading(
                col,
                text=col
            )


        self.table.column(
            "Document ID",
            width=100
        )

        self.table.column(
            "Type",
            width=200
        )

        self.table.column(
            "File Name",
            width=250
        )

        self.table.column(
            "Upload Date",
            width=220
        )

        self.table.column(
            "Uploaded By",
            width=180
        )



        self.table.grid(
            row=0,
            column=0,
            sticky="nsew"
        )



        scrollbar = ttk.Scrollbar(
            table_frame,
            orient="horizontal",
            command=self.table.xview
        )


        scrollbar.grid(
            row=1,
            column=0,
            sticky="ew"
        )


        self.table.configure(
            xscrollcommand=scrollbar.set
        )



        self.table.bind(
            "<ButtonRelease-1>",
            self.select_document
        )




    def display_documents(self, documents):

        self.documents = documents
        self.selected_document = None


        for item in self.table.get_children():

            self.table.delete(item)



        for doc in documents:

            self.table.insert(
                "",
                "end",
                values=(
                    doc.document_id,
                    doc.document_type,
                    doc.file_name,
                    doc.upload_date,
                    doc.uploaded_by
                )
            )




    def select_document(self,event):

        selected = self.table.selection()


        if not selected:

            self.selected_document=None
            return



        values = self.table.item(
            selected[0]
        )["values"]



        document_id = values[0]


        for doc in self.documents:

            if doc.document_id == document_id:

                self.selected_document = doc

                print(
                    "Selected Document:",
                    doc.document_id
                )

                return




    def get_selected_document(self):

        return self.selected_document