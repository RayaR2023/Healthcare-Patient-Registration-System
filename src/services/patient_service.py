#this file is responsible for talking to the database:

#first goal: retrieve every patient:

#uses the SQL connection we've built in db.py
from src.database.db import get_connection
#uses patient class from patient.py file
from src.models.patient import Patient
from src.models.referral import Referral
from src.models.lab_result import LabResult
from src.models.document import Document
from src.models.appointment import Appointment
from src.models.referral import Referral

def row_to_patient(row):

    return Patient(
        first_name=row.FirstName,
        last_name=row.LastName,
        date_of_birth=row.DateOfBirth,
        sex=row.Sex,
        phone=row.Phone,
        email=row.Email,
        address=row.Address,
        health_card_number=row.HealthCardNumber,
        emergency_contact=row.EmergencyContact,
        emergency_phone=row.EmergencyPhone,
        family_doctor=row.FamilyDoctor,
        blood_type=row.BloodType,
        allergies=row.Allergies,
        patient_id=row.PatientID
    )



def get_all_patients():

    #creates the SQL connection
    connection = get_connection()
    #cursor is what actually sends SQL commands to SQL server (Python--> Cursor--> SQL Server)
    cursor = connection.cursor()

    #the SQL Query:
    cursor.execute("""
        SELECT *
        FROM Patients
        ORDER BY PatientID 
    """)

    #fetch rows
    rows = cursor.fetchall()

    #create an empty list that will fill with Patient objects
    patients = []

    #loop one patient at a time:
    for row in rows: 
        #convert SQL row into Python object
        patient = Patient(
            row.PatientID,
            row.FirstName,
            row.LastName,
            row.DateOfBirth,
            row.Sex,
            row.Phone,
            row.Email,
            row.Address,
            row.HealthCardNumber,
            row.EmergencyContact,
            row.EmergencyPhone,
            row.FamilyDoctor,
            row.BloodType,
            row.Allergies
        )
        patients.append(patient)

    #close connection
    connection.close()
    #method returns patient list, which will be called in another file
    return patients



def get_patient_by_id(patient_id):
    connection = get_connection()
    cursor = connection.cursor()

#query will give you the row of all the details of the patient with id used in method parameter
    cursor.execute(""" 
        SELECT *
        FROM Patients
        WHERE PatientID = ?
    """, patient_id)

    row = cursor.fetchone()
    connection.close()

    if row is None:
        return None

    return row_to_patient(row)

def search_by_health_card(health_card_number):

    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
        SELECT * 
        FROM Patients
        WHERE HealthCardNumber = ?
    """, health_card_number     
    )

    row = cursor.fetchone()
    connection.close()

    if row is None:
        return None

    return row_to_patient(row)


def add_patient(patient_data):
    connection = get_connection()
    cursor = connection.cursor()

#pass a dictionary, easier to maintain
    cursor.execute("""
    
        INSERT INTO Patients
        (
            FirstName,
            LastName,
            DateOfBirth,
            Sex,
            Phone,
            Email,
            Address,
            HealthCardNumber,
            EmergencyContact,
            EmergencyPhone,
            FamilyDoctor,
            BloodType,
            Allergies    
            )
            OUTPUT INSERTED.PatientID

            VALUES
            (?,
             ?,
             ?,
             ?,
             ?,
             ?,
             ?,
             ?,
             ?,
             ?,
             ?,
             ?,
             ?      
            )
    
    
    """, 
    patient_data["first_name"],
    patient_data["last_name"],
    patient_data["date_of_birth"],
    patient_data["sex"],
    patient_data["phone"],
    patient_data["email"],
    patient_data["address"],
    patient_data["health_card_number"],
    patient_data["emergency_contact"],
    patient_data["emergency_phone"],
    patient_data["family_doctor"],
    patient_data["blood_type"],
    patient_data["allergies"]
    )

    connection.commit()
    connection.close()


def get_patient_appointments(patient_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
    
        SELECT
            AppointmentID,
            PatientID,
            AppointmentDate, 
            AppointmentTime,
            AppointmentReason,
            AppointmentStatus,
            RoomNumber
        FROM Appointments
        WHERE PatientID = ?
        ORDER BY AppointmentDate DESC, AppointmentTime DESC
    
    """, patient_id)

    rows = cursor.fetchall()
    appointments = []
    for row in rows:
        appointment = Appointment(
            row.AppointmentID,
            row.PatientID,
            row.AppointmentDate,
            row.AppointmentTime,
            row.AppointmentReason,
            row.AppointmentStatus,
            row.RoomNumber
        )
        appointments.append(appointment)
    connection.close()
    return appointments
   


