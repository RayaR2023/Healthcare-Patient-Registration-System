from src.services.patient_service import add_patient

new_patient = {

    "first_name": "Emma",

    "last_name": "Wilson",

    "date_of_birth": "2010-04-12",

    "sex": "Female",

    "phone": "6132223333",

    "email": "emma@email.com",

    "address": "45 Ottawa Street",

    "health_card_number": "HC99999999",

    "emergency_contact": "David Wilson",

    "emergency_phone": "6132224444",

    "family_doctor": "Dr. Elliana James",

    "blood_type": "A+",

    "allergies": "None"
}

add_patient(new_patient)
print("Patient added successfully!")