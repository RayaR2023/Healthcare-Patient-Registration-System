#this file is responsible for talking to the database:

#first goal: retrieve every patient:

#uses the SQL connection we've built in db.py
from src.database.db import get_connection
#uses patient class from patient.py file
from src.models.patient import Patient
from src.models.referral import Referral
from src.models.lab_result import LabResult

def row_to_patient(row):

    return Patient(
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
            AppointmentDate, 
            AppointmentTime,
            AppointmentReason,
            AppointmentStatus,
            RoomNumber
        FROM Appointments
        WHERE PatientID = ?
        ORDER BY AppointmentDate
    
    """, patient_id)

    appointments = cursor.fetchall()

    connection.close()
    return appointments


def get_patient_referrals(patient_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT
            ReferralID,
            PatientID,
            ReferringClinic,
            ReferralDate,
            DepartmentID,
            Status,
            Notes
        FROM Referrals
        WHERE PatientID = ?
        ORDER BY ReferralDate DESC
        """,
        patient_id
    )

    referrals = []

    for row in cursor.fetchall():
        referrals.append(
            Referral(
                row.ReferralID,
                row.PatientID,
                row.ReferringClinic,
                row.ReferralDate,
                row.DepartmentID,
                row.Status,
                row.Notes
            )
        )
    connection.close()
    return referrals


def get_patient_lab_results(patient_id):
    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT
        LabResultID,
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

    results = []

    for row in cursor.fetchall():
        results.append(
            LabResult(
                row.LabResultID,
                row.PatientID,
                row.TestName,
                row.TestDate,
                row.Result,
                row.Notes
            )
        )

    connection.close()
    return results