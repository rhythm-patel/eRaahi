CREATE TABLE movie_booking(
   Book_id  INTEGER  NOT NULL PRIMARY KEY
  ,Movie_Id INTEGER  NOT NULL
  ,Hall_id  INTEGER  NOT NULL
  ,date     DATE  NOT NULL
  ,Cost     INTEGER  NOT NULL
  ,Slots    INTEGER  NOT NULL
  ,FOREIGN KEY(Movie_Id) REFERENCES Movies(Movie_Id)
  ,FOREIGN KEY(Hall_id) REFERENCES hall(Hall_id)

);
INSERT INTO movie_booking(Book_id,Movie_Id,Hall_id,date,Cost,Slots) VALUES (1,1,1,'07/08/20',100,1);
INSERT INTO movie_booking(Book_id,Movie_Id,Hall_id,date,Cost,Slots) VALUES (2,2,2,'07/01/21',200,3);
INSERT INTO movie_booking(Book_id,Movie_Id,Hall_id,date,Cost,Slots) VALUES (3,3,3,'23/12/20',150,4);
INSERT INTO movie_booking(Book_id,Movie_Id,Hall_id,date,Cost,Slots) VALUES (4,4,4,'13/07/20',250,2);
INSERT INTO movie_booking(Book_id,Movie_Id,Hall_id,date,Cost,Slots) VALUES (5,5,5,'29/01/21',300,3);
INSERT INTO movie_booking(Book_id,Movie_Id,Hall_id,date,Cost,Slots) VALUES (6,6,6,'25/07/19',400,4);
INSERT INTO movie_booking(Book_id,Movie_Id,Hall_id,date,Cost,Slots) VALUES (7,7,7,'18/08/20',500,2);
INSERT INTO movie_booking(Book_id,Movie_Id,Hall_id,date,Cost,Slots) VALUES (8,8,8,'13/11/19',350,3);
INSERT INTO movie_booking(Book_id,Movie_Id,Hall_id,date,Cost,Slots) VALUES (9,9,9,'27/03/21',100,4);
INSERT INTO movie_booking(Book_id,Movie_Id,Hall_id,date,Cost,Slots) VALUES (10,10,10,'16/02/20',200,2);
INSERT INTO movie_booking(Book_id,Movie_Id,Hall_id,date,Cost,Slots) VALUES (11,11,11,'15/05/19',150,1);
INSERT INTO movie_booking(Book_id,Movie_Id,Hall_id,date,Cost,Slots) VALUES (12,12,12,'09/05/20',250,3);
INSERT INTO movie_booking(Book_id,Movie_Id,Hall_id,date,Cost,Slots) VALUES (13,13,13,'24/07/19',300,2);
INSERT INTO movie_booking(Book_id,Movie_Id,Hall_id,date,Cost,Slots) VALUES (14,14,14,'13/10/20',400,4);
INSERT INTO movie_booking(Book_id,Movie_Id,Hall_id,date,Cost,Slots) VALUES (15,15,15,'21/01/20',500,3);
INSERT INTO movie_booking(Book_id,Movie_Id,Hall_id,date,Cost,Slots) VALUES (16,16,1,'14/11/20',350,2);
INSERT INTO movie_booking(Book_id,Movie_Id,Hall_id,date,Cost,Slots) VALUES (17,17,2,'23/08/20',100,1);
INSERT INTO movie_booking(Book_id,Movie_Id,Hall_id,date,Cost,Slots) VALUES (18,18,3,'01/01/20',200,2);
INSERT INTO movie_booking(Book_id,Movie_Id,Hall_id,date,Cost,Slots) VALUES (19,19,4,'29/08/20',400,4);
INSERT INTO movie_booking(Book_id,Movie_Id,Hall_id,date,Cost,Slots) VALUES (20,20,5,'24/01/20',500,3);
INSERT INTO movie_booking(Book_id,Movie_Id,Hall_id,date,Cost,Slots) VALUES (21,21,6,'26/05/20',350,2);
INSERT INTO movie_booking(Book_id,Movie_Id,Hall_id,date,Cost,Slots) VALUES (22,22,7,'09/05/20',100,4);
INSERT INTO movie_booking(Book_id,Movie_Id,Hall_id,date,Cost,Slots) VALUES (23,23,8,'12/11/20',400,2);
INSERT INTO movie_booking(Book_id,Movie_Id,Hall_id,date,Cost,Slots) VALUES (24,24,9,'04/12/20',500,1);
INSERT INTO movie_booking(Book_id,Movie_Id,Hall_id,date,Cost,Slots) VALUES (25,25,10,'31/10/19',350,2);
INSERT INTO movie_booking(Book_id,Movie_Id,Hall_id,date,Cost,Slots) VALUES (26,26,11,'12/05/20',100,1);
INSERT INTO movie_booking(Book_id,Movie_Id,Hall_id,date,Cost,Slots) VALUES (27,27,12,'01/06/19',200,1);
INSERT INTO movie_booking(Book_id,Movie_Id,Hall_id,date,Cost,Slots) VALUES (28,28,13,'27/06/20',400,3);
INSERT INTO movie_booking(Book_id,Movie_Id,Hall_id,date,Cost,Slots) VALUES (29,29,14,'26/12/20',500,4);
INSERT INTO movie_booking(Book_id,Movie_Id,Hall_id,date,Cost,Slots) VALUES (30,30,15,'25/08/20',350,3);
INSERT INTO movie_booking(Book_id,Movie_Id,Hall_id,date,Cost,Slots) VALUES (31,31,1,'30/12/20',100,2);
INSERT INTO movie_booking(Book_id,Movie_Id,Hall_id,date,Cost,Slots) VALUES (32,32,2,'19/12/19',200,2);
INSERT INTO movie_booking(Book_id,Movie_Id,Hall_id,date,Cost,Slots) VALUES (34,34,3,'01/03/21',400,3);
INSERT INTO movie_booking(Book_id,Movie_Id,Hall_id,date,Cost,Slots) VALUES (36,36,4,'23/12/19',100,4);
INSERT INTO movie_booking(Book_id,Movie_Id,Hall_id,date,Cost,Slots) VALUES (38,38,5,'04/03/21',200,3);
INSERT INTO movie_booking(Book_id,Movie_Id,Hall_id,date,Cost,Slots) VALUES (39,39,6,'20/12/20',400,2);
INSERT INTO movie_booking(Book_id,Movie_Id,Hall_id,date,Cost,Slots) VALUES (40,40,7,'16/07/19',500,2);
INSERT INTO movie_booking(Book_id,Movie_Id,Hall_id,date,Cost,Slots) VALUES (41,41,8,'27/03/21',350,1);
INSERT INTO movie_booking(Book_id,Movie_Id,Hall_id,date,Cost,Slots) VALUES (42,42,9,'10/04/20',100,4);
INSERT INTO movie_booking(Book_id,Movie_Id,Hall_id,date,Cost,Slots) VALUES (43,43,10,'26/07/19',400,3);
INSERT INTO movie_booking(Book_id,Movie_Id,Hall_id,date,Cost,Slots) VALUES (44,44,11,'20/07/20',500,2);
INSERT INTO movie_booking(Book_id,Movie_Id,Hall_id,date,Cost,Slots) VALUES (45,45,12,'18/05/19',350,1);
INSERT INTO movie_booking(Book_id,Movie_Id,Hall_id,date,Cost,Slots) VALUES (46,46,13,'24/08/20',100,1);
INSERT INTO movie_booking(Book_id,Movie_Id,Hall_id,date,Cost,Slots) VALUES (47,47,14,'02/04/20',200,4);
INSERT INTO movie_booking(Book_id,Movie_Id,Hall_id,date,Cost,Slots) VALUES (48,48,15,'08/06/20',400,3);
INSERT INTO movie_booking(Book_id,Movie_Id,Hall_id,date,Cost,Slots) VALUES (49,49,1,'26/08/19',500,2);
INSERT INTO movie_booking(Book_id,Movie_Id,Hall_id,date,Cost,Slots) VALUES (50,50,2,'08/07/19',350,1);
