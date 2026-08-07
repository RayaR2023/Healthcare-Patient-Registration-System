# 🏥 Healthcare Patient Registration System (HPRMS)

A full-stack desktop healthcare management application built with **Python**, **SQL Server**, and **CustomTkinter**.

The Healthcare Patient Registration System (HPRMS) allows healthcare staff to register patients, manage appointments, referrals, laboratory results, patient documents, and generate professional PDF reports. This project was developed as a portfolio application to demonstrate healthcare administration, database management, CRUD operations, desktop GUI development, and SQL integration.

---

# Features

### 👤 Patient Management
- Register new patients
- Search patients by Health Card Number
- View patient information
- Edit patient information
- Delete patients

### 📅 Appointment Management
- Add appointments
- Edit appointments
- Delete appointments
- Appointment history

### ➡️ Referral Management
- Add referrals
- Edit referrals
- Delete referrals
- Department lookup

### 🧪 Laboratory Results
- Record lab results
- Edit lab results
- Delete lab results
- Track abnormal results

### 📄 Patient Documents
- Upload document records
- Edit document information
- Delete documents

### 📊 Dashboard
- Live patient statistics
- Appointment totals
- Pending referrals
- Abnormal laboratory results
- Document totals

### 📑 Reporting
- Generate professional PDF patient reports
- Export patient demographic information
- Export appointments
- Export referrals
- Export laboratory results
- Export uploaded documents

---

# Technologies Used

- Python 3.11
- SQL Server
- SQL Server Management Studio (SSMS)
- CustomTkinter
- pyodbc
- ReportLab
- Git
- GitHub

---

# Project Structure

```text
Healthcare-Patient-Registration-System/

src/
│
├── database/
├── gui/
├── models/
├── services/
├── utils/
│
sql/
│
├── database.sql
└── sample_data.sql

reports/

requirements.txt
README.md
```

---

# Screenshots

*(Screenshots will be added in a future update.)*

- Dashboard
- Register Patient
- Search Patient
- Appointments
- Referrals
- Laboratory Results
- Documents
- PDF Report

---

# Installation

## 1. Clone the repository

```bash
git clone https://github.com/RayaR2023/Healthcare-Patient-Registration-System.git
```

Move into the project folder:

```bash
cd Healthcare-Patient-Registration-System
```

---

## 2. Create a virtual environment

Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

---

## 3. Install the required packages

```bash
pip install -r requirements.txt
```

---

## 4. Install SQL Server

Install:

- Microsoft SQL Server Express
- SQL Server Management Studio (SSMS)

---

## 5. Create the database

Open SQL Server Management Studio.

Run the following scripts in order:

```text
sql/database.sql
```

Then:

```text
sql/sample_data.sql
```

These scripts create:

- Database
- Tables
- Relationships
- Sample healthcare data

---

## 6. Configure the database connection

Open:

```text
src/database/db.py
```

Update the connection string if necessary.

Example:

```python
connection_string = (
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=localhost\\SQLEXPRESS;"
    "DATABASE=HPRMS;"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)
```

If your SQL Server instance uses a different server name, replace:

```text
localhost\SQLEXPRESS
```

with your own SQL Server instance.

---

## 7. Run the application

```bash
python -m src.gui.app
```

The desktop application will launch.

---

# Sample Data

The repository includes fictional healthcare data inspired by popular television and movie characters for demonstration purposes.

Included data includes:

- Patients
- Doctors
- Departments
- Appointments
- Referrals
- Laboratory Results
- Documents

---

# PDF Reports

Patient reports can be exported directly from the application.

Generated reports are automatically saved to:

```text
reports/
```

---

# Future Improvements

- User authentication
- Role-based access control
- Prescription management
- Medical imaging support
- Advanced search filters
- Email appointment reminders
- Dark mode customization
- Cloud database deployment
- Automated backups

---

# Skills Demonstrated

This project demonstrates experience with:

- Python programming
- Object-Oriented Programming (OOP)
- SQL Server database design
- CRUD operations
- Database normalization
- Desktop GUI development
- MVC-style project organization
- PDF report generation
- Git version control
- GitHub project management
- Healthcare information systems concepts

---

# Author

**Raya Rozario**

Bachelor of Computer Science  
Carleton University

GitHub:

https://github.com/RayaR2023

---

# License

This project is intended for educational and portfolio purposes only.

The patient data included is entirely fictional and does not represent real individuals.
