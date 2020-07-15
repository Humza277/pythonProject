USE dangus_db

IF EXISTS(SELECT 1 FROM sys.tables WHERE object_id = OBJECT_ID('Passengers'))
BEGIN;
    DROP TABLE [Passengers];
END;
GO

CREATE TABLE [Passengers] (
    [PassengersID] INTEGER NOT NULL IDENTITY(1, 1),
    [First Name] VARCHAR(255) NULL,
    [Last Name] VARCHAR(255) NULL,
    [Passport Number] INTEGER NULL,
    [Date of Birth] VARCHAR(255),
    [Booking_ID] INTEGER NULL,
    PRIMARY KEY ([PassengersID])
);
GO

INSERT INTO Passengers([First Name],[Last Name],[Passport Number],[Date of Birth],[Booking_ID]) 
VALUES
    ('Zephr','Estrada',9892,'18/03/20',3198),
    ('Nicole','Castro',8628,'27/10/19',4241),
    ('Ingrid','Long',6331,'15/06/20',801),
    ('Maite','Copeland',6078,'24/09/19',4398),
    ('Kathleen','Nielsen',3534,'12/05/20',2391),
    ('Addison','Wyatt',2772,'15/12/19',392),
    ('Merritt','Stanton',938,'12/05/20',4809),
    ('Alden','Heath',3400,'20/07/19',4506),
    ('Ciaran','Jordan',1444,'20/08/19',69),
    ('Noble','Miller',8404,'20/02/20',1936);
