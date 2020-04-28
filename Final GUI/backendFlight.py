import mysql.connector

class customer:
    def __init__(self, arr):
        self.id = arr[3]
        self.balance = arr[5]

class backendFlight:
    def __init__(self):
        # self.mydb = mysql.connector.connect(host = "127.0.0.1", user = "root", passwd = "40@Vaibhav", database = "dbms")
        self.mydb = mysql.connector.connect(host="localhost",user="root",passwd="admin",database = 'finalproject',auth_plugin='mysql_native_password',autocommit=True)
        # self.mydb = mysql.connector.connect(user='root', password='40@Vaibhav',
        #                                    host='127.0.0.1',
        #                                    database='dbms')
        self.mycursor = self.mydb.cursor()
        self.countries = []
        self.cities = []
        self.getAirport()
        self.mycustomer = customer(['Sam','Alsop','sam.alsop@gmail.com',1,'M',60144])

    def getAirport(self):
        self.mycursor.execute("Select distinct country from airport order by country")
        for country in self.mycursor:
            self.countries.append(country[0])
        self.mycursor.execute("Select distinct city from airport order by city")
        for city in self.mycursor:
            self.cities.append(city[0])

    def getFlights(self,city):
        print('selected city is {}'.format(city))

        queryResult = []

        self.mycursor.execute('Select * from flight where dest_airport in (Select id from airport where city = \'{}\')'.format(city))

        for i in self.mycursor:

            queryResult.append(i)

        result = []

        for i in queryResult:
            print(type(i))
            print(i)
            result.append(self.flightinfo(i))
        return result

    def city4country(self, country):
        self.mycursor.execute('Select distinct city from airport where country = \'{}\' order by city'.format(country))
        mycity = []
        for city in self.mycursor:
            mycity.append(city[0])

        return mycity
    def flightinfo(self, flight_tuple):


        cursor2 = self.mydb.cursor()
        id = flight_tuple[0]
        cursor2.execute('Select Name from airlines where ID = {}'.format(flight_tuple[1]))
        for i in cursor2:
            airline =i[0]
        self.mycursor.execute('select count(*) from booking where Flight_id = \'{}\' and Booked = 0'.format(flight_tuple[0]))
        numseats = 0
        for i in self.mycursor:
            numseats = i[0]
        cursor2.execute('Select distinct name from airport where id = \'{}\''.format(flight_tuple[2]))
        for i in cursor2:
            airport =i[0]
        departure = flight_tuple[3]
        arrival = flight_tuple[4]
        entry = {}
        entry['id'] = id
        entry['departure'] = departure
        entry['arrival'] = arrival
        entry['airport'] = airport
        entry['airline'] = airline
        entry['numseats'] = numseats
        entry['duration'] = arrival-departure



        return entry

    def bookSeats(self, flightId, numSeats):
        print("Hello")
        cost = 0
        # self.mycursor.execute('select * from flight where flight_id = \'{}\')'.format(flightId))
        self.mycursor.execute('select * from booking where Flight_id = \'{}\' and Booked = 0 order by Seat_No'.format(flightId))
        results = self.mycursor.fetchall()
        availableSeats = 0
        cost = 0
        seatlist = []
        r_id = []
        for i in results:
            print(type(i))
            print(i)
            availableSeats+=1
            cost += i[5]
            seatlist.append(i[2])
            r_id.append(i[0])
            if (availableSeats == numSeats):
                break
        if (numSeats>availableSeats):

            return 1

        if (self.mycustomer.balance < cost ):
            return 1

        self.mycustomer.balance -= cost

        # check seats available return 1 if not enough
        #cost = cost * numSeats
        # check balance return 2 if not enough

        # deduct balance
        # mark seats return list of seatsNo

        for i in r_id:
            print(i)
            try:
                self.mycursor.execute('update test_schema.booking set Booked = true, Passenger_id = \'{0}\' where r_id = \'{1}\';'.format(self.mycustomer.id, i))
                self.mydb.commit()
            except mysql.connector.Error as error:
                print(error)
            #print(self.mycursor.fetchall())
        BookingNumber = 10
        return seatlist

class AdminBackend:
    def __init__(self):
        self.mydb = mysql.connector.connect(host = "127.0.0.1", user = "rhuthmos", passwd = "VinayG$2303", database = "test_schema")
        self.mycursor = self.mydb.cursor()

    def getPassengers(self, flightId):
        result = []
        self.mycursor.execute('select distinct Passenger_id from booking where Flight_id = \'{}\' ;'.format(flightId))
        for i in self.mycursor:
            result.append(i)

    def addFlight(self, airportId,airlineId, dep_time, arr_time, numseats, price):
        self.mycursor.execute('select max(flight_id) from flight;')
        indx = 0
        for i in self.mycursor:
            indx = i[0]
        indx+=1
        self.mycursor.execute('insert into flight(flight_id, airline, dest_airport, departure, arrival) values (\'{0}\', \'{1}\',\'{2}\',\'{3}\',\'{4}\') ;'.format(indx, airlineId, airportId, dep_time, arr_time))
        self.mycursor.execute('select max(r_id) from booking;')
        indx2 = 0
        for i in self.mycursor:
            indx2 = i[0]
        indx2+=1
        for i in range(numseats):
            self.mycursor.execute('insert into booking(r_id, Flight_id, Seat_No, Booked, Passenger_id, Cost) values (\'{0}\', \'{1}\',\'{2}\',\'{3}\',\'{4}\', \'{5}\') ;'.format(indx2, indx, i+1, false, NULL, price))

    def removeFlight(self, flightid):
        self.mycursor.execute('delete from flight where flight_id =  \'{}\';'.format(flightid))
        self.mycursor.execute('delete from booking where Flight_id = \'{}\''.format(flightid))
