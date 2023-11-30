import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import os

class Recommender():
    def __init__(self):
        self.key_df = pd.read_csv(os.path.join(os.getcwd(), "key_english.csv"))
        self.vectors = pd.read_csv(os.path.join(os.getcwd(), "data.csv"))
        self.similarity = cosine_similarity(self.vectors)
        self.data = pd.read_csv(os.path.join(os.getcwd(), "dataa.csv"))

    def verse_in(self, fullverse):
        temp = fullverse.split()
        if len(temp) == 4:
            book = " ".join(temp[0:2])
            chap = temp[2]
            verse = temp[3]
        else:
            book, chap, verse = temp
        book = "b" + str(self.key_df[self.key_df['n'] == book]["b"].index[0] + 1)
        return " ".join([book, chap, verse])
    
    def verse_out(self, fullverse):
        book, chap, verse = fullverse.split()
        chap = chap.replace("chapter", "")
        verse = verse.replace("verse", "")
        book = book.replace("b", "")
        book = self.key_df.loc[self.key_df['b'] == int(book), 'n'].values[0]
        return book + " " + chap + ":" + verse
    
    def recommend(self, verse):
        verse = self.data[self.data['labels']==self.verse_in(verse)]
        if verse.empty:
            return False
        verse_index = verse.index[0]
        distances = self.similarity[verse_index]
        verse_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:100]
        verse_list = [self.data.iloc[i[0]].labels for i in verse_list]
        verse_list = [self.verse_out(i) for i in verse_list]
        return verse_list