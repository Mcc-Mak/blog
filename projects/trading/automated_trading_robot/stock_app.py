"""Launcher for the Streamlit stock price prediction app."""

import os
import time

# path to the streamlit app script
path = os.getcwd() + "/stock_price_prediction.py"

# --- install required packages ---
os.system(r"pip install streamlit")
os.system(r"pip install pandas")
os.system(r"pip install yfinance")
os.system(r"pip install pytreands")
os.system(r"pip install numpy")
os.system(r"pip install yahoo-fin")
os.system(r"pip install ssl")
os.system(r"pip install beautifulsoup4")
os.system(r"pip install typing")
os.system(r"pip install requests")
os.system(r"pip install quandl")
os.system(r"pip install regex")

# --- run the streamlit app ---
try:
    os.system(r'streamlit run "{}"'.format(path))
except:
    print("Failed to launch.")

# --- keep the launcher alive while the app runs ---
while True:
    print("Running....")
    time.sleep(5)