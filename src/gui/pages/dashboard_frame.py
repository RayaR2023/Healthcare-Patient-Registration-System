import customtkinter as ctk

class DashboardFrame(ctk.CTkFrame):

    def __init__(self,parent):

        super().__init__(parent)

        title = ctk.CTkLabel(

            self,
            text="🏥 Dashboard",
            font=("Segoe UI", 26, "bold")
        )
        title.pack(
            anchor = "w",
            padx = 30,
            pady = (25,10)
        )

        subtitle = ctk.CTkLabel(
            self,
            text="Healthcare Patient Registration System",
            font=("Segoe UI", 15)
        )
        subtitle.pack(
            anchor = "w",
            padx = 30,
            pady = (0,25)
        )

        self.cards_frame = ctk.CTkFrame(
            self,
            fg_color = "transparent"
        )

        self.cards_frame.pack(
            padx =25,
            pady = 10,
            fill = "both",
            expand = True
        )
        self.cards_frame.grid_columnconfigure((0,1), weight=1)

        self.patient_card = self.create_card(
            0,
            0,
            "Patients"
        )

        self.appointment_card = self.create_card(
            0,
            1,
            "Appointments"
        )

        self.referral_card = self.create_card(
            1,
            0,
            "Referrals"
        )

        self.lab_card = self.create_card(
            1,
            1,
            "Lab Results"
        )

        self.document_card = self.create_card(
            2,
            0,
            "Documents"
        )

    def create_card(self, row, column, title):
        card = ctk.CTkFrame(
            self.cards_frame,
            corner_radius=15
        )   
        card.grid(
            row=row,
            column=column,
            padx=15,
            pady=15,
            sticky="nsew"
        )

        title_label = ctk.CTkLabel(
            card,
            text=title,
            font=("Segoe UI",18,"bold")
        )

        title_label.pack(
            pady=(20,10)
        )

        value = ctk.CTkLabel(
            card,
            text="0",
            font=("Segoe UI",34,"bold")
        )

        value.pack(
            pady=(0,20)
        )

        return value

    def load_statistics(self, stats):

        self.patient_card.configure(
            text=str(stats["patients"])
        )

        self.appointment_card.configure(
            text=str(stats["appointments"])
        )

        self.referral_card.configure(
            text=str(stats["referrals"])
        )

        self.lab_card.configure(
            text=str(stats["lab_results"])
        )

        self.document_card.configure(
            text=str(stats["documents"])
        )