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
    return df


def handle_missing_value(df):
    '''
    This function is to handles missing values in  data.
    '''

    # Convert 'NaN' to np.nan
    df=df.replace('NaN', float(np.nan), regex=True)
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
    handle_missing_value(df)
    drop_columns(df)
    return df


if  __name__ == "__main__":

    # reading configuration from config file.
    with open ("config.json",'r') as file:
        config = json.load(file)
    train = config["train_path"]

    # Reading Train data
    df = load_data(train)

    # Data processing
    df = prepare_data(df)
    print(df[["ID","Weatherconditions",'Time_taken(min)']].head())