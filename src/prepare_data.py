import json
import numpy as np
import pandas as pd
from math import sin, cos, sqrt, atan2, radians
from load_data import load_data
from configuration import *

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


def process_weatherconditions(df):
    '''
    This function is to process Weather conditions column.
    params:
        df : Dataframe to be processed
    return: 
        Processed Dataframe
    '''
    weat_con = list(df['Weatherconditions'])
    weath_con = []
    for i in range(len(weat_con)):
        weath_con.append(weat_con[i].split(" ")[1])
    df['Weatherconditions'] = np.array(weath_con)
    return df


def process_time_taken(df):
    '''
    This function is to process Time Taken column.
    params:
        df : Dataframe to be processed
    return: 
        Processed Dataframe
    '''
    t_t = list(df['Time_taken(min)'])
    t_ti = []
    for i in range(len(t_t)):
        t_ti.append(t_t[i].split(" ")[1])
    df['Time_taken(min)'] = np.array(t_ti)
    return df

def process_timecolumns(df):
    '''
    This function is to process timestamp columns from data for model building.
    params:
        df : Dataframe to be processed
    return: 
        Processed Dataframe
    '''
    df['Time_Orderd']=pd.to_timedelta(df['Time_Orderd'])
    df['Time_Order_picked']=pd.to_timedelta(df['Time_Order_picked'])
    df['Order_prep_time'] = ((df['Time_Order_picked'] - df['Time_Orderd']).dt.total_seconds())/60
    return df


def process_order_preapre_time(df):
    '''
    This function is to extract Order prep time.
    params:
        df : Dataframe to be processed
    return: 
        Processed Dataframe
    '''
    # Dropping Next day dilevery
    # TODO fix for Next day delivery scenario
    index_ord = df[df['Order_prep_time']<=0].index
    df.drop(index_ord,inplace = True)
    return df


def drop_columns(df):
    '''
    This function is to remove unwanted columns from data for model building.
    params:
        df : Dataframe to be processed
    return: 
        Processed Dataframe
    '''
    # Dropping after processing calculate_distance.
    df.drop(['Restaurant_latitude', 'Restaurant_longitude',
        'Delivery_location_latitude', 'Delivery_location_longitude'],axis = 1,inplace = True)
    df.drop(['ID','Delivery_person_ID','Order_Date'],axis = 1, inplace = True)
    df.drop(['Time_Orderd','Time_Order_picked'],axis = 1, inplace = True)
    return df


def type_conversion(df):
    '''
    This function is to convert columns into appropiate datatype.
    params:
        df : Dataframe to be processed
    return: 
        Processed Dataframe
    '''
    df = df.astype(
                    {'Delivery_person_Age': 'int', 
                    'distance': 'float64',
                    'Delivery_person_Ratings':'float64',
                    'Weatherconditions':'object',
                    'Road_traffic_density':'object',
                    'Type_of_order':'object',
                    'Type_of_vehicle':'object',
                    'Festival':'object',
                    'City':'object',
                    'multiple_deliveries':'int',
                    'Time_taken(min)':'int'}
                )
    return df


def handle_missing_value(df):
    '''
    This function is to handles missing values in  data.
    '''
    df.dropna(inplace = True)
    return df


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

    # Processing columns
    process_weatherconditions(df)
    process_time_taken(df)
    process_timecolumns(df)
    process_order_preapre_time(df)
    handle_missing_value(df)
    drop_columns(df)
    type_conversion(df)
    return df
