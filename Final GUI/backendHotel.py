import mysql.connector

class backendHotel:
	def __init__(self):
		self.mydb = mysql.connector.connect(host="localhost",user="root",passwd="admin",database = 'finalproject',auth_plugin='mysql_native_password',autocommit=True)
		self.mycursor = self.mydb.cursor(buffered=True)
		self.hotels = []
		self.all_hotel_list=[]
		self.all_reviews=[]
		self.all_rooms=[]
		self.balance=0
		self.getallhotel()
		self.getAllReview()

	def updateroominfo(self,rid,a,b,c,d):
		self.mycursor.execute('update room set capacity = %s where id = %s',(str(a),str(rid)))
		self.mycursor.execute('update room set hotel_id = %s where id = %s',(str(b),str(rid)))
		self.mycursor.execute('update room set cost = %s where id = %s',(str(c),str(rid)))
		self.mycursor.execute('update room set booked = %s where id = %s',(str(d),str(rid)))
		self.mydb.commit()


	def updatelocationinfo(self,lid,name,x,y):
		self.mycursor.execute('update locations set name = %s where id = %s',(str(name),str(lid)))
		self.mycursor.execute('update locations set x = %s where id = %s',(str(x),str(lid)))
		self.mycursor.execute('update locations set y = %s where id = %s',(str(y),str(lid)))
		self.mydb.commit()

	def updatecustomerinfo(self,cid,fname,lname,contact,gender,bal):
		self.mycursor.execute('update customer set firstName = %s where id = %s',(str(fname),str(cid)))
		self.mycursor.execute('update customer set lastName = %s where id = %s',(str(lname),str(cid)))
		self.mycursor.execute('update customer set contact = %s where id = %s',(str(contact),str(cid)))
		self.mycursor.execute('update customer set gender = %s where id = %s',(str(gender),str(cid)))
		self.mycursor.execute('update customer set balance = %s where id = %s',(str(bal),str(cid)))
		self.mydb.commit()		


	def updatehotelinfo(self,hid,name,lid,contact):
		self.mycursor.execute('update hotel set name = %s where id = %s',(str(name),str(hid)))
		self.mycursor.execute('update hotel set loc_id = %s where id = %s',(str(lid),str(hid)))
		self.mycursor.execute('update hotel set contact = %s where id = %s',(str(contact),str(hid)))
		self.mydb.commit()		

	def addintohotel(self,name,lid,contact):
		self.mycursor.execute('INSERT INTO hotel (Name, loc_id, contact) VALUES (%s, %s, %s)',(str(name),str(lid),str(contact)))
		self.mydb.commit()		

	def addintolocation(self,name,x,y):
		self.mycursor.execute('INSERT INTO locations (Name, x, y) VALUES (%s, %s, %s)',(str(name),str(x),str(y)))
		self.mydb.commit()

	def addintocustomer(self,fname,lname,contact,gender,bal):
		self.mycursor.execute('INSERT INTO customer (firstName, lastName, contact, gender, balance) VALUES (%s, %s, %s, %s, %s)',(str(fname),str(lname),str(contact),str(gender),str(bal)))
		self.mydb.commit()

	def addintoroom(self,cap,hid,cost,booked):
		self.mycursor.execute('INSERT INTO room (capacity, hotel_id, cost, booked) VALUES (%s, %s, %s,%s)',(str(cap),str(hid),str(cost),str(booked)))
		self.mydb.commit()

	def getroombounds(self):
		self.mycursor.execute('select min(id) from room')
		for temp in self.mycursor:
			a = temp[0]
		self.mycursor.execute('select max(id) from room')
		for temp in self.mycursor:
			b = temp[0]
		return a,b

	def getinforoom(self,rid):
		self.mycursor.execute('select * from room where id = \'{}\''.format(rid))
		for temp in self.mycursor:
			a = str(temp[1])
			b = str(temp[2])
			c = str(temp[3])
			d = str(temp[4])

		return a,b,c,d

	def getinfocustomer(self,cid):
		self.mycursor.execute('select * from customer where id = \'{}\''.format(cid))
		for temp in self.mycursor:
			a = str(temp[0])
			b = str(temp[1])
			c = str(temp[2])
			d = str(temp[4])
			e = str(temp[5])

		return a,b,c,d,e		


	def getinfolocation(self,lid):
		self.mycursor.execute('select * from locations where id = \'{}\''.format(lid))
		for temp in self.mycursor:
			a = str(temp[0])
			b = str(temp[2])
			c = str(temp[3])

		return a,b,c

	def getinfohotel(self,hid):
		self.mycursor.execute('select * from hotel where id = \'{}\''.format(hid))
		for temp in self.mycursor:
			a = str(temp[0])
			b = str(temp[2])
			c = str(temp[3])

		return a,b,c
	def getlocationbounds(self):
		self.mycursor.execute('select min(id) from locations')
		for temp in self.mycursor:
			a = temp[0]
		self.mycursor.execute('select max(id) from locations')
		for temp in self.mycursor:
			b = temp[0]
		return a,b

	def getcustomerbounds(self):
		self.mycursor.execute('select min(id) from customer')
		for temp in self.mycursor:
			a = temp[0]
		self.mycursor.execute('select max(id) from customer')
		for temp in self.mycursor:
			b = temp[0]
		return a,b

	def gethotelbounds(self):
		self.mycursor.execute('select min(id) from hotel')
		for temp in self.mycursor:
			a = temp[0]
		self.mycursor.execute('select max(id) from hotel')
		for temp in self.mycursor:
			b = temp[0]
		return a,b


	def updateroom(self,rid):
		self.mycursor.execute('update room set booked = 1 where id = \'{}\''.format(str(rid)))
		self.mydb.commit()

	def setBalance(self,bal,uid):
		self.mycursor.execute('update customer set balance = %s where id = %s',(str(bal),str(uid)))
		self.mydb.commit()
		self.balance=bal

	def getBalance(self,uid):
		self.mycursor.execute('select balance from customer where id = \'{}\''.format(uid))
		for temp in self.mycursor:
			self.balance=temp[0]
		return self.balance

	def getrooms(self,hotel_name):
		self.all_rooms=[]
		self.mycursor.execute("select * from room where booked=0")
		for room in self.mycursor:
			temp = [str(room[0]),str(room[1]),str(room[2]),str(room[3]),str(room[4])]
			self.all_rooms.append(temp)
		for room in self.all_rooms:
			self.mycursor.execute('select name from hotel where id = \'{}\''.format(room[2]))
			for temp in self.mycursor:
				room.append(temp[0])
		ans=[]
		for temp in self.all_rooms:
			if temp[5]==hotel_name[7:]:
				ans.append(temp)
		return ans


	def gethotels(self):
		self.mycursor.execute('select name,id from hotel')
		for hotel in self.mycursor:
			self.hotels.append(hotel)
		return self.hotels

	def getAllReview(self):
		self.mycursor.execute('select * from hotel_feedback')
		for review in self.mycursor:
			temp = [str(review[0]),str(review[1]),review[2],str(review[3]),str(review[4])]
			self.all_reviews.append(temp)
		for temp in self.all_reviews:
			self.mycursor.execute('select firstName,lastName from customer where id = \'{}\''.format(temp[3]))
			for a,b in self.mycursor:
				temp.append(a+" "+b)
		for temp in self.all_reviews:
			self.mycursor.execute('select name from hotel where id = \'{}\''.format(temp[4]))
			for a in self.mycursor:
				temp.append(a[0])
			
	def getReview(self,hotel_name):
		ans=[]
		for temp in self.all_reviews:
			if temp[6]==hotel_name[7:]:
				ans.append(temp)
		return ans

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
				# print(avg_price[0])
				if avg_price[0]==None:
					temp.append(str(0))
				else:
					temp.append(str(int(avg_price[0])))

		# adding booked percent
		for temp in self.all_hotel_list:
			self.mycursor.execute('select count(*) from room where booked = True and hotel_id = \'{}\''.format(temp[1]))
			for ans in self.mycursor:
				booked=ans[0]
			self.mycursor.execute('select count(*) from room where hotel_id = \'{}\''.format(temp[1]))
			for ans in self.mycursor:
				if(ans[0]==0):
					temp.append(str(0)+'%')
				else:
					temp.append(str((100*booked/ans[0]))+'%')

		# adding avg rating
		for temp in self.all_hotel_list:
			self.mycursor.execute('select avg(stars) from hotel_feedback where hotel_id = \'{}\''.format(temp[1]))
			for avg_price in self.mycursor:
				if(avg_price[0]==None):
					temp.append(str(0.0))
				else:
					d = str(avg_price[0])
					temp.append(d[:4])

	#filtering on basis of rating
	def gethotelbyrating(self,rating=0):
		ans =[]
		for temp in self.all_hotel_list:
			# print(temp)
			if(float(temp[5])>=rating):
				ans.append(temp)
		return ans

	def gethotelbyprice(self,price=999999):
		ans =[]
		for temp in self.all_hotel_list:
			if(float(temp[3])<=price):
				ans.append(temp)
		return ans
