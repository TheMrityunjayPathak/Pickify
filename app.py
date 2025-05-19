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