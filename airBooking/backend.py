import mysql.connector

class customer:
    def __init__(self, arr):
        self.id = arr[3]
        self.balance = arr[5]

class backend:
    def __init__(self):
        self.mydb = mysql.connector.connect(host = "127.0.0.1", user = "rhuthmos", passwd = "password", database = "air-booking")
        self.mycursor = self.mydb.cursor()
        self.countries = []
        self.cities = []
        self.getAirport()
        self.mycustomer = customer(['Sam','Alsop','sam.alsop@gmail.com',1,'M',6144])

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
        self.mycursor.execute('Select * from flights where destination_airport_id in (Select id from airport where city = \'{}\')'.format(city))
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
        self.mycursor.execute('select count(*) from bookings where Flight_id = \'{}\' and Booked = "false"'.format(flight_tuple[0]))
        numseats = 0
        for i in self.mycursor:
            numseats = i
        cursor2.execute('Select distinct name from airport where id = \'{}\''.format(flight_tuple[2]))
        for i in cursor2:
            airport =i[0]
        destination = flight_tuple[3]
        arrival = flight_tuple[4]
        return (id,airline,airport,destination,arrival, numseats)
    
    def bookSeats(self, flightId, numSeats):
        print("Hello")
        # cost = 0
        # self.mycursor.execute('select * from flights where id = \'{}\')'.format(flightId))
        # self.mycursor.execute('select * from booking where id = \'{}\' and Booked = False order by SeatNo)'.format(flightId))
        
        # availableSeats = 0
        # cost = 0
        # seatlist = []
        # r_id = []
        # for i in self.cursor:
        #     availableSeats+=1
        #     cost += i[4]
        #     seatlist.append(i[3])
        #     r_id.append(i[0])
        # if (numSeats>availableSeats):
        #     return 1
        
        # if (self.mycustomer.balance < cost ):
        #     return 1
        
        # self.mycustomer.balance -= cost

        # # check seats available return 1 if not enough
        # #cost = cost * numSeats
        # # check balance return 2 if not enough

        # # deduct balance
        # # mark seats return list of seatsNo
        
        # for i in r_id:
        #     self.mycursor.execute('update booking set Booked = True where r_id = {}', id)
        # BookingNumber = 10
        # return seatlist, BookingNumber



