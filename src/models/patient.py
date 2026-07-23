class Patient: 

    #reps one patient record in database:

    def __init__(
            self,
            patient_id,
            first_name, 
            last_name, 
            date_of_birth,
            sex,
            phone,
            email, 
            address,
            health_card_number,
            emergency_contact,
            emergency_phone,
            family_doctor,
            blood_type,
            allergies

    ):

        self.patient_id = patient_id
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.sex = sex
        self.phone = phone
        self.email = email
        self.address = address
        self.health_card_number = health_card_number
        self.emergency_contact = emergency_contact
        self.emergency_phone = emergency_phone
        self.family_doctor = family_doctor
        self.blood_type = blood_type
        self.allergies = allergies

    def __str__(self):
        return f"{self.patient_id} - {self.first_name} {self.last_name}"