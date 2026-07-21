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
