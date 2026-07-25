class Referral:

    def __init__(
            self,
            referral_id,
            patient_id,
            referring_clinic,
            referral_date,
            department_id,
            status,
            notes
    ):

        self.referral_id = referral_id
        self.patient_id = patient_id
        self.referring_clinic = referring_clinic
        self.referral_date = referral_date
        self.department_id = department_id
        self.status = status
        self.notes = notes