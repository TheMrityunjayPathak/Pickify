# Importing Libraries
import os
import sys
import time
import gdown
import pickle
import requests
import pandas as pd
import streamlit as st

# Adding utils directory to PYTHONPATH
sys.path.append(os.path.abspath("../utils"))

# Page Configuration
from utils.file_locator import get_path
st.set_page_config(page_title='Pickify', page_icon=get_path('images', 'logo.png'), layout='wide')

# List of Movies
movies = pd.read_csv(get_path('clean_data','cleaned_data.csv'))
movies_list = movies['title'].values

# Downloading similarity matrix from Google Drive
file_id = '1Zo0ayKcdOxyqNmUjU2niKAVbWl5S3Sol'
output = 'similarity.pkl'
url = f'https://drive.google.com/uc?id={file_id}'

if not os.path.exists(output):
    gdown.download(url, output, quiet=False)

# Loading similarity matrix
with open(output, 'rb') as f:
    similarity = pickle.load(f)

# Navbar Section
st.markdown("""
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Special+Gothic+Expanded+One&display=swap" rel="stylesheet">
            
    <style>
        .navbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            color: white;
            font-family: "Special Gothic Expanded One", sans-serif;
        }
            
        .navbar .logo {
            font-size: 28px;
            font-weight: bold;
            color: #FD3A84;
            letter-spacing: 0.8px
        }
            
        .navbar .nav-right button {
            background-color: #020200;
            padding: 5px 15px;
            color: white;
            cursor: pointer;
            font-size: 15px;
            margin: 4px;
            border: 2px solid rgba(190, 190, 190);
            border-radius: 100px;
        }
            
        .navbar .nav-right .login {
            background-color: #FD3A84;
            padding: 5px 15px;
            color: white;
            cursor: pointer;
            font-size: 15px;
            margin: 4px;
            border: 2px solid #FD3A84;
            border-radius: 100px;
        }
    </style>

    <div class="navbar">
        <div class="logo">Pickify</div>
        <div class="nav-right">
            <form action="#">
                <button>Sign up</button>
                <button class='login'>Login</button>
            </form>
        </div>
    </div>
""", unsafe_allow_html=True)

# Adding banner for visual enhancement
st.image(get_path('images','banner.png'), use_container_width=True)

# Function to fetch movie posters
def fetch_poster(movie_id):
    api_key = st.secrets["tmdb"]["api_key"]
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}'
    response = requests.get(url)
    data = response.json()
    poster_path = data['poster_path']
    full_img_path = f"https://image.tmdb.org/t/p/w500{poster_path}"
    return full_img_path

# Function to get top 5 movie recommendations
def recommend(movie_name):
    movie_idx = movies[movies['title'] == movie_name].index[0]
    movie_similarity = similarity[movie_idx]
    similar_movies = sorted(list(enumerate(movie_similarity)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    movies_posters = []
    for i in similar_movies:
        recommended_movies.append(movies.iloc[i[0]]['title'])
        movies_posters.append(fetch_poster(movies.iloc[i[0]]['movie_id']))
    return recommended_movies, movies_posters

# Displaying recommended movies with posters
with st.expander(label="Watched a great movie, we've got similar picks!", expanded=True, icon=":material/movie:"):
    selected_movie = st.selectbox(label="Watched a great movie? We've got similar picks!", options=movies_list, label_visibility='collapsed')
    if st.button(label='Recommend', icon=":material/thumb_up:", type='primary'):

        progress_text = "Recommending movies, Please wait..."
        my_bar = st.progress(0, text=progress_text)
        for percent_complete in range(101):
            time.sleep(0.02)
            my_bar.progress(percent_complete, text=progress_text)
        time.sleep(0.5)
        my_bar.empty()

        names, posters = recommend(selected_movie)
        col1, col2, col3, col4, col5 = st.columns(5, border=True, vertical_alignment='center')
        with col1:
            st.image(posters[0],use_container_width=True)
            st.caption(names[0])
        with col2:
            st.image(posters[1],use_container_width=True)
            st.caption(names[1])
        with col3:
            st.image(posters[2],use_container_width=True)
            st.caption(names[2])
        with col4:
            st.image(posters[3],use_container_width=True)
            st.caption(names[3])
        with col5:
            st.image(posters[4],use_container_width=True)
            st.caption(names[4])

# Footer Section
st.divider()
st.markdown("<p style='text-align:center;'>Made with ❤️ using Streamlit</p>", unsafe_allow_html=True)