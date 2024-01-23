import pickle
import pandas as pd
import streamlit as st
from pandas import DataFrame


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    dis = similarity[movie_index]
    movielist = sorted(list(enumerate(dis)), reverse=True, key=lambda x: x[1])[1:6]
    for i in movielist:
        st.write(movies.iloc[i[0]].title)
st.title("Movie Recommender System")
movies_list=pickle.load(open('movies_dict.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))
movies=pd.DataFrame(movies_list)
option=st.selectbox('Select the film which you want to watch',movies['title'].values)
if st.button('Recommend'):
    recommend(option)


