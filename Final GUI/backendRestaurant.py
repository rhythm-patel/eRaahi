from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QTextEdit, QPushButton, QPlainTextEdit
import sys
import pandas as pd
import numpy as np
import mysql.connector

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from nltk.tokenize import WordPunctTokenizer
import string
import re

class PUM(QDialog):
    def __init__(self, message):
        super(PUM, self).__init__()
        uic.loadUi("ErrorBoxRest.ui", self)
        self.show()
        self.error = self.findChild(QPlainTextEdit, "errorBox")
        error.insertPlainText(message);



class backendRestaurant:
    def __init__(self):
        self.cnx = mysql.connector.connect(user='root', password='40@Vaibhav',host='127.0.0.1', database='dbms')
        # self.cnx = mysql.connector.connect(host="localhost",user="root",passwd="admin",database = 'finalproject',auth_plugin='mysql_native_password',autocommit=True)
        # self.cnx = mysql.connector.connect(user='rhythm', password='password',
        #                                    host='127.0.0.1',
        #                                    database='proj')
        self.cur = self.cnx.cursor(buffered=True)
        self.getRestaurant()


    def getIDs(self, id):
    	self.cur.execute('select Venue_Id from Venues')
    	for ids in self.cur:
            if(int(id) == ids[0]):
                return True
    	return False


    def updateRestaurants(self,Venue,Venue_lat,Venue_long,Category,Venue_Id,Likes, Cost, Neighbourhood):
        if(len(Venue) is not 0):

            self.cur.execute('update Venues set Venue = %s where Venue_Id = %s',(str(Venue),str(Venue_Id)))

        if(len(Venue_lat) is not 0):
            self.cur.execute('update Venues set Venue_Latitude = %s where Venue_Id = %s',(str(Venue_lat),str(Venue_Id)))

        if(len(Venue_long) is not 0):
            self.cur.execute('update Venues set Venue_Longitude = %s where Venue_Id = %s',(str(Venue_long),str(Venue_Id)))

        if(len(Category) is not 0):
            self.cur.execute('update Venues set Venue_Category = %s where Venue_Id = %s',(str(Category),str(Venue_Id)))

        if(len(Likes) is not 0):
            self.cur.execute('update Venues set Likes = %s where Venue_Id = %s',(str(Likes),str(Venue_Id)))
            self.cur.execute('update Review set Likes = %s where Venue_Id = %s',(str(Likes),str(Venue_Id)))

        if(len(Cost) is not 0):
            self.cur.execute('update Venues set Likes = %s where Venue_Id = %s',(str(Cost),str(Venue_Id)))

        if(len(Neighbourhood) is not 0):
            self.cur.execute('update Venues set Neighbourhood = %s where Venue_Id = %s',(str(Neighbourhood),str(Venue_Id)))


        self.cnx.commit()

    def addRestaurants(self,Venue,Venue_lat,Venue_long,Category,Venue_Id,Likes, Cost, Neighbourhood):
        self.cur.execute('INSERT INTO Venues (Venue, Venue_Latitude, Venue_Longitude, Venue_Category, Venue_Id, Likes, Cost, Neighbourhood) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',(str(Venue),str(Venue_lat),str(Venue_long),str(Category),str(Venue_Id),str(Likes),str(Cost), str(Neighbourhood)))
        self.cnx.commit()

    def getRestaurant(self):
        self.Rest = []
        self.cur.execute('select Venue, Venue_Category, Cost, Likes from Venues')
        for rest in self.cur:
            self.Rest.append(rest)
        return self.Rest

    def likeDescRest(self):
        self.Rest = []
        self.cur.execute('select Venue, Venue_Category, Cost, Likes from Venues order by Likes Desc')
        for rest in self.cur:
            self.Rest.append(rest)
        return self.Rest

    def costAscRest(self):
        self.Rest = []
        self.cur.execute(
            'select Venue, Venue_Category, Cost, Likes from Venues order by Cost')
        for rest in self.cur:
            self.Rest.append(rest)
        return self.Rest

    def costDescRest(self):
        self.Rest = []
        self.cur.execute(
            'select  Venue, Venue_Category, Cost, Likes from Venues order by Cost Desc')
        for rest in self.cur:
            self.Rest.append(rest)
        return self.Rest


