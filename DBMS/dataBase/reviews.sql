CREATE TABLE reviews(
   Movie_Id    INTEGER  NOT NULL
  ,Rating      INTEGER  NOT NULL
  ,customer_id INTEGER  NOT NULL
  ,PRIMARY KEY(Movie_Id,customer_id)
  ,FOREIGN KEY(Movie_Id) REFERENCES Movies(Movie_Id)

);
INSERT INTO reviews(Movie_Id,Rating,customer_id) VALUES (1,4,1);
INSERT INTO reviews(Movie_Id,Rating,customer_id) VALUES (2,4,2);
INSERT INTO reviews(Movie_Id,Rating,customer_id) VALUES (3,4,3);
INSERT INTO reviews(Movie_Id,Rating,customer_id) VALUES (4,5,4);
INSERT INTO reviews(Movie_Id,Rating,customer_id) VALUES (5,5,5);
INSERT INTO reviews(Movie_Id,Rating,customer_id) VALUES (6,3,6);
INSERT INTO reviews(Movie_Id,Rating,customer_id) VALUES (7,5,7);
INSERT INTO reviews(Movie_Id,Rating,customer_id) VALUES (8,4,8);
INSERT INTO reviews(Movie_Id,Rating,customer_id) VALUES (9,5,9);
INSERT INTO reviews(Movie_Id,Rating,customer_id) VALUES (10,5,10);
INSERT INTO reviews(Movie_Id,Rating,customer_id) VALUES (11,5,11);
INSERT INTO reviews(Movie_Id,Rating,customer_id) VALUES (12,5,12);
INSERT INTO reviews(Movie_Id,Rating,customer_id) VALUES (13,3,13);
INSERT INTO reviews(Movie_Id,Rating,customer_id) VALUES (14,5,14);
INSERT INTO reviews(Movie_Id,Rating,customer_id) VALUES (15,4,15);
INSERT INTO reviews(Movie_Id,Rating,customer_id) VALUES (16,5,16);
INSERT INTO reviews(Movie_Id,Rating,customer_id) VALUES (17,3,17);
INSERT INTO reviews(Movie_Id,Rating,customer_id) VALUES (18,3,18);
INSERT INTO reviews(Movie_Id,Rating,customer_id) VALUES (19,5,19);
INSERT INTO reviews(Movie_Id,Rating,customer_id) VALUES (20,4,20);
INSERT INTO reviews(Movie_Id,Rating,customer_id) VALUES (21,4,21);
INSERT INTO reviews(Movie_Id,Rating,customer_id) VALUES (22,5,22);
INSERT INTO reviews(Movie_Id,Rating,customer_id) VALUES (23,4,23);
INSERT INTO reviews(Movie_Id,Rating,customer_id) VALUES (24,3,24);
INSERT INTO reviews(Movie_Id,Rating,customer_id) VALUES (25,4,25);
INSERT INTO reviews(Movie_Id,Rating,customer_id) VALUES (26,5,26);
INSERT INTO reviews(Movie_Id,Rating,customer_id) VALUES (27,4,27);
INSERT INTO reviews(Movie_Id,Rating,customer_id) VALUES (28,3,28);
INSERT INTO reviews(Movie_Id,Rating,customer_id) VALUES (29,5,29);
INSERT INTO reviews(Movie_Id,Rating,customer_id) VALUES (30,4,30);
INSERT INTO reviews(Movie_Id,Rating,customer_id) VALUES (31,4,31);
INSERT INTO reviews(Movie_Id,Rating,customer_id) VALUES (32,5,32);
INSERT INTO reviews(Movie_Id,Rating,customer_id) VALUES (34,4,34);
INSERT INTO reviews(Movie_Id,Rating,customer_id) VALUES (36,4,36);
INSERT INTO reviews(Movie_Id,Rating,customer_id) VALUES (38,4,38);
INSERT INTO reviews(Movie_Id,Rating,customer_id) VALUES (39,5,39);
INSERT INTO reviews(Movie_Id,Rating,customer_id) VALUES (40,5,40);
INSERT INTO reviews(Movie_Id,Rating,customer_id) VALUES (41,3,41);
INSERT INTO reviews(Movie_Id,Rating,customer_id) VALUES (42,5,42);
INSERT INTO reviews(Movie_Id,Rating,customer_id) VALUES (43,3,43);
INSERT INTO reviews(Movie_Id,Rating,customer_id) VALUES (44,4,44);
INSERT INTO reviews(Movie_Id,Rating,customer_id) VALUES (45,3,45);
INSERT INTO reviews(Movie_Id,Rating,customer_id) VALUES (46,3,46);
INSERT INTO reviews(Movie_Id,Rating,customer_id) VALUES (47,4,47);
INSERT INTO reviews(Movie_Id,Rating,customer_id) VALUES (48,5,48);
INSERT INTO reviews(Movie_Id,Rating,customer_id) VALUES (49,5,49);
INSERT INTO reviews(Movie_Id,Rating,customer_id) VALUES (50,5,50);
