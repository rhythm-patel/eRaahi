import mysql.connector

class backend:
    mycursor = ''
    mydb = ''

    def __init__(self):
        self.mydb = mysql.connector.connect(user='newuser', password='password',
                                           host='localhost',
                                           database='final')
        self.mycursor = self.mydb.cursor(buffered=True)

    def getmovies(self, search_text, filter):
        movies = []
        if filter == "Name":
            self.mycursor.execute("select * from Movies where Movie_name LIKE '%"+search_text+"%'")
        elif filter == "Age":
            self.mycursor.execute("select * from Movies where Age LIKE '%"+search_text+"%'")
        else:
            self.mycursor.execute("select * from Movies where Genres LIKE '%"+search_text+"%'")

        myresult = self.mycursor.fetchall()
        for movie in myresult:
            movies.append(movie)
        return movies

    def get_movie_rating(self, movie_id):
        self.mycursor.execute("select * from reviews where Movie_id = "+ movie_id)
        myresult = self.mycursor.fetchall()

        if len(myresult) == 0:
            return {"Rating":0, "of":"0 Users"}

        return {"Rating": sum(row[1] for row in myresult)/len(myresult), "of":str(len(myresult))+" Users"}

    def getHallInfo(self, hall_id):
        self.mycursor.execute("select * from hall where Hall_id = "+ str(hall_id))
        myresult = self.mycursor.fetchall()
        for hall in myresult:
            hall_info = {
                "hall_name": hall[1],
                "total_seats": hall[2],
                "location": hall[3]
            }
            return hall_info

    def getAvailableSeats(self, book_id):
        self.mycursor.execute("select * from seats where Book_id = "+ str(book_id))
        myresult = self.mycursor.fetchall()
        for seats in myresult:
            return seats[1]

    def get_booking_details(self, movie_id):
        available_bookings = []
        self.mycursor.execute("select * from movie_booking where Movie_id = "+ str(movie_id))
        myresult = self.mycursor.fetchall()
        for book_option in myresult:
            book_info = {}
            book_info['book_id'] = book_option[0]
            book_info['cost'] = book_option[4]
            book_info['date'] = book_option[3]
            book_info.update(self.getHallInfo(book_option[2]))

            book_info['available'] = self.getAvailableSeats(book_option[0])
            if book_info['available'] == None or book_info['available'] < 1:
                continue

            available_bookings.append(book_info)
        return available_bookings

    def get_movie_info(self,search_text, filter):
        all_movie_detail = []
        found_movies = self.getmovies(search_text, filter)

        for movie in found_movies:
            movie_info = {}
            movie_info['Name'] = movie[1]
            movie_info['Genre'] = movie[2]
            movie_info['Age'] = movie[3]
            movie_id = str(movie[0])

            movie_info['bookings'] = self.get_booking_details(movie_id)
            movie_info.update(self.get_movie_rating(movie_id))


            all_movie_detail.append(movie_info)
        return all_movie_detail

    def bookTickets(self, book_id_dict, customer_id):

        sql = "INSERT INTO booked (Book_id, customer_id, seats) VALUES (%s, %s, %s)"
        reduceSeats = "UPDATE seats SET available_seats = %s WHERE Book_id = %s"
        to_insert = []
        toReduce = []
        for book_id, seats in book_id_dict.items():
            to_insert.append((book_id, customer_id,seats))
            toReduce.append((self.getAvailableSeats(book_id)-seats,book_id))

        self.mycursor.executemany(sql, to_insert)
        self.mycursor.executemany(reduceSeats, toReduce)
        self.mydb.commit()

    def getMovieFromBook(self, book_id):

        self.mycursor.execute("select Movie_Id from movie_booking where Book_id = "+ str(book_id))
        myresult = self.mycursor.fetchall()
        movieid = myresult[0][0]

        self.mycursor.execute("select Movie_name from Movies where Movie_Id = "+ str(movieid))
        myresult = self.mycursor.fetchall()

        return {movieid: myresult[0][0] }

    def getMovieToreview(self, customer_id):
        customer_id = str(customer_id)
        self.mycursor.execute("select Book_id from booked where customer_id = "+ customer_id)
        myresult = self.mycursor.fetchall()
        movies_booked = {}
        for book_info in myresult:
            movies_booked.update(self.getMovieFromBook(book_info[0]))
        self.mycursor.execute("select Movie_Id from reviews where customer_id = "+ customer_id )
        myresult = self.mycursor.fetchall()

        for movie in myresult:
            if movie[0] in movies_booked.keys():
                del movies_booked[movie[0]]

        return movies_booked

    def updateReview(self, customer_id, ratings):
        sql = "INSERT INTO reviews (Movie_Id, Rating, customer_id) VALUES (%s, %s, %s)"
        to_insert = []

        for movie_id, rating in ratings.items():
            to_insert.append((movie_id,rating,customer_id))

        self.mycursor.executemany(sql, to_insert)
        self.mydb.commit()



    #########################################
    #########################################

    def adminMovies(self, vals, addorupdate):
        try:
            if addorupdate == "Add":
                sql = "INSERT INTO Movies (Movie_name, Genres, Age) VALUES {}".format(tuple(vals))

                self.mycursor.execute(sql)
                self.mydb.commit()

            else:
                sql = "UPDATE Movies SET Movie_name='{}', Genres='{}', Age='{}' WHERE Movie_Id={}".format(vals[1],vals[2],vals[3],vals[0])
                print(sql)
                self.mycursor.execute(sql)
                self.mydb.commit()
        except:
            print("Bhap Bhenchod")

    def adminhall(self, vals, addorupdate):
        try:
            if addorupdate == "Add":
                sql = "INSERT INTO hall (Hall_name, Available_seats, Location) VALUES {}".format(tuple(vals))
                self.mycursor.execute(sql)
                self.mydb.commit()

            else:
                sql = "UPDATE hall SET Hall_name = '{}', Available_seats= '{}', Location='{}' WHERE Hall_id = {}".format(vals[1],vals[2],vals[3],vals[0])
                self.mycursor.execute(sql)
                self.mydb.commit()
        except:
            print("hello")

    def adminbooking(self, vals, addorupdate):
        vals.append(1)
        try:
            if addorupdate == "Add":
                sql = "INSERT INTO booking (Movie_Id, Hall_id, date, Cost, Slots) VALUES {}".format(tuple(vals))
                self.mycursor.execute(sql)
                self.mydb.commit()

            else:
                sql = "UPDATE booking SET Movie_Id = '{}', Hall_id= '{}', date='{}', Cost='{}', Slots='{}'   WHERE Movie_Id = {}".format(vals[1],vals[2],vals[3],vals[4],vals[5],vals[0])
                self.mycursor.execute(sql)
                self.mydb.commit()
        except:
            print("hello")


    def adminseats(self, vals, addorupdate):
        try:
            if addorupdate == "Add":
                sql = "INSERT INTO seats (Book_id, available_seats) VALUES {}".format(tuple(vals))
                self.mycursor.execute(sql)
                self.mydb.commit()

            else:
                sql = "UPDATE seats SET available_seats = '{}' WHERE Book_id = {}".format(vals[1], vals[0])
                self.mycursor.execute(sql)
                self.mydb.commit()
        except:
            print("hello")