def get_patient_referrals(patient_id):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT
            r.ReferralID,
            r.PatientID,
            r.ReferringClinic,
            r.ReferralDate,
            r.DepartmentID,
            d.DepartmentName,
            r.Status,
            r.Notes

        FROM Referrals r

        INNER JOIN Departments d
            ON r.DepartmentID = d.DepartmentID

        WHERE r.PatientID = ?

        ORDER BY r.ReferralDate DESC
        """,
        patient_id
    )

    referrals = []

    for row in cursor.fetchall():

        referral = Referral(
            row.ReferralID,
            row.PatientID,
            row.ReferringClinic,
            row.ReferralDate,
            row.DepartmentID,
            row.Status,
            row.Notes
        )

        # add department name to the object
        referral.department_name = row.DepartmentName

        print(
            row.DepartmentID,
            row.DepartmentName
        )
        print(
            referral.department_name
        )
        referrals.append(referral)

    connection.close()

    return referrals


def get_patient_lab_results(patient_id):
    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT
            ResultID,
            PatientID,
            TestName,
            TestDate,
            Result,
            Notes
        FROM LabResults
        WHERE PatientID = ?
        ORDER BY TestDate DESC
        """,
        patient_id
    )
    rows = cursor.fetchall()
    results = []

    for row in rows:
        result = LabResult(
            row.ResultID,
            row.PatientID,
            row.TestName,
            row.TestDate,
            row.Result,
            row.Notes
        )
        results.append(result)
    cursor.close()
    connection.close()
   
    return results


def get_patient_documents(patient_id):
    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT 
            DocumentID,
            PatientID,
            DocumentType,
            FileName,
            UploadedBy,
            UploadDate
        FROM Documents
        WHERE PatientID = ?
        ORDER BY UploadDate DESC

        """,
        patient_id
    )

    documents = []
    for row in cursor.fetchall():
        documents.append(
            Document(
                row.DocumentID,
                row.PatientID,
                row.DocumentType,
                row.FileName,
                row.UploadDate,
                row.UploadedBy
            )
        )
    connection.close()
    return documents


def get_dashboard_statistics():

    connection = get_connection()
    cursor = connection.cursor()

    statistics = {}

    cursor.execute("SELECT COUNT(*) FROM Patients")
    statistics["patients"] = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM Appointments")
    statistics["appointments"] = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(*)
        FROM Referrals
        WHERE Status = 'Pending'
    """)
    statistics["pending_referrals"] = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(*)
        FROM LabResults
        WHERE Result='Abnormal'
    """)
    statistics["abnormal_labs"] = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(*)
        FROM Documents
    """)
    statistics["documents"] = cursor.fetchone()[0]

    connection.close()

    return statistics


