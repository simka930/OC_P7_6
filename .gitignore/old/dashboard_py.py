import streamlit as st
import pickle
import pandas as pd
import requests

st.title("Scoring Credit Dashboard")

loaded_model = pickle.load(open("Pickle_RL_Model.pkl", 'rb'))


@st.cache
def load_data():
    data = pd.read_csv("data.csv")
    X = data.drop(["SK_ID_CURR", "TARGET"], axis=1)
    return data, X


data, X = load_data()


def get_prediction(client_id):
    # try:
    #     client_id = int(float(client_id))
    # except ValueError:
    #     st.error("Input Error - Valid number expected")
    #     return ""
    if client_id in data["SK_ID_CURR"].to_list():
        index_client = data[data["SK_ID_CURR"] == client_id].index[0]
        result_ = loaded_model.predict(X.iloc[[index_client]]).item()
        if result_:
            return "loan granted"
        else:
            return "loan rejected"
    else:
        return "This client ID does not exist"


st.text("In this project we give details about loan agreements")

# client_id = st.text_input("Enter Client ID")
nombre = st.number_input("Enter Client ID")
if nombre:
    result = get_prediction(nombre)
    st.write(result)
