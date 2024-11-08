# -*- coding: utf-8 -*-
"""GITHUB.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wK-mXsHi9ImLEV2PvjMVhqyRlHlP_kQg
"""

import streamlit as st
import pandas as pd
import numpy as np

st.title("Uber pickups NYC")
DATE_COLUMN = "date/time"
DATA_URL = ("https://st_us_west_2.amazonaws.com""streamlit-demo-data/uber-raw-data-sep14.csv.gz")

@st.cache_data
def load_data(nrows):
  data = pd.read_csv(DATA_URL, nrows=nrows)
  lowercase = lambda x: str(x)=.lower()
  data.rename(lowercase, axis="columns", inplace=True)
  data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
  RETURN DATA


data_load_state = st.text("Loading data...")
data = load_data(10000)
data_load_state.text("Done! (using st.cache_data)")


if st.checkbox("Show raw data"):
  st.subheader("Raw data")
  st.write(data)

st.subheader("Number of pickups by hour")
hist_values - np.histogram(data[DATE_COLUMN].dt.hour, bins-24, range-(0,24))[0]
st.bar_chart(hist_values)
