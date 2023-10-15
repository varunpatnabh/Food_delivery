import json
import numpy as np
from math import sin, cos, sqrt, atan2, radians
from load_data import load_data


def calculate_distance(df):
    '''
    This function is to calculate the distance between longitude and latitude.
    params:
        df : Dataframe to be processed
    return: 
        Numpy array of caluclated Distance
    '''
    r_lat_long = []
    R = 6373.0
    for i in range(len(df)):
        lat1 = radians(df.iloc[i]['Restaurant_latitude'])
        lon1 = radians(df.iloc[i]['Restaurant_longitude'])
        lat2 = radians(df.iloc[i]['Delivery_location_latitude'])
        lon2 = radians(df.iloc[i]['Delivery_location_longitude'])
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        distance = format(R * c,'.2f')
        r_lat_long.append(distance)
    return np.array(r_lat_long)


def prepare_data(df):
    '''
    This function is to prepare data for model building.
    params:
        df : Dataframe to be processed
    return: 
        Processed Dataframe
    '''
    # Inserting Distance calculated at columns 3.
    df.insert(3, 'distance',calculate_distance(df))

    # Dropping auxillary columns
    df.drop(['Restaurant_latitude', 'Restaurant_longitude',
        'Delivery_location_latitude', 'Delivery_location_longitude'],axis = 1,inplace = True)
    return df


def handle_missing_value(df):
    '''
    This function is to handles missing values in  data.
    '''
    #TODO


if  __name__ == "__main__":

    # reading configuration from config file.
    with open ("config.json",'r') as file:
        config = json.load(file)
    train = config["train_path"]

    # Reading Train data
    df = load_data(train)
    print(df.head())

    # Data processing
    df = prepare_data(df)
    print(df.head())