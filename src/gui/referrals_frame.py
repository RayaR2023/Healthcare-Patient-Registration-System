import customtkinter as ctk


class ReferralsFrame(ctk.CTkFrame):

    def __init__(self,parent):

        super().__init__(parent)

        title = ctk.CTkLabel(
            self,
            text = "Patient Referrals",
            font = ("Segoe UI", 18, "bold")
        )

        title.pack(
            anchor = "w",
            padx = 20,
            pady = (15,20)
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


    def display_referrals(self, referrals):
        self.table.delete(
            "1.0",
            "end"
        )

        header = (
            f"{'Date':<15}"
            f"{'Status':<15}"
            f"{'Clinic':<35}"
            f"Notes\n"
        )

        self.table.insert(
            "end",
            header
        )

        self.table.insert(
            "end",
            "-" * 110 + "\n"
        )

        for referral in referrals:
            line = (
            f"{str(referral.referral_date):<15}"
            f"{referral.status:<15}"
            f"{referral.referring_clinic:<35}"
            f"{referral.notes}\n"
            )

            self.table.insert(
                "end",
                line
            )
        