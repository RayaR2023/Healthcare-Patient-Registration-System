import customtkinter as ctk

class LabResultsFrame(ctk.CTkFrame):

    def __init__(self,parent):

        super().__init__(parent)

        title = ctk.CTkLabel(
            self,
            text = "Lab Results",
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

    def display_lab_results(self, results):

        self.table.delete(
            "1.0",
            "end"
        )

        header = (
            f"{'Date':<15}"
            f"{'Test':<35}"
            f"{'Result':<15}"
            f"Notes\n"
        )
        self.table.insert(
            "end",
            header
        )
        self.table.insert(
            "end",
            "-" *110 + "\n"
        )

        for result in results:
            self.table.insert(
                "end",
                f"{str(result.test_date):<15}"
                f"{result.test_name:<35}"
                f"{result.result:<15}"
                f"{result.notes}\n"
            )
