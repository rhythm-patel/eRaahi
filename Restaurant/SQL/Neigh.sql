/* CREATE TABLE */
CREATE TABLE IF NOT EXISTS Neigh(
  Neighbourhood VARCHAR(100), 
  Neighbourhood_Latitude DECIMAL(10, 2), 
  Neighbour_Longitude DECIMAL(10, 2)
);
/* INSERT QUERY */
INSERT INTO Neigh(
  Neighbourhood, Neighbourhood_Latitude, 
  Neighbour_Longitude
) 
VALUES 
  (
    'New York', 40.7127281,-74.0060152
  );
/* INSERT QUERY */
INSERT INTO Neigh(
  Neighbourhood, Neighbourhood_Latitude, 
  Neighbour_Longitude
) 
VALUES 
  (
    'San Francisco', 37.7790262,-122.4199061
  );
/* INSERT QUERY */
INSERT INTO Neigh(
  Neighbourhood, Neighbourhood_Latitude, 
  Neighbour_Longitude
) 
VALUES 
  (
    'Charlotte', 35.2270869,-80.8431268
  );
/* INSERT QUERY */
INSERT INTO Neigh(
  Neighbourhood, Neighbourhood_Latitude, 
  Neighbour_Longitude
) 
VALUES 
  (
    'Boston', 42.3602534,-71.0582912
  );
/* INSERT QUERY */
INSERT INTO Neigh(
  Neighbourhood, Neighbourhood_Latitude, 
  Neighbour_Longitude
) 
VALUES 
  (
    'Connaught Place', 28.6313827, 77.2197924
  );
/* INSERT QUERY */
INSERT INTO Neigh(
  Neighbourhood, Neighbourhood_Latitude, 
  Neighbour_Longitude
) 
VALUES 
  ('Berlin', 52.5170365, 13.3888599);
