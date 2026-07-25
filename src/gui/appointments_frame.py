import customtkinter as ctk
class AppointmentsFrame(ctk.CTkFrame):

    def __init__(self,parent):
        super().__init__(parent)


        title = ctk.CTkLabel(
            self, 
            text = "Appointments",
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
            height = 180
        )

        self.table.pack(
            padx = 20,
            pady = (0,20),
            fill = "x"
        )


    def display_appointments(self, appointments):
        self.table.delete(
            "1.0",
            "end"
        )

        header = (
            f"{'Date':<14}"
            f"{'Time':<10}"
            f"{'Status':<15}"
            f"{'Room':<10}"
            f"Reason\n"
        )

        self.table.insert(
            "end",
            header
        )

        self.table.insert(
            "end",
            "-" * 90 + "\n"
        )

        for appt in appointments:

            line = (


                f"{str(appt.AppointmentDate):<14}"

                f"{str(appt.AppointmentTime):<10}"

                f"{appt.AppointmentStatus:<15}"

                f"{appt.RoomNumber:<10}"

                f"{appt.AppointmentReason}"

                "\n"
                
            )

            self.table.insert(
                "end",
                line
            )