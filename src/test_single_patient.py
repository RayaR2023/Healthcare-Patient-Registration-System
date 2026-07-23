from services.patient_service import get_patient_by_id

patient = get_patient_by_id(1001)

if patient: 
    print(patient)
else:
    print("Patient not found.")