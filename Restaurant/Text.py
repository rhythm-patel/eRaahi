from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from nltk.tokenize import WordPunctTokenizer
import string
import re
import pandas as pd
import numpy as np


class Test:

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

    def Process(self, text):
        df = pd.read_csv("DelhiRestaurants.csv")
        df['Reviews'] = self.clean_text(df['Reviews'])
        user_df = df[['User Id', 'Reviews']]
        venue_df = df[['Venue Id', 'Reviews']]
        user_df = user_df.groupby('User Id').agg({'Reviews': ' '.join})
        venue_df = venue_df.groupby('Venue Id').agg({'Reviews': ' '.join})
        print("1")
        userid_vectorizer = TfidfVectorizer(tokenizer=WordPunctTokenizer().tokenize, max_features=1000)
        userid_vectors = userid_vectorizer.fit_transform(user_df['Reviews'])

        venue_vectorizer = TfidfVectorizer(tokenizer=WordPunctTokenizer().tokenize, max_features=1000)
        venue_vectors = venue_vectorizer.fit_transform(venue_df['Reviews'])

        P = pd.DataFrame(userid_vectors.toarray(), index=user_df.index, columns=userid_vectorizer.get_feature_names())
        Q = pd.DataFrame(venue_vectors.toarray(), index=venue_df.index, columns=venue_vectorizer.get_feature_names())
        print("2")
        userid_rating_matrix = pd.pivot_table(df, values='Likes', index=['User Id'], columns=['Venue Id'])
        # P, Q = self.matrix_factorization(userid_rating_matrix, P, Q, steps=100, gamma=0.001, lamda=0.02)

        P = pd.read_csv("P.csv")
        Q = pd.read_csv("Q.csv")
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
        print("3")
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

        print("\n".join([str1, str2, str3]))


text = "Amazing Pizza"
t = Test()
t.Process(text)