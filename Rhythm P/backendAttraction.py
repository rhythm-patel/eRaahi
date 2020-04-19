import mysql.connector


class backendAttraction:
    def __init__(self):
        self.cnx = mysql.connector.connect(user='rhythm', password='password',
                                           host='127.0.0.1',
                                           database='proj')
        self.cur = self.cnx.cursor(buffered=True)

        self.getAttractions()

    def getAttractions(self):
        self.attractions = []
        self.cur.execute(
            'select Name_of_Attraction, Type, Summary, Duration, Start_Time, Cost from attraction')
        for attraction in self.cur:
            self.attractions.append(attraction)
        return self.attractions

    def durationAsc(self):
        self.attractions = []
        self.cur.execute(
            'select Name_of_Attraction, Type, Summary, Duration, Start_Time, Cost from attraction order by Duration Asc')
        for attraction in self.cur:
            self.attractions.append(attraction)
        return self.attractions

    def durationDesc(self):
        self.attractions = []
        self.cur.execute(
            'select Name_of_Attraction, Type, Summary, Duration, Start_Time, Cost from attraction order by Duration Desc')
        for attraction in self.cur:
            self.attractions.append(attraction)
        return self.attractions

    def startTimeAsc(self):
        self.attractions = []
        self.cur.execute(
            'select Name_of_Attraction, Type, Summary, Duration, Start_Time, Cost from attraction order by Start_Time Asc')
        for attraction in self.cur:
            self.attractions.append(attraction)
        return self.attractions

    def startTimeDesc(self):
        self.attractions = []
        self.cur.execute(
            'select Name_of_Attraction, Type, Summary, Duration, Start_Time, Cost from attraction order by Start_Time Desc')
        for attraction in self.cur:
            self.attractions.append(attraction)
        return self.attractions

    def costAsc(self):
        self.attractions = []
        self.cur.execute(
            'select Name_of_Attraction, Type, Summary, Duration, Start_Time, Cost from attraction order by Cost Asc')
        for attraction in self.cur:
            self.attractions.append(attraction)
        return self.attractions

    def costDesc(self):
        self.attractions = []
        self.cur.execute(
            'select Name_of_Attraction, Type, Summary, Duration, Start_Time, Cost from attraction order by Cost Desc')
        for attraction in self.cur:
            self.attractions.append(attraction)
        return self.attractions
