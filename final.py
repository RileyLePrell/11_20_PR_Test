import streamlit as st
import random
import altair as alt
import numpy as np
import pandas as pd

df = pd.read_csv('developments.csv', encoding='latin1')

print(df) 

st.write(df)