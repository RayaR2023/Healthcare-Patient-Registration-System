from services.patient_service import get_all_patients

try: 
    #call this method, which will connect to SQL server, and runs the query we wrote in that file
    #this will also create a Patient object for each row, and return a Python List and print each patient
    patients = get_all_patients()
    print("Patient List")
    print("-" * 40)
#you will get an output of a list of each patient id and the name
    for patient in patients:
        print(patient)

except Exception as e:
    print("Error:")
    print(e)