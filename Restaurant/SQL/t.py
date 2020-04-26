import mysql.connector
conn = mysql.connector.connect(user = 'root', password = '40@Vaibhav', host = 'localhost', database = 'dbms')
cursor = conn.cursor()
# cursor.execute("CREATE TABLE Venue(Venue VARCHAR(47) NOT NULL PRIMARY KEY,Venue_Latitude  NUMERIC(18,15) NOT NULL,Venue_Longitude NUMERIC(21,17) NOT NULL,Venue_Category  VARCHAR(31) NOT NULL,Venue_Id        VARCHAR(24) NOT NULL);")
cursor.execute("CREATE TABLE hotel( Neighbourhood VARCHAR(15) NOT NULL PRIMARY KEY,Neighbourhood_Latitude NUMERIC(10,7) NOT NULL,Neighbour_Longitude    NUMERIC(12,7) NOT NULL);")
# for x in cursor:
# cursor.execute("INSERT INTO Lat_Long(Neighbourhood,Neighbourhood_Latitude,Neighbour_Longitude) VALUES ('New York',40.7127281,-74.0060152);-")
#     print(x)
