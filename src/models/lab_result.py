class LabResult: 

    def __init__(
            self,
            lab_result_id,
            patient_id,
            test_name,
            test_date,
            result,
            notes
    ):

        self.lab_result_id = lab_result_id
        self.patient_id = patient_id
        self.test_name = test_name
        self.test_date = test_date
        self.result = result
        self.notes = notes