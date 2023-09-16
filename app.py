import streamlit as st
import pickle
import pandas as pd
import requests

def recommend(movie):
    movie_index = movies[movies['title']==movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True,key=lambda x: x[1])[1:6]

    recommended_movies=[]
    for i in movies_list:
        movie_id = i[0]
        recommended_movies.append(movies.iloc[i[0]].title)
    
    return recommended_movies


movie_dict = pickle.load(open('pickle_files/movie_dict.pkl','rb'))
movies = pd.DataFrame(movie_dict)

similarity = pickle.load(open('pickle_files/similarity.pkl','rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Choose a movie',
    movies['title'].values)

if st.button('Recommend'):
    names = recommend(selected_movie_name)
    for i in names:
        st.write(i)
    
