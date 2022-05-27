import streamlit as st
import pickle
import pandas as pd
import requests
url = "http://127.0.0.1:8000/get-proba/"


st.title("Scoring Credit Dashboard")




st.text("In this project we give details about loan agreements")

nombre = st.text_input("Enter Client ID")
# nombre = st.number_input("Enter Client ID")


if nombre:
    x=requests.get(url+str(nombre))
    st.write('probability to NOT return the loan : ', x.text)
#%%
