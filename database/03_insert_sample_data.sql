INSERT INTO Departments
VALUES
('Pediatrics','6135551111',2),
('Genetics','6135552222',3),
('Cardiology','6135553333',4),
('Neurology','6135554444',5),
('Emergency','6135555555',1);

INSERT INTO Doctors
VALUES

('Elliana','James',1,'ejames@hospital.ca','6135551111'),

('Amos','Smith',2,'asmith@hospital.ca','6135552222'),

('Theodore','Lee',3,'tlee@hospital.ca','6135553333');


INSERT INTO Patients (

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

VALUES(

'Olivia',

'Brown',

'2015-06-11',

'Female',

'6135558888',

'olivia@email.com',

'123 Maple Street',

'HC12345678',

'Jane Brown',

'6135557777',

'Dr. Elliana James',

'O+',

'Peanuts'

), 
(

'Gabriella',

'Scott',

'2017-06-11',

'Female',

'6136667777',

'gabs@email.com',

'677 Daffodil Street',

'HC67676767',

'John Scott',

'6135457777',

'Dr. Theodore Lee',

'B+',

'Peanuts'

);

Insert into Doctors
VALUES
('Derek', 'Shepherd', 4, 'dshepherd@hospital.ca', '6134556789'),
('Meredith', 'Grey', 5, 'mgrey@hospital.ca', '6134558989');


INSERT INTO Patients (

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

VALUES(

'Rachel',

'Green',

'1972-06-11',

'Female',

'6135455888',

'rachelg@email.com',

'13 Smith Street',

'HC88888887',

'Karen Green',

'6139997987',

'Dr. Amos Smith',

'A-',

'N/A'

),
(

'Monica',

'Geller',

'1972-08-13',

'Female',

'6133576888',

'monicag@email.com',

'12 Forest Street',

'HC12345666',

'Ross Geller',

'6138887987',

'Dr. Theodore Lee',

'O-',

'Eggs'

),
(

'Conrad',

'Fisher',

'2001-09-11',

'Male',

'6135437888',

'connie@email.com',

'2 Summer Street',

'HC89988887',

'Jeremiah Fisher',

'6139997987',

'Dr. Derek Shepherd',

'A-',

'N/A'

)




INSERT INTO Appointments
(
    PatientID,
    DoctorID,
    AppointmentDate,
    AppointmentTime,
    AppointmentStatus,
    AppointmentReason,
    RoomNumber
)
VALUES
(
    1000,
    2,
    '2026-08-04',
    '09:30',
    'Scheduled',
    'Initial Genetics Consultation',
    'G-302'
),
(
    1001,
    2,
    '2026-08-15',
    '19:30',
    'Complete',
    'Initial Genetics Consultation',
    'G-301'
),
(
    1002,
    3,
    '2026-08-10',
    '16:30',
    'Scheduled',
    'Cardiology Follow-Up Consultation',
    'C-402'
),
(
    1003,
    4,
    '2026-12-04',
    '09:00',
    'Scheduled',
    'Initial Neurology Consultation',
    'N-500'
),
(
    1004,
    5,
    '2026-10-05',
    '13:30',
    'Complete',
    'Emergency Head Scan',
    'G-100'
);



INSERT INTO Documents
(
    PatientID,
    DocumentType,
    FileName,
    UploadedBy
)
VALUES
(
    1000,
    'Referral Letter',
    'Referral_1000.pdf',
    'Sarah Wilson'
), 
(
    1001,
    'Referral Letter',
    'Referral_1001.pdf',
    'John Adams'
),
(
    1002,
    'Referral Letter',
    'Referral_1002.pdf',
    'Randall Lee'
),
(
    1003,
    'Referral Letter',
    'Referral_1003.pdf',
    'Carly Han'
), 
(
    1004,
    'Referral Letter',
    'Referral_1004.pdf',
    'Sarah Wilson'
);

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
    1000,
    'Chromosome Analysis',
    '2026-08-10',
    'Normal',
    'No chromosomal abnormalities detected.'
), 
(
    1001,
    'Chromosome Analysis',
    '2026-09-10',
    'Abnormal',
    'Chromosomal Abnormality on Chromosome 13.'
), 
(
    1002,
    'Cardio Stress Test Follow-Up',
    '2026-09-10',
    'Normal',
    'No heart issues detected during test.'
)

INSERT INTO Users
(
    Username,
    PasswordHash,
    Role
)
VALUES
(
    'swilson',
    'HASH_PLACEHOLDER',
    'Registration Clerk'
);



INSERT INTO Referrals
(
    PatientID,
    ReferringClinic,
    ReferralDate,
    DepartmentID,
    Status,
    Notes
)
VALUES
(
    1000,
    'Ottawa Genetic Health Clinic',
    '2026-07-15',
    2,
    'Scheduled',
    'Referral submitted for genetic consultation due to family history of inherited condition. Awaiting appointment scheduling.'
), 
(
    1001,
    'Kanata Genetic Health Clinic',
    '2026-07-19',
    2,
    'Scheduled',
    'Referral submitted for genetic consultation due to family history of inherited condition. Awaiting appointment scheduling.'
), 
(
    1002,
    'The Ottawa General Hospital- Cardiology Department',
    '2026-07-15',
    3,
    'Scheduled',
    'Follow-Up cardio stress test due to abnormal heart murmur detected from previous consultation.'
);
