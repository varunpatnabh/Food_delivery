import os
import sys
import json
import numpy as np
import pandas as pd
from datetime import datetime
from math import sin, cos, sqrt, atan2, radians


def load_data(input_path):
    '''
    This function is to load data from file source.
    params:
        input_path: this points to the path of input csv file.

    return: DataFrame 
    '''
    df = pd.read_csv(input_path)
    return df

if  __name__ == "__main__":

    # reading configuration from config file.
    with open ("config.json",'r') as file:
        config = json.load(file)
    train = config["train_path"]
    test = config["test_path"]

    # Reading Train data
    df = load_data(train)
    print(df.head())

    # Reading Test data
    df = load_data(test)
    print(df.head())