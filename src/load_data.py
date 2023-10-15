import os
import sys
import json
import numpy as np
import pandas as pd
from datetime import datetime
from math import sin, cos, sqrt, atan2, radians


def load_data(input_path,na_values):
    '''
    This function is to load data from file source.
    params:
        input_path: this points to the path of input csv file.

    return: DataFrame 
    '''
    df = pd.read_csv(input_path,na_values=na_values,keep_default_na=False)
    return df