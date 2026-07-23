from services.patient_service import search_by_health_card

patient = search_by_health_card("HC12345678")

if patient:
    print(patient)
else:
    print("Patient not found.")