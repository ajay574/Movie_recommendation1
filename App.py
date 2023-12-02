import streamlit as st
import pickle
import pandas as pd
import requests
st.title("Movie Recommender System")
def Fetch_poster(Movie_id):
    url = "https://api.themoviedb.org/3/movie/"+str(Movie_id)+"?api_key=3b8ab95a5f4639996272e3cc1c16db72&language=en-US"
    print(url)
    data=requests.get(url)
    data=data.json()
    Poster_path=data["poster_path"]
    Poster="https://image.tmdb.org/t/p/original/"+Poster_path
    print(Poster)
    return Poster


def recommend(Movie):
      movie_index=movie[movie["title"]==Movie].index[0]
      distance=similar[movie_index]
      movie_list=sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:5]
      Recommend_list=[]
      Recommend_poster=[]
      for i in movie_list:
         movie_id=movie.iloc[i[0]].movie_id
         Recommend_poster.append(Fetch_poster(movie_id))
         Recommend_list.append(movie.iloc[i[0]].title)
      return Recommend_list,Recommend_poster

similar=pickle.load(open("similarty.pkl","rb"))
movie_details=pickle.load(open("Movies_dict.pkl","rb"))
print(movie_details)
movie=pd.DataFrame(movie_details)
Movie_selected=st.selectbox("What Are  you looking For Today ",movie["title"].values)
if st.button('Recommend'):
    Recommendation_name,Recommendation_Poster=recommend(Movie_selected)
    col1,col2,col3,col4=st.columns(4)
    with col1:
        st.text(Recommendation_name[0])
        st.image(Recommendation_Poster[0])
    with col2:
        st.text(Recommendation_name[1])
        st.image(Recommendation_Poster[1])
    with col3:
        st.text(Recommendation_name[2])
        st.image(Recommendation_Poster[2])
    with col4:
        st.text(Recommendation_name[3])
        st.image(Recommendation_Poster[3])





