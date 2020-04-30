import mysql.connector

class backendFlight:
    def __init__(self):
        self.mydb = mysql.connector.connect(host="localhost",user="root",passwd="40@Vaibhav",database = 'dbms',autocommit=True)
        # self.mydb = mysql.connector.connect(host="localhost",user="root",passwd="admin",database = 'finalproject',auth_plugin='mysql_native_password',autocommit=True)
        # self.mydb = mysql.connector.connect(user='rhythm', password='password',
        #                                    host='127.0.0.1',
        #                                    database='proj')
        self.mycursor = self.mydb.cursor()
        self.countries = []
        self.cities = []
        self.getAirport()

    def getAirport(self):
        self.cities = []
        self.countries = []
        self.mycursor.execute("Select distinct country from airport order by country")
        for country in self.mycursor:
            self.countries.append(country[0])
        self.mycursor.execute("Select distinct city from airport order by city")
        for city in self.mycursor:
            self.cities.append(city[0])

    def getAllAirports(self):
        self.mycursor.execute("Select name from airport")
        out = [i[0] for i in self.mycursor]
        return out

    def getFlightIDs(self):
        self.mycursor.execute("Select flight_id from flight order by flight_id")
        out = [str(i[0]) for i in self.mycursor]
        return out

    def getAirlines(self):
        self.mycursor.execute("Select Name from airlines")
        out = [i[0] for i in self.mycursor]
        return out
    def getFlights(self,city):
        print('selected city is {}'.format(city))

        queryResult = []

        self.mycursor.execute('Select * from flight where dest_airport in (Select id from airport where city = \'{}\')'.format(city))

        for i in self.mycursor:

            queryResult.append(i)

        result = []

        for i in queryResult:
            #print(type(i))
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


        id = flight_tuple[0]
        self.mycursor.execute('Select Name from airlines where ID = {}'.format(flight_tuple[1]))
        for i in self.mycursor:
            airline =i[0]
        self.mycursor.execute('select Cost from booking where Flight_id = \'{}\' and Booked = 0'.format(flight_tuple[0]))
        numseats = 0
        cost = 0
        for i in self.mycursor:
            numseats+=1
            cost+=i[0]
        self.mycursor.execute('Select distinct name from airport where id = \'{}\''.format(flight_tuple[2]))
        for i in self.mycursor:
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
        entry['avgCost'] = int(cost/numseats)


        return entry

    def addBalance(self, userid, balance):
        balance += 10000
        self.mycursor.execute('update customer set balance = \'{0}\' where id = \'{1}\''.format(balance, userid))
        self.mydb.commit()
    def bookSeats(self, flightId, numSeats, userid, balance):
        print("Hello")
        cost = 0
        # self.mycursor.execute('select * from flight where flight_id = \'{}\')'.format(flightId))
        self.mycursor.execute('select * from booking where Flight_id = \'{}\' and Booked = 0 order by Seat_No'.format(flightId))
        results = self.mycursor.fetchall()
        availableSeats = 0
        cost = 0
        seatlist = [balance]
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

        if (balance < cost ):
            return [-1]

        seatlist[0] -= cost
        self.mycursor.execute('update customer set balance = \'{0}\' where id = \'{1}\''.format(seatlist[0], userid))
        self.mydb.commit()

        for i in r_id:
            print(i)
            try:
                self.mycursor.execute('update booking set Booked = true, Passenger_id = \'{0}\' where r_id = \'{1}\';'.format(userid, i))
                self.mydb.commit()
            except mysql.connector.Error as error:
                print(error)


        return seatlist

    def validateAirport(self, name):
        self.mycursor.execute("Select name from airport")
        out = [i[0] for i in self.mycursor]
        if (name in out):
            return False
        return True

    def addAirport(self, name, country , city):
        print("I will add airport {0}, country {1}, city {2}".format(name, country, city))
        self.mycursor.execute('select max(id) from airport;')
        indx = 0
        for i in self.mycursor:
            indx = i[0]
        indx+=1
        self.mycursor.execute('insert into airport(id, country, city, name) values (\'{0}\', \'{1}\',\'{2}\',\'{3}\') ;'.format(indx, country, city, name))

    def addAirline(self, name, mail):
        print("I will add airline {0}, contact {1} ".format(name, mail))
        self.mycursor.execute('select max(ID) from airlines;')
        indx = 0
        for i in self.mycursor:
            indx = i[0]
        indx+=1
        self.mycursor.execute('insert into airlines(ID, Name, Contact) values (\'{0}\', \'{1}\',\'{2}\') ;'.format(indx, name, mail))

    def addFlight(self, airline, airport, departure, arrival):
        print("I will add flight of airline {0}, destination airport {1}, departure time {2}, arrival time {3} ".format(airline, airport, departure, arrival))
        self.mycursor.execute('select max(flight_id) from flight;')
        indx = 0
        airlineId = 0
        airportId = 0
        for i in self.mycursor:
            indx = i[0]
        indx+=1
        self.mycursor.execute('select ID from airlines where Name = \'{0}\''.format(airline))
        for i in self.mycursor:
            airlineId = i[0]
        self.mycursor.execute('select id from airport where name = \'{0}\''.format(airport))
        for i in self.mycursor:
            airportId = i[0]

        self.mycursor.execute('insert into flight(flight_id, airline, dest_airport, departure, arrival) values (\'{0}\', \'{1}\',\'{2}\',\'{3}\',\'{4}\') ;'.format(indx, airlineId, airportId, departure, arrival))
        return indx
    def validateTicketFlight(self, id):
        self.mycursor.execute('select flight_id from flight')
        out = [i[0] for i in self.mycursor]
        if (id in out):
            return True
        return False

    def addTickets(self, flightid, numtickets, price):
        print("I will add tickets for flight : {0}. There are {1} tickets and you'll have to pay {2} for each one of them".format(flightid, numtickets, price))
        self.mycursor.execute('select Flight_id from booking;')
        flag = False
        indx2 = 0
        for i in self.mycursor:
            indx2+=1
            if (flightid==i[0]):
                flag = True

        indx2+=1
        if not(flag):
            for i in range(numtickets):
                self.mycursor.execute('insert into booking(r_id, Flight_id, Seat_No, Booked, Passenger_id, Cost) values (\'{0}\', \'{1}\',\'{2}\',false, NULL, \'{3}\') ;'.format(indx2+i, flightid, i+1, price))
        else:
            self.mycursor.execute('select max(Seat_No) from booking where Flight_id = \'{0}\';'.format(flightid))
            seatno = 0
            for i in self.mycursor:
                seatno = i[0]
            seatno+=1
            for i in range(numtickets):
                self.mycursor.execute('insert into booking(r_id, Flight_id, Seat_No, Booked, Passenger_id, Cost) values (\'{0}\', \'{1}\',\'{2}\',false, NULL, \'{3}\') ;'.format(indx2+i, flightid, seatno+i, price))

    def removeFlight(self, id):
        print("I will delete flight No. {0}".format(id))

        self.mycursor.execute('delete from booking where Flight_id = \'{0}\''.format(id))
        self.mycursor.execute('delete from flight where flight_id = \'{0}\''.format(id))

    def removeAirline(self, name):
        print("I will delete Airline : {0}".format(name))
        self.mycursor.execute('select ID from airlines where Name = \'{0}\''.format(name))
        id = 0
        for i in self.mycursor:
            id = i[0]
        self.mycursor.execute('select flight_id from flight where airline = \'{0}\''.format(id))
        arr = [i[0] for i in self.mycursor]
        for i in arr:
            self.removeFlight(i)
        self.mycursor.execute('delete from airlines where Name = \'{0}\''.format(name))
