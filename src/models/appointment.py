class Appointment:

    def __init__(
            self,
            appointment_id,
            patient_id,
            appointment_date,
            appointment_time,
            appointment_reason, 
            appointment_status,
            room_number
    ):
        self.appointment_id = appointment_id
        self.patient_id = patient_id
        self.appointment_date = appointment_date
        self.appointment_time = appointment_time
        self.appointment_reason = appointment_reason
        self.appointment_status = appointment_status
        self.room_number = room_number