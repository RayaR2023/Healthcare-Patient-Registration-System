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
            height = 250,
            font = ("Consolas", 13)
        )

        self.table.pack(
            fill = "both",
            expand = True,
            padx = 20,
            pady = 20
        )

    def display_lab_results(self, results):
        self.table.configure(
            state = "normal"
        )

        self.table.delete(
            "1.0", 
            "end"
        )
        if not results:
            self.table.insert(
                "end",
                "No lab results found for this patient."
            )
        else:
            self.table.insert(
                "end",
                "ID     Date          Test Name                     Result"      
            )
            self.table.insert(
                "end",
                "-"*100 + "\n"
            )

            for lab in results:

                self.table.insert(
                    "end",
                    f"{lab.result_id:<7}"
                    f"{str(lab.test_date):<14}"
                    f"{lab.test_name:<30}"
                    f"{lab.result:<20}"
                    f"{lab.notes or ''}\n"
                )


        self.table.configure(
            state="disabled"
        )