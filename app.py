import pickle
import streamlit as st
import requests

# def fetch_poster(movie_id):
#     url=""
#     data=requests.get(url)
#     data=data.json()
#     poster_path=data['poster_path']
#     full_path=""+poster_path
#     return full_path

def recommend(query):
    query = query.lower()
    matches = movies[movies['tags'].apply(lambda x: query in x.lower())]
    recommended_movies_name = []
    # recommended_movies_poster = []
    for idx in matches.index[:5]:
        movie_id = matches.loc[idx].movie_id
        # recommended_movies_poster.append(fetch_poster(movie_id))
        recommended_movies_name.append(matches.loc[idx].title)
    return recommended_movies_name

st.header("Movies Recommendation System Using Machine Learning")
movies = pickle.load(open('output/movie_list.pkl', 'rb'))
similarity = pickle.load(open('output/similarity.pkl', 'rb'))

query = st.text_input('Type a movie, cast, or director to get recommendations')

if st.button('Show Recommendation'):
    recommended_movies_name = recommend(query)
    if recommended_movies_name:
        col1, col2, col3, col4, col5 = st.columns(5)
        cols = [col1, col2, col3, col4, col5]
        for col, movie in zip(cols, recommended_movies_name):
            with col:
                st.text(movie)
                # st.image(recommended_movies_poster[recommended_movies_name.index(movie)])
    else:
        st.text("No matches found.")
