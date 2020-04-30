CREATE INDEX hnameindex ON hotel(name);
CREATE INDEX cnameindex ON customer(firstname);
CREATE INDEX hhotelfeedbackidindex ON hotel_feedback(hotel_id);
CREATE INDEX room_hotel_id_index ON room(hotel_id);
CREATE INDEX hotel_booking_cust_id_index ON hotel_booking(cust_id);