def add_patient(patient):

    connection = get_connection()
    cursor = connection.cursor()

    query = """
    INSERT INTO Patients
    (
      FirstName,
      LastName,
      DateOfBirth,
      Sex,
      Phone,
      Email,
      Address,
      HealthCardNumber,
      EmergencyContact,
      EmergencyPhone,
      FamilyDoctor,
      BloodType,
      Allergies
    )
    OUTPUT INSERTED.PatientID
    VALUES
    (
        ?,
        ?,
        ?,
        ?,
        ?,
        ?,
        ?,
        ?,
        ?,
        ?,
        ?,
        ?,
        ?
    
    )
    """

    cursor.execute(
        query,
        (
            patient.first_name,
            patient.last_name,
            patient.date_of_birth,
            patient.sex,
            patient.phone,
            patient.email,
            patient.address,
            patient.health_card_number,
            patient.emergency_contact,
            patient.emergency_phone,
            patient.family_doctor,
            patient.blood_type,
            patient.allergies   
        )
    ) 
    new_id = cursor.fetchone()[0]
    connection.commit()
    patient.patient_id = int(new_id)
    cursor.close()
    connection.close()
    return patient

def update_patient(patient):

    connection = get_connection()
    cursor = connection.cursor()

    query = """
    
    UPDATE Patients
    SET 
        FirstName = ?,
        LastName = ?,
        DateOfBirth =?,
        Sex = ?,
        Phone = ?,
        Email = ?,
        Address = ?,
        HealthCardNumber = ?,
        EmergencyContact = ?,
        EmergencyPhone = ?,
        FamilyDoctor = ?,
        BloodType = ?,
        Allergies = ?
    WHERE PatientID = ?
    """
    cursor.execute(
        query,
        (
            patient.first_name,
            patient.last_name,
            patient.date_of_birth,
            patient.sex,
            patient.phone,
            patient.email,
            patient.address,
            patient.health_card_number,
            patient.emergency_contact,
            patient.emergency_phone,
            patient.family_doctor,
            patient.blood_type,
            patient.allergies,
            patient.patient_id  
        )
    )
    connection.commit()
    cursor.close()
    connection.close()


def delete_patient(patient_id):

    connection = get_connection()
    cursor = connection.cursor()

    try:

        # Delete appointments first
        cursor.execute(
            """
            DELETE FROM Appointments
            WHERE PatientID = ?
            """,
            (
                patient_id,
            )
        )


        # Delete referrals
        cursor.execute(
            """
            DELETE FROM Referrals
            WHERE PatientID = ?
            """,
            (
                patient_id,
            )
        )


        # Delete lab results
        cursor.execute(
            """
            DELETE FROM LabResults
            WHERE PatientID = ?
            """,
            (
                patient_id,
            )
        )


        # Delete documents
        cursor.execute(
            """
            DELETE FROM Documents
            WHERE PatientID = ?
            """,
            (
                patient_id,
            )
        )


        # Delete patient last
        cursor.execute(
            """
            DELETE FROM Patients
            WHERE PatientID = ?
            """,
            (
                patient_id,
            )
        )


        connection.commit()


    except Exception as e:

        connection.rollback()

        raise e


    finally:

        cursor.close()

        connection.close()

def add_appointment(
        patient_id,
        appointment_date,
        appointment_time,
        reason,
        status,
        room
):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO Appointments
        (
            PatientID,
            AppointmentDate,
            AppointmentTime,
            AppointmentReason,
            AppointmentStatus,
            RoomNumber
        )
        VALUES(?,?,?,?,?,?)

        """,
        patient_id,
        appointment_date,
        appointment_time,
        reason,
        status,
        room
    )

    connection.commit()
    connection.close()

def delete_appointment(appointment_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        DELETE FROM Appointments
        WHERE AppointmentID = ?
        """,
        appointment_id
    )
    connection.commit()
    connection.close()

def update_appointment(appointment):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE Appointments

        SET

            AppointmentDate=?,
            AppointmentTime=?,
            AppointmentReason=?,
            AppointmentStatus=?,
            RoomNumber=?

        WHERE AppointmentID=?
        """,

        appointment.appointment_date,
        appointment.appointment_time,
        appointment.appointment_reason,
        appointment.appointment_status,
        appointment.room_number,
        appointment.appointment_id
    )

    conn.commit()

    conn.close()


def add_referral(
        patient_id,
        clinic,
        referral_date,
        department_id,
        status,
        notes
): 
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO Referrals
        (
            PatientID,
            ReferringClinic,
            ReferralDate,
            DepartmentID,
            Status,
            Notes
        )
        VALUES(?,?,?,?,?,?)
        """,
        patient_id,
        clinic,
        referral_date,
        department_id,
        status,
        notes
    )

    conn.commit()
    conn.close()

