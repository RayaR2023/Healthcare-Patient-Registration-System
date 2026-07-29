import customtkinter as ctk


class AppointmentsFrame(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(parent)

        self.pack_propagate(False)

        self.configure(
            height=300
        )


        title = ctk.CTkLabel(
            self,
            text="Appointments",
            font=("Segoe UI",18,"bold")
        )

        title.pack(
            anchor="w",
            padx=20,
            pady=(15,10)
        )


        self.table = ctk.CTkTextbox(
            self,
            height=220,
            font=("Consolas",13)
        )

        self.table.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0,20)
        )



    def display_appointments(self, appointments):

        self.table.configure(
            state="normal"
        )

        self.table.delete(
            "1.0",
            "end"
        )


        if not appointments:

            self.table.insert(
                "end",
                "No appointments found."
            )

        else:

            self.table.insert(
                "end",
                "Date            Time        Reason                         Status        Room\n"
            )

            self.table.insert(
                "end",
                "-"*100 + "\n"
            )


            for appt in appointments:

                self.table.insert(
                    "end",
                    f"{appt[0]}    "
                    f"{appt[1]}    "
                    f"{appt[2]}    "
                    f"{appt[3]}    "
                    f"{appt[4]}\n"
                )


        self.table.configure(
            state="disabled"
        )