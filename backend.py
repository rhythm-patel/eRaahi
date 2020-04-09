import mysql.connector

class backend:
	def __init__(self):
		self.mydb = mysql.connector.connect(host="localhost",user="root",passwd="admin",database = 'finalproject',auth_plugin='mysql_native_password')
		self.mycursor = self.mydb.cursor(buffered=True)
		self.hotels = []
		self.all_hotel_list=[]

	def gethotels(self):
		self.mycursor.execute('select name,id from hotel')
		for hotel in self.mycursor:
			self.hotels.append(hotel)
		return self.hotels

	def getallhotel(self):
		self.all_hotel_list=[]
		self.mycursor.execute('select name,loc_id,id from hotel')
		for hotel in self.mycursor:
			temp = [hotel[0],str(hotel[1]),str(hotel[2])]
			self.all_hotel_list.append(temp)

		#adding location name
		for temp in self.all_hotel_list:
			self.mycursor.execute('select name from locations where id = \'{}\''.format(temp[1]))
			temp.pop(1)
			for loc_name in self.mycursor:
				temp.append(loc_name[0])

		# adding avg price
		for temp in self.all_hotel_list:
			self.mycursor.execute('select avg(cost) from room where hotel_id = \'{}\''.format(temp[1]))
			for avg_price in self.mycursor:
				temp.append(str(int(avg_price[0])))

		# adding booked percent
		for temp in self.all_hotel_list:
			self.mycursor.execute('select count(*) from room where booked = True and hotel_id = \'{}\''.format(temp[1]))
			for ans in self.mycursor:
				booked=ans[0]
			self.mycursor.execute('select count(*) from room where hotel_id = \'{}\''.format(temp[1]))
			for ans in self.mycursor:
				 temp.append(str((100*booked/ans[0]))+'%')

		# adding avg rating
		for temp in self.all_hotel_list:
			self.mycursor.execute('select avg(stars) from hotel_feedback where hotel_id = \'{}\''.format(temp[1]))
			for avg_price in self.mycursor:
				d = str(avg_price[0])
				temp.append(d[:4])
			print(temp)

		return self.all_hotel_list
