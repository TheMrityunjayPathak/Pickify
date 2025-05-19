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