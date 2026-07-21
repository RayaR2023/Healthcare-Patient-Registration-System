create table Departments (

	DepartmentID INT Primary KEY Identity(1,1),

	DepartmentName VARCHAR(100) not null,

	PhoneNumber Varchar(20),

	FloorNumber INT

);

CREATE TABLE Doctors (

    DoctorID INT PRIMARY KEY IDENTITY(1,1),

    FirstName VARCHAR(50),

    LastName VARCHAR(50),

    DepartmentID INT,

    Email VARCHAR(100),

    Phone VARCHAR(20),

    FOREIGN KEY (DepartmentID)
    REFERENCES Departments(DepartmentID)

);

CREATE TABLE Patients (

    PatientID INT PRIMARY KEY IDENTITY(1000,1),

    FirstName VARCHAR(50) NOT NULL,

    LastName VARCHAR(50) NOT NULL,

    DateOfBirth DATE NOT NULL,

    Sex VARCHAR(10),

    Phone VARCHAR(20),

    Email VARCHAR(100),

    Address VARCHAR(200),

    HealthCardNumber VARCHAR(20) UNIQUE,

    EmergencyContact VARCHAR(100),

    EmergencyPhone VARCHAR(20),

    FamilyDoctor VARCHAR(100),

    BloodType VARCHAR(5),

    Allergies VARCHAR(255),

    DateRegistered DATETIME DEFAULT GETDATE()

);

CREATE TABLE Referrals (

    ReferralID INT PRIMARY KEY IDENTITY(1,1),

    PatientID INT,

    ReferringClinic VARCHAR(150),

    ReferralDate DATE,

    DepartmentID INT,

    Status VARCHAR(50),

    Notes VARCHAR(500),

    FOREIGN KEY (PatientID)

        REFERENCES Patients(PatientID),

    FOREIGN KEY (DepartmentID)

        REFERENCES Departments(DepartmentID)

);


CREATE TABLE Appointments (

    AppointmentID INT PRIMARY KEY IDENTITY(1,1),

    PatientID INT,

    DoctorID INT,

    AppointmentDate DATE,

    AppointmentTime TIME,

    AppointmentStatus VARCHAR(50),

    AppointmentReason VARCHAR(200),

    RoomNumber VARCHAR(20),

    FOREIGN KEY (PatientID)

        REFERENCES Patients(PatientID),

    FOREIGN KEY (DoctorID)

        REFERENCES Doctors(DoctorID)

);


CREATE TABLE Documents (

    DocumentID INT PRIMARY KEY IDENTITY(1,1),

    PatientID INT,

    DocumentType VARCHAR(100),

    FileName VARCHAR(255),

    UploadDate DATETIME DEFAULT GETDATE(),

    UploadedBy VARCHAR(100),

    FOREIGN KEY(PatientID)

    REFERENCES Patients(PatientID)

);


CREATE TABLE LabResults (

    ResultID INT PRIMARY KEY IDENTITY(1,1),

    PatientID INT,

    TestName VARCHAR(150),

    TestDate DATE,

    Result VARCHAR(255),

    Notes VARCHAR(500),

    FOREIGN KEY(PatientID)

    REFERENCES Patients(PatientID)

);

CREATE TABLE Users (

    UserID INT PRIMARY KEY IDENTITY(1,1),

    Username VARCHAR(50),

    PasswordHash VARCHAR(255),

    Role VARCHAR(50)

);

