from src.services.patient_service import update_appointment


update_appointment(
    5,   # AppointmentID - replace with your actual ID
    "2026-09-05",
    "11:00",
    "Updated Follow-up Appointment",
    "Scheduled",
    "B-205"
)


print("Appointment updated")