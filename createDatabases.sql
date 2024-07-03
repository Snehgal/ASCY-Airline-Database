-Plane Mananagement
create database PM;
use PM;
create table P_Management (Id int primary key,
Model varchar(20), YoM int (4), Capacity int(3),
Fuel_Hour int(5), Endurance int (5), Hours_Flown int (5),
Status varchar (20));
Insert into P_Management values ( 1, ‘Airbus 320’,2000 , 150, 350, 6300, 20000,
‘Grounded’);
Insert into P_Management values ( 2, ‘Airbus 321’,2010 , 180, 450, 8000, 25000,
‘Airworthy’);
Insert into P_Management values ( 3, ‘Airbus 330’,2015 , 220, 750, 10000, 12000,
‘Check’);
Insert into P_Management values( 5, ‘Boeing 737’,1998 , 150, 100, 2500, 25000,
‘Retired’);

-Passenger Details
create database PAX;
use PAX;
create table DETAILS (Pax_Code int(5) primary key,
Flight_No int (5),
Class varchar(20),Name varchar (20),
Phone_No int (20), Sex varchar (20),
Email varchar (30));
Insert into DETAILS values (12345, 22222, ‘First’, ‘Chirag’, 9981928182 , ‘ Male’,
‘abc@gmail.com’);
Insert into DETAILS values (13345, 22223, ‘First’, ‘Advay’, 8981928182 , ‘ Male’,
‘xyz@gmail.com’);
Insert into DETAILS values (14345, 22224, ‘First’, ‘Srijan’, 7981928182 , ‘ Male’,
‘pqr@gmail.com’);
Insert into DETAILS values (15345, 22225, ‘Economy’, ‘Tarini’, 6981928182 , ‘
Female’, ‘aaa@gmail.com’);

-Flight and Ticket Details
create database DETAILS;
use DETAILS;
create table DEETS (FlightID varchar(5) primary key,
Destination varchar (20), Date_Departure Date,
Gate_No int(3), Boarding_Time time,
Ticket_Cost int(5));
Insert into DEETS values ( ‘ABC21’, ‘Bombay’, ‘2022-12-10’, 35, ‘02:00:00’, 10000);
Insert into DEETS values ( ‘ABC22’, ‘Delhi’, ‘2022-12-12, 12’,’ 06:00:00’, 9000);
Insert into DEETS values ( ‘ABC23’, ‘London’, ‘2022-12-11’, 9, ‘12:30:00’, 90000);
Insert into DEETS values( ‘PQR21’, ‘New York’,’ 2022-12-15’, 8, ‘12:45:00’, 80000);

-Employee Mananagement
create database EMP;
use EMP;
create table INFO ( Emp_Id int (5) primary key,
Name varchar(20) , D_O_J date ,
Designation varchar (20),
Salary int (6));
Insert into INFO values (77821, ‘Rajesh’ , ‘2010-05-01’, ‘Sales Head’, 75000);
Insert into INFO values(77822, ‘Ram’ , ‘2012-06-01’, ‘HR Head’, 90000);
Insert into INFO values (77823, ‘Rohini’ ,’ 2010-01-01’, ‘Marketing Head’, 80000);
Insert into INFO values(77824, ‘Rose’ , ‘2009-02-01’, ‘CEO’,95000);
