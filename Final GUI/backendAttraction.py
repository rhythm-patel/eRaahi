import mysql.connector


class backendAttraction:
    def __init__(self):
        self.cnx = mysql.connector.connect(user='root', password='40@Vaibhav',
                                           host='127.0.0.1',
                                           database='dbms')
        # self.cnx = mysql.connector.connect(host="localhost",user="root",passwd="admin",database = 'finalproject',auth_plugin='mysql_native_password',autocommit=True)
        # self.cnx = mysql.connector.connect(user='rhythm', password='password',
        #                                    host='127.0.0.1',
        #                                    database='proj')
        self.cur = self.cnx.cursor(buffered=True)

        self.getAttractions()

    def getIDs(self):
    	self.IDs = []
    	self.cur.execute('select Attraction_ID from Attraction')
    	for ids in self.cur:
    		self.IDs.append(ids)
    	return self.IDs

    def updateAttractions(self,Attraction_ID,Name_of_Attraction,Summary,Duration,Start_Time,Cost,Type):
        self.cur.execute('update Attraction set Name_of_Attraction = %s where Attraction_ID = %s',(str(Name_of_Attraction),str(Attraction_ID)))
        self.cur.execute('update Attraction set Summary = %s where Attraction_ID = %s',(str(Summary),str(Attraction_ID)))
        self.cur.execute('update Attraction set Duration = %s where Attraction_ID = %s',(str(Duration),str(Attraction_ID)))
        self.cur.execute('update Attraction set Start_Time = %s where Attraction_ID = %s',(str(Start_Time),str(Attraction_ID)))
        self.cur.execute('update Attraction set Cost = %s where Attraction_ID = %s',(str(Cost),str(Attraction_ID)))
        self.cur.execute('update Attraction set Type = %s where Attraction_ID = %s',(str(Type),str(Attraction_ID)))
        self.cnx.commit()

    def addAttractions(self,Attraction_ID,Name_of_Attraction,Summary,Duration,Start_Time,Cost,Type):
        self.cur.execute('INSERT INTO Attraction (Attraction_ID, Name_of_Attraction, Summary, Duration, Start_Time, Cost, Type) VALUES (%s, %s, %s, %s, %s, %s, %s)',(str(Attraction_ID),str(Name_of_Attraction),str(Summary),str(Duration),str(Start_Time),str(Cost),str(Type)))
        self.cnx.commit()

    def getAttractions(self):
        self.attractions = []
        self.cur.execute(
            'select Name_of_Attraction, Type, Summary, Duration, Start_Time, Cost from Attraction')
        for attraction in self.cur:
            self.attractions.append(attraction)
        return self.attractions

    def durationAsc(self):
        self.attractions = []
        self.cur.execute(
            'select Name_of_Attraction, Type, Summary, Duration, Start_Time, Cost from Attraction order by Duration Asc')
        for attraction in self.cur:
            self.attractions.append(attraction)
        return self.attractions

    def durationDesc(self):
        self.attractions = []
        self.cur.execute(
            'select Name_of_Attraction, Type, Summary, Duration, Start_Time, Cost from Attraction order by Duration Desc')
        for attraction in self.cur:
            self.attractions.append(attraction)
        return self.attractions

    def startTimeAsc(self):
        self.attractions = []
        self.cur.execute(
            'select Name_of_Attraction, Type, Summary, Duration, Start_Time, Cost from Attraction order by Start_Time Asc')
        for attraction in self.cur:
            self.attractions.append(attraction)
        return self.attractions

    def startTimeDesc(self):
        self.attractions = []
        self.cur.execute(
            'select Name_of_Attraction, Type, Summary, Duration, Start_Time, Cost from Attraction order by Start_Time Desc')
        for attraction in self.cur:
            self.attractions.append(attraction)
        return self.attractions

    def costAsc(self):
        self.attractions = []
        self.cur.execute(
            'select Name_of_Attraction, Type, Summary, Duration, Start_Time, Cost from Attraction order by Cost Asc')
        for attraction in self.cur:
            self.attractions.append(attraction)
        return self.attractions

    def costDesc(self):
        self.attractions = []
        self.cur.execute(
            'select Name_of_Attraction, Type, Summary, Duration, Start_Time, Cost from Attraction order by Cost Desc')
        for attraction in self.cur:
            self.attractions.append(attraction)
        return self.attractions
