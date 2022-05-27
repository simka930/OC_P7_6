from fastapi import FastAPI, Path
import pickle
import pandas as pd
from typing import Optional
from functionsp7 import*
from functions_API import*

app = FastAPI()

loaded_model = pickle.load(open("Pickle_RL_Model.pkl", 'rb'))
data_train = pd.read_csv("data_train_preprocessed.csv")
data_test = pd.read_csv("data_test_preprocessed.csv") #data train WITHOUT TARGET that has been saved in the following file
target = pd.read_csv("column_target")
feature_importance = pd.read_csv("global_feature_importance_sorted.csv")




@app.get("/get-proba/{client_id}")
def get_proba_explaination_api(client_id: int = Path(None, description="Expecting client ID")):
    return get_prediction_and_explaination(data_test, client_id, loaded_model)

@app.get("/get-global-feat-imp")
def get_global_feat_imp:
    return feature_importance


#%%
