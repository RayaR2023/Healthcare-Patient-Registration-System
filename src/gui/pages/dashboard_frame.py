import customtkinter as ctk

from src.gui.styles import *


class DashboardFrame(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            fg_color=BACKGROUND
        )


        self.grid_rowconfigure(
            2,
            weight=1
        )

        self.grid_columnconfigure(
            0,
            weight=1
        )


        # ==========================
        # HEADER
        # ==========================


        header = ctk.CTkFrame(
            self,
            fg_color=PRIMARY,
            corner_radius=20
        )


        header.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=30,
            pady=(25,15)
        )


        ctk.CTkLabel(
            header,
            text="Healthcare Patient Registration System",
            font=TITLE_FONT,
            text_color="white"
        ).pack(
            anchor="w",
            padx=25,
            pady=(20,5)
        )


        ctk.CTkLabel(
            header,
            text="Clinical Management Dashboard",
            font=SUBTITLE_FONT,
            text_color="white"
        ).pack(
            anchor="w",
            padx=25,
            pady=(0,20)
        )



        # ==========================
        # CARDS
        # ==========================


        self.cards_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )


        self.cards_frame.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=30
        )


        self.cards_frame.grid_columnconfigure(
            (0,1),
            weight=1
        )



        self.patient_card = self.create_card(
            0,
            0,
            "👤 Patients"
        )


        self.appointment_card = self.create_card(
            0,
            1,
            "📅 Appointments"
        )


        self.referral_card = self.create_card(
            1,
            0,
            "➡ Pending Referrals"
        )


        self.lab_card = self.create_card(
            1,
            1,
            "🧪 Abnormal Labs"
        )


        self.document_card = self.create_card(
            2,
            0,
            "📄 Documents"
        )



        # ==========================
        # WELCOME PANEL
        # ==========================


        welcome = ctk.CTkFrame(
            self,
            fg_color=CARD_BACKGROUND,
            corner_radius=20
        )


        welcome.grid(
            row=2,
            column=0,
            sticky="nsew",
            padx=30,
            pady=20
        )



        ctk.CTkLabel(
            welcome,
            text="Welcome",
            font=HEADER_FONT,
            text_color=PRIMARY_DARK
        ).pack(
            anchor="w",
            padx=25,
            pady=(20,10)
        )


        message = (
            "Welcome to the Healthcare Patient Registration System.\n\n"
            "Manage:\n\n"
            "• Patient registration\n"
            "• Appointments\n"
            "• Referrals\n"
            "• Laboratory results\n"
            "• Medical documents\n\n"
            "Dashboard statistics update automatically."
        )


        ctk.CTkLabel(
            welcome,
            text=message,
            justify="left",
            font=BODY_FONT,
            text_color=TEXT
        ).pack(
            anchor="w",
            padx=25,
            pady=(0,25)
        )



    def create_card(self,row,column,title):


        card = ctk.CTkFrame(
            self.cards_frame,
            fg_color=CARD_BACKGROUND,
            corner_radius=20,
            height=150
        )


        card.grid(
            row=row,
            column=column,
            sticky="nsew",
            padx=15,
            pady=15
        )


        card.grid_propagate(False)



        ctk.CTkLabel(
            card,
            text=title,
            font=CARD_TITLE_FONT,
            text_color=PRIMARY_DARK
        ).pack(
            pady=(25,5)
        )


        value = ctk.CTkLabel(
            card,
            text="0",
            font=CARD_VALUE_FONT,
            text_color=PRIMARY
        )


        value.pack()


        return value



    def load_statistics(self,stats):

        self.patient_card.configure(
            text=str(stats["patients"])
        )

        self.appointment_card.configure(
            text=str(stats["appointments"])
        )

        self.referral_card.configure(
            text=str(stats["pending_referrals"])
        )

        self.lab_card.configure(
            text=str(stats["abnormal_labs"])
        )

        self.document_card.configure(
            text=str(stats["documents"])
        )