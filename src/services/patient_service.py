#this file is responsible for talking to the database:

#first goal: retrieve every patient:

#uses the SQL connection we've built in db.py
from database.db import get_connection
#uses patient class from patient.py file
from models.patient import Patient

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