class RSS(QDialog):

    # Text Cleaning
    def clean_text(self, reviews):
        res = []
        for text in reviews:
            text = text.translate(string.punctuation)

            ## Convert words to lower case and split them
            text = text.lower().split()

            ## Remove stop words
            stops = set(stopwords.words("english"))
            text = [w for w in text if not w in stops and len(w) >= 3]

            text = " ".join(text)

            # Clean the text
            text = re.sub(r"[^A-Za-z0-9^,!.\/'+-=]", " ", text)
            text = re.sub(r"what's", "what is ", text)
            text = re.sub(r"\'s", " ", text)
            text = re.sub(r"\'ve", " have ", text)
            text = re.sub(r"n't", " not ", text)
            text = re.sub(r"i'm", "i am ", text)
            text = re.sub(r"\'re", " are ", text)
            text = re.sub(r"\'d", " would ", text)
            text = re.sub(r"\'ll", " will ", text)
            text = re.sub(r",", " ", text)
            text = re.sub(r"\.", " ", text)
            text = re.sub(r"!", " ! ", text)
            text = re.sub(r"\/", " ", text)
            text = re.sub(r"\^", " ^ ", text)
            text = re.sub(r"\+", " + ", text)
            text = re.sub(r"\-", " - ", text)
            text = re.sub(r"\=", " = ", text)
            text = re.sub(r"'", " ", text)
            text = re.sub(r"(\d+)(k)", r"\g<1>000", text)
            text = re.sub(r":", " : ", text)
            text = re.sub(r" e g ", " eg ", text)
            text = re.sub(r" b g ", " bg ", text)
            text = re.sub(r" u s ", " american ", text)
            text = re.sub(r"\0s", "0", text)
            text = re.sub(r" 9 11 ", "911", text)
            text = re.sub(r"e - mail", "email", text)
            text = re.sub(r"j k", "jk", text)
            text = re.sub(r"\s{2,}", " ", text)
            res.append(text)
        return res

    def Process(self, text):

        df = pd.read_csv("TEMP/DelhiRestaurants.csv")
        df['Reviews'] = self.clean_text(df['Reviews'])
        user_df = df[['User Id', 'Reviews']]
        venue_df = df[['Venue Id', 'Reviews']]
        user_df = user_df.groupby('User Id').agg({'Reviews': ' '.join})
        venue_df = venue_df.groupby('Venue Id').agg({'Reviews': ' '.join})

        userid_vectorizer = TfidfVectorizer(tokenizer=WordPunctTokenizer().tokenize, max_features=1000)
        userid_vectors = userid_vectorizer.fit_transform(user_df['Reviews'])

        venue_vectorizer = TfidfVectorizer(tokenizer=WordPunctTokenizer().tokenize, max_features=1000)
        venue_vectors = venue_vectorizer.fit_transform(venue_df['Reviews'])

        P = pd.DataFrame(userid_vectors.toarray(), index=user_df.index, columns=userid_vectorizer.get_feature_names())
        Q = pd.DataFrame(venue_vectors.toarray(), index=venue_df.index, columns=venue_vectorizer.get_feature_names())

        # userid_rating_matrix = pd.pivot_table(df, values='Likes', index=['User Id'], columns=['Venue Id'])
        # P, Q = self.matrix_factorization(userid_rating_matrix, P, Q, steps=100, gamma=0.001,lamda=0.02)

        P = pd.read_csv("TEMP/P.csv")
        Q = pd.read_csv("TEMP/Q.csv")
        Q = Q.rename(Q.iloc[:, 0])
        Q = Q.iloc[:, 1:]

        words = text
        test_df = pd.DataFrame([words], columns=['Review'])
        test_df['Review'] = self.clean_text(test_df['Review'])
        test_vectors = userid_vectorizer.transform(test_df['Review'])
        test_v_df = pd.DataFrame(test_vectors.toarray(), index=test_df.index,
                                 columns=userid_vectorizer.get_feature_names())

        predictItemRating = pd.DataFrame(np.dot(test_v_df.loc[0], Q.T), index=Q.index, columns=['Likes'])
        topRecommendations = pd.DataFrame.sort_values(predictItemRating, ['Likes'], ascending=[0])[:3]
        final_df = []
        final_df = pd.DataFrame(columns=['Neighbourhood', 'Neighbourhood Latitude', 'Neighbourhood Longitude',
                                         'Venue', 'Venue Latitude', 'Venue Longitude', 'Venue Category',
                                         'Venue Id', 'Reviews', 'User Id', 'Likes'])
        for i in topRecommendations.index.values:
            temp = df.loc[df['Venue Id'] == i]
            #     final_df.loc[len(final_df)] = temp
            final_df = final_df.append(temp)

        str1 = final_df.iloc[0][3] + " : " + final_df.iloc[0][0]
        str2 = final_df.iloc[1][3] + " : " + final_df.iloc[1][0]
        str3 = final_df.iloc[2][3] + " : " + final_df.iloc[2][0]

        return("\n".join([str1, str2, str3]))


    def __init__(self):
            super(RSS, self).__init__()
            uic.loadUi("RRS.ui", self)
            self.show()
            self.hello = self.findChild(QTextEdit, "Hello")
            self.hello.setReadOnly(True)
            self.inptag = self.findChild(QPlainTextEdit, "Req")
            self.rectag = self.findChild(QPlainTextEdit, "Rec")
            self.inp = self.findChild(QPlainTextEdit, "Inp")
            self.ans = self.findChild(QPlainTextEdit, "Ans")
            self.ans.setReadOnly(True)
            self.inptag.setReadOnly(True)
            self.rectag.setReadOnly(True)
            self.submit = self.findChild(QPushButton, "Submit")
            self.submit.clicked.connect(self.click)

    def click(self):
        text = self.inp.toPlainText()
        if (text == ""):
            return True
        self.ans.setPlainText("")
        self.ans.insertPlainText(self.Process(text))

    def matrix_factorization(self, R, P, Q, steps=100, gamma=0.001, lamda=0.02):
        for step in range(steps):
            for i in R.index:
                for j in R.columns:
                    if R.loc[i, j] > 0:
                        eij = R.loc[i, j] - np.dot(P.loc[i], Q.loc[j])
                        P.loc[i] = P.loc[i] + gamma * (eij * Q.loc[j] - lamda * P.loc[i])
                        Q.loc[j] = Q.loc[j] + gamma * (eij * P.loc[i] - lamda * Q.loc[j])
            e = 0
            for i in R.index:
                for j in R.columns:
                    if R.loc[i, j] > 0:
                        e = e + pow(R.loc[i, j] - np.dot(P.loc[i], Q.loc[j]), 2) + lamda * (
                                pow(np.linalg.norm(P.loc[i]), 2) + pow(np.linalg.norm(Q.loc[j]), 2))
            if e < 0.001:
                break

        return P, Q
