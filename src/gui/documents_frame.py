import customtkinter as ctk

class DocumentsFrame(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(parent)

        title = ctk.CTkLabel(
            self,
            text = "Patient Documents",
            font = ("Segoe UI", 18, "bold")
        )
        title.pack(
            anchor = "w",
            padx = 20,
            pady = (15,10)
        )

        self.table = ctk.CTkTextbox(
            self,
            width = 900,
            height = 220
        )

        self.table.pack(
            fill = "both",
            expand = True,
            padx = 20,
            pady = (0,20)
        )


    def display_documents(self, documents):

        self.table.delete(
            "1.0",
            "end"
        )

        header = (
            f"{'Type':<25}"
            f"{'File':<30}"
            f"{'Uploaded By'}\n"
        )

        self.table.insert(
            "end",
            header
        )

        self.table.insert(
            "end",
            "-" * 90 + "\n"
        )

        for document in documents:

            self.table.insert(
                "end",
                f"{document.document_type:<25}"
                f"{document.file_name:<30}"
                f"{document.uploaded_by}\n"
            )