def delete_referral(referral_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM Referrals
        WHERE ReferralID = ?
        """,
        referral_id
    )
    conn.commit()
    cursor.close()
    conn.close()

def update_referral(referral):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        UPDATE Referrals
        SET
            ReferringClinic = ?,
            ReferralDate = ?,
            DepartmentID = ?,
            Status = ?,
            Notes = ?
        WHERE ReferralID = ?
        """,
        referral.referring_clinic,
        referral.referral_date,
        referral.department_id,
        referral.status,
        referral.notes,
        referral.referral_id
    )
    conn.commit()
    cursor.close()
    conn.close()

def get_all_departments():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT
            DepartmentID,
            DepartmentName
        FROM Departments
        ORDER BY DepartmentName
        """
    )

    departments = cursor.fetchall()

    connection.close()

    return departments


def add_lab_result(
        patient_id,
        test_name,
        test_date,
        result,
        notes
):

    connection = get_connection()

    cursor = connection.cursor()


    cursor.execute(
        """
        INSERT INTO LabResults
        (
            PatientID,
            TestName,
            TestDate,
            Result,
            Notes
        )

        VALUES
        (
            ?,
            ?,
            ?,
            ?,
            ?
        )

        """,

        patient_id,
        test_name,
        test_date,
        result,
        notes
    )


    connection.commit()

    cursor.close()

    connection.close()


def update_lab_result(lab_result):

    connection = get_connection()

    cursor = connection.cursor()


    cursor.execute(
        """
        UPDATE LabResults

        SET

            TestName=?,
            TestDate=?,
            Result=?,
            Notes=?

        WHERE ResultID=?

        """,

        lab_result.test_name,
        lab_result.test_date,
        lab_result.result,
        lab_result.notes,
        lab_result.result_id
    )


    connection.commit()

    cursor.close()

    connection.close()


def delete_lab_result(result_id):

    connection = get_connection()

    cursor = connection.cursor()


    cursor.execute(
        """
        DELETE FROM LabResults

        WHERE ResultID = ?

        """,
        result_id
    )


    connection.commit()

    cursor.close()

    connection.close()

def add_document(
        patient_id,
        document_type,
        file_name,
        upload_date,
        uploaded_by
):

    connection = get_connection()

    cursor = connection.cursor()


    cursor.execute(
        """
        INSERT INTO Documents
        (
            PatientID,
            DocumentType,
            FileName,
            UploadDate,
            UploadedBy
        )

        VALUES
        (
            ?,
            ?,
            ?,
            ?,
            ?
        )

        """,

        patient_id,
        document_type,
        file_name,
        upload_date,
        uploaded_by
    )


    connection.commit()

    cursor.close()

    connection.close()

def update_document(document):

    connection = get_connection()

    cursor = connection.cursor()


    cursor.execute(
        """
        UPDATE Documents

        SET
            DocumentType = ?,
            FileName = ?,
            UploadDate = ?,
            UploadedBy = ?

        WHERE DocumentID = ?

        """,
        (
            document.document_type,
            document.file_name,
            document.upload_date,
            document.uploaded_by,
            document.document_id
        )
    )


    connection.commit()

    cursor.close()

    connection.close()

def delete_document(document_id):

    connection = get_connection()

    cursor = connection.cursor()


    cursor.execute(
        """
        DELETE FROM Documents
        WHERE DocumentID = ?
        """,
        document_id
    )


    connection.commit()

    cursor.close()

    connection.close()
    
def health_card_exists(number):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM Patients
        WHERE HealthCardNumber = ?
        """,
        number
    )

    result = cursor.fetchone()[0]

    connection.close()

    return result > 0