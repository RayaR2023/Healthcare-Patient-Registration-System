class Document:

    def __init__(
        self,
        document_id,
        patient_id,
        document_type,
        file_name,
        upload_date,
        uploaded_by
    ):

        self.document_id = document_id
        self.patient_id = patient_id
        self.document_type = document_type
        self.file_name = file_name
        self.upload_date = upload_date
        self.uploaded_by = uploaded_by