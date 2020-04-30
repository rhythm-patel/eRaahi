CREATE TABLE booked(
   id          INTEGER  NOT NULL AUTO_INCREMENT
  ,Book_id     INTEGER  NOT NULL
  ,customer_id INTEGER  NOT NULL
  ,seats       INTEGER  NOT NULL,
  PRIMARY KEY(id),
  FOREIGN KEY(Book_id) REFERENCES movie_booking(Book_id)

);
INSERT INTO booked(Book_id,customer_id,seats) VALUES (1,1,3);
INSERT INTO booked(Book_id,customer_id,seats) VALUES (2,2,3);
INSERT INTO booked(Book_id,customer_id,seats) VALUES (3,3,6);
INSERT INTO booked(Book_id,customer_id,seats) VALUES (4,4,3);
INSERT INTO booked(Book_id,customer_id,seats) VALUES (5,5,2);
INSERT INTO booked(Book_id,customer_id,seats) VALUES (6,6,3);
INSERT INTO booked(Book_id,customer_id,seats) VALUES (7,7,9);
INSERT INTO booked(Book_id,customer_id,seats) VALUES (8,8,4);
INSERT INTO booked(Book_id,customer_id,seats) VALUES (9,9,3);
INSERT INTO booked(Book_id,customer_id,seats) VALUES (10,10,6);
INSERT INTO booked(Book_id,customer_id,seats) VALUES (47,47,3);
INSERT INTO booked(Book_id,customer_id,seats) VALUES (48,48,1);
INSERT INTO booked(Book_id,customer_id,seats) VALUES (49,49,4);
INSERT INTO booked(Book_id,customer_id,seats) VALUES (50,50,2);
