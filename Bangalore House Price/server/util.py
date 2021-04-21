import pickle
import json
import numpy as np

import warnings
warnings.filterwarnings('ignore')

__locations=None
__model=None
__data_columns=None

def get_estimated_price(location,sqft,bhk,bath):
    try:
        loc_index=__data_columns.index(location.lower())
    except:
        loc_index=-1
    x=np.zeros(len(__data_columns))
    x[0]=sqft
    x[1]=bath
    x[2]=bhk
    if loc_index>=0:
        x[loc_index]=1

    return round(__model.predict([x])[0],2)


def get_location_names():
    return __locations

def load_saved_artifacts():
    print("Loading saved artifacts...start")
    global __locations
    global __data_columns

    with open("./artifacts/columns.json","r") as f:
        __data_columns=json.load(f)['data_columns']
        __locations=__data_columns[3:]

    global __model
    with open("./artifacts/banglore_home_prices_model.pickle", "rb") as f:
        __model=pickle.load(f)
    print("Loading saved artifacts...done")

def get_data_columns():
    return __data_columns

load_saved_artifacts()