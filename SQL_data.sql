USE Northwind

CREATE DATABASE dangus_db;
USE dangus_db;

SELECT * FROM Passengers
SELECT * FROM Booking_Details
SELECT * FROM Staff
SELECT * FROM Destination
SELECT * FROM Airplane

DROP TABLE Passengers
DROP TABLE Booking_Details
DROP TABLE Staff
DROP TABLE Destination
DROP TABLE Airplane


CREATE TABLE Booking_Details 
(
    Booking_ID INT,
    Flight_Number INT,
    PassengersID INT,
    Destination_ID INT,
    Flight_Price INT,
    PRIMARY KEY (Booking_ID),
);


INSERT INTO Booking_Details
VALUES 
(505, 8232, 269, 1099, 799),
(408, 660, 149, 3019, 654),
(800, 680, 227, 1031, 76),
(190, 680, 201, 1031, 76),
(122, 595, 140, 1471, 45),
(21, 660, 183, 3019, 654),
(900, 595, 253, 1472, 45), 
(305, 595, 203, 1472, 45),
(211, 660, 144, 3019, 654),
(16, 8232, 150, 1099, 799),
(241, 680, 218, 1031, 76)

SELECT * FROM Booking_Details


CREATE TABLE Passengers
(
    PassengersID INT,
    First_Name VARCHAR(20),
    Last_Name VARCHAR(30),
    DOB DATE,
    Booking_ID INT,
    Passport_Number INT, 
    PRIMARY KEY (PassengersID),
    FOREIGN KEY ([Booking_ID]) REFERENCES Booking_Details(Booking_ID)
)

INSERT INTO Passengers
VALUES 
(269, 'Emma', 'Caldwell', '1993-01-05',505, 16090925),
(149, 'Tom','Sims','1960-02-21',408,16180213),
(227, 'James', 'Weaver', '1987-03-20', 800, 16171111),
(201, 'Philip', 'Thomas', '1998-01-13', 190, 16940104),
(140, 'Ellie', 'Krueger', '1988-09-05', 122, 16240825),
(183, 'Randy', 'Meyers', '2001-01-01', 21, 16860404),
(253, 'Marcus', 'Mann', '2000-11-08', 900, 16310108),
(203, 'Jacob', 'Ferguson', '1994-01-14', 305, 16240825),
(144, 'Harry', 'Ritter', '1996-01-14', 211, 16970829),
(150, 'Peter', 'Atkinson', '1992-01-16', 16, 16890626),
(218, 'Elizabeth', 'Rojas', '1979-12-14', 241, 16060317)

SELECT * FROM Passengers

CREATE TABLE Staff
(
    Staff_ID INT,
    Destination_ID INT,
    Employee_Name VARCHAR (40),
    PRIMARY KEY (Staff_ID),
    FOREIGN KEY (Destination_ID) REFERENCES Destination (Destination_ID)
)

INSERT INTO STAFF
VALUES
(1, 1031, 'Vicki Guerrero'),
(2, 3019, 'Stephan Mcclure'),
(3, 1099, 'Chardonnay Miranda'),
(4, 3019, 'Destiny Kirby'),
(5, 1031, 'Alex Cruz'),
(6, 1099, 'Rohaan Golden'),
(7, 1471, 'Karis Woodward'),
(8, 1031, 'Eileen Gibbons'),
(9, 1471, 'Bianka Peters'),
(10,1031,'Nicolas Mcgill')

SELECT * FROM Staff

CREATE TABLE Destination
(
    Destination_ID INT, 
    Country VARCHAR(20),
    City VARCHAR(20),
    Flight_Price INT, 
    Flight_Type VARCHAR(15),
    PRIMARY KEY(Destination_ID)
)

INSERT INTO Destination
VALUES
(3019, 'Brazil', 'Sao Paulo', 654, 'Long-haul'),
(1031, 'Norway', 'Oslo', 76, 'Short-haul'),
(1471, 'Spain', 'Barcelona', 45, 'Short-haul'),
(1099, 'Australia', 'Sydney', 799, 'Long-haul')

INSERT INTO Destination
VALUES
(1040, 'Spain', 'Madrid', 39, 'Short-haul'),
(1011, 'Spain', 'Valencia',48, 'Short-haul' ),
(1021, 'France', 'Paris', 50, 'Short-haul'),
(1075, 'Italy', 'Rome', 51, 'Short-haul'),
(1055, 'Italy', 'Milan', 35, 'Short-haul'), 
(1072, 'Germany', 'Berlin', 66, 'Short-haul'),
(4011, 'Germany', 'Munich', 98, 'Short-haul'),
(1101, 'Czezh Republic', 'Prague', 45, 'Short-haul'),
(6011, 'Hungary', 'Budapest', 21, 'Short-haul')

INSERT INTO Destination
VALUES
(7100, 'South Africa', 'Cape Town', 545, 'Long- haul'),
(5133, 'Mexico', 'Cancun', 614, 'Long-haul')


SELECT * FROM Destination

CREATE TABLE Airplane
(
    Flight_ID INT IDENTITY (10,1),
    Flight_Number INT,
    Destination_ID INT,
    PassengersID INT,
    Duration TIME,
    Seat_Location INT,
    PRIMARY KEY (Flight_ID),
    FOREIGN KEY (PassengersID) REFERENCES Passengers (PassengersID),
    FOREIGN KEY (Destination_ID) REFERENCES Destination (Destination_ID)
)

INSERT INTO Airplane
VALUES
(8232, 1099, 269, '18:00:00', 19),
(660, 3019, 149, '12:00:00', 15),
(680, 1031, 227, '2:00:00', 11),
(680, 1031, 201, '2:00:00', 17),
(595, 1471, 140, '3:00:00', 60),
(660, 3019, 183, '12:00:00', 21),
(595, 1471, 253, '3:00:00', 70),
(595, 1471, 203, '3:00:00', 75),
(660, 3019, 144, '12:00:00', 16),
(8232, 1099, 150, '18:00:00', 30),
(680, 1031, 218, '2:00:00', 10)

SELECT * FROM Airplane


____
SELECT p.First_name, p.PassengersID,d.City FROM Passengers p
JOIN Booking_Details bd on bd.PassengersID = p.PassengersID
JOIN Destination d on bd.Destination_ID = d.Destination_ID
WHERE City = 'Oslo';


SELECT * FROM Destination;
SELECT * FROM Destination WHERE Flight_Type = 'Short-haul';
SELECT * FROM Destination WHERE Flight_Type = 'Long-haul';
