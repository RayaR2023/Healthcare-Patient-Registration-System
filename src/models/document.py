class Document: 


    def __init__(
        self,
        document_id,
        patient_id,
        document_type,
        file_name,
        uploaded_by,
        upload_date     
    ):
        self.document_id = document_id
        self.patient_id = patient_id
        self.document_type = document_type
        self.file_name = file_name
        self.uploaded_by = uploaded_by
        self.upload_date = upload_date