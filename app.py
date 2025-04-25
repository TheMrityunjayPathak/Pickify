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