INSERT INTO Passengers([First Name],[Last Name],[Passport Number],[Date of Birth],[Booking_ID]) VALUES('Lynn','Joyce',8455,'25/02/20',4394),('Merrill','Sanders',5111,'30/04/20',2426),('Minerva','Banks',6560,'22/05/20',1750),('Laith','Fleming',5034,'18/05/20',4167),('Plato','Hart',4594,'08/01/20',1501),('Jesse','Mercer',9454,'11/02/20',3919),('Fritz','Ford',3982,'24/03/20',859),('Harding','Hawkins',9300,'22/08/19',4430),('Demetrius','Wolf',4349,'26/01/20',1755),('Leila','Grant',6806,'30/11/19',1985);
INSERT INTO Passengers([First Name],[Last Name],[Passport Number],[Date of Birth],[Booking_ID]) VALUES('Sheila','Richards',9370,'14/11/19',2186),('Simone','House',1876,'04/10/19',1087),('Angela','Phillips',3567,'19/04/20',3548),('Charissa','Sanford',5283,'12/04/20',2366),('Colleen','Slater',1210,'16/03/20',248),('Edan','Barr',9296,'08/08/19',45),('Lucian','Bowers',2923,'11/07/20',3108),('Josiah','Carson',2376,'17/05/20',3135),('Berk','Hammond',6820,'17/06/20',3116),('Galvin','Sims',5721,'25/07/19',1408);
INSERT INTO Passengers([First Name],[Last Name],[Passport Number],[Date of Birth],[Booking_ID]) VALUES('Thor','Delaney',6790,'24/11/19',1782),('Fay','Figueroa',6536,'22/01/20',4079),('Lewis','Snider',287,'15/09/19',2574),('Karen','Rhodes',25,'05/10/19',257),('Wynter','Shannon',4941,'02/05/20',2565),('Kirsten','Pace',8082,'07/12/19',3916),('Basil','Pennington',204,'24/03/20',1487),('Imani','Drake',1756,'19/03/20',4618),('Xandra','Guerra',2654,'19/05/20',3749),('Keane','Delgado',1923,'21/07/19',4266);
INSERT INTO Passengers([First Name],[Last Name],[Passport Number],[Date of Birth],[Booking_ID]) VALUES('Celeste','Lott',4674,'19/02/20',4963),('Patrick','Norton',2994,'03/09/19',4728),('Bertha','Mcgowan',131,'11/07/20',737),('Hope','Clayton',7948,'25/11/19',3521),('Melissa','Ratliff',3950,'26/07/19',311),('Lillian','Horton',868,'02/07/20',3635),('Kerry','Gibbs',5350,'22/12/19',4178),('Lara','Marsh',3814,'09/06/20',898),('Colleen','Alston',4725,'28/10/19',557),('Boris','Cherry',8920,'01/08/19',240);
INSERT INTO Passengers([First Name],[Last Name],[Passport Number],[Date of Birth],[Booking_ID]) VALUES('Peter','Buckner',8530,'11/07/20',1335),('Courtney','Church',1042,'15/01/20',2086),('Hamilton','Fleming',5903,'23/04/20',2388),('Bianca','Camacho',3609,'13/06/20',3103),('Kareem','Sears',4270,'12/01/20',895),('Wang','Fuentes',5785,'18/12/19',1369),('Blaze','Serrano',3686,'15/03/20',4961),('Taylor','Montoya',6219,'26/11/19',750),('Hop','Wooten',6084,'08/04/20',3769),('Elijah','Hensley',1472,'10/04/20',4461);
INSERT INTO Passengers([First Name],[Last Name],[Passport Number],[Date of Birth],[Booking_ID]) VALUES('Maris','Richards',4284,'29/06/20',289),('Gwendolyn','Sykes',9348,'26/04/20',468),('Doris','Davenport',7765,'27/07/19',2483),('Shoshana','Hutchinson',8747,'25/09/19',2207),('Larissa','Moran',6155,'06/02/20',5),('Robin','Rivers',4983,'10/07/20',4185),('Lucius','Cunningham',1056,'15/05/20',2205),('Jakeem','Puckett',6621,'30/10/19',2146),('Jennifer','Rodriguez',3554,'08/09/19',4586),('Dorothy','Noble',1138,'09/02/20',4690);
INSERT INTO Passengers([First Name],[Last Name],[Passport Number],[Date of Birth],[Booking_ID]) VALUES('Cameron','Hernandez',9858,'25/02/20',3167),('Mason','Fry',4619,'15/10/19',2498),('Kaye','Mercer',7748,'22/07/19',3765),('Walter','Fisher',6652,'20/05/20',267),('Emily','Cote',5963,'16/08/19',4250),('Joseph','Pace',5061,'20/12/19',3688),('Kevyn','Hoover',6844,'09/06/20',3129),('Harrison','Burns',7175,'17/04/20',1302),('Susan','Prince',9036,'18/11/19',1550),('Clarke','White',4130,'20/08/19',2646);
INSERT INTO Passengers([First Name],[Last Name],[Passport Number],[Date of Birth],[Booking_ID]) VALUES('Lester','Holt',6495,'16/07/19',4961),('Lani','Blevins',8276,'27/11/19',2731),('Abra','Ortega',1644,'03/09/19',1658),('Clarke','Everett',4906,'17/02/20',3532),('Emery','Blanchard',2097,'29/12/19',1483),('Irma','Maldonado',7768,'07/07/20',1095),('Mara','Hubbard',6462,'12/07/20',2765),('Quynn','Charles',9418,'20/07/19',333),('Hollee','Sellers',8852,'18/06/20',3990),('Elton','Mcpherson',1448,'26/05/20',3350);
INSERT INTO Passengers([First Name],[Last Name],[Passport Number],[Date of Birth],[Booking_ID]) VALUES('Oleg','Foley',1745,'08/06/20',1578),('Ingrid','Gillespie',7684,'02/07/20',3609),('Ivor','Pope',9358,'19/10/19',950),('Evan','Maldonado',8467,'09/12/19',3685),('Neville','Gill',5553,'21/06/20',4534),('Paki','Burke',9233,'30/07/19',4189),('Dennis','Chen',8486,'03/01/20',3092),('Danielle','Oneil',1409,'16/09/19',1488),('Justine','Hoffman',277,'09/08/19',1896),('Tamara','Sanchez',9891,'17/11/19',3783);


SELECT [First Name] FROM [Passengers];
SELECT [Passport Number] FROM [Passengers];
SELECT * FROM [Passengers];