import os
import pickle

def convert_float(df):
  df['distance'] = df['distance'].astype('float')
  df['Time_taken(min)'] = df['Time_taken(min)'].astype('float')
  return df


def process_road_trafic_density(df):
  road_trafic_density_dict = {
                        'Low ': 1,
                        'Medium ': 2, 
                        'High ': 3,
                        'Jam ': 4,
                        }
  df['Road_traffic_density'] = df['Road_traffic_density'].apply(lambda x: road_trafic_density_dict[x])
  return road_trafic_density_dict


def process_festival(df):
  festival_dict = {
              'No ': 0,
              'Yes ': 1
              }
  df['Festival'] = df['Festival'].apply(lambda x: festival_dict[x])
  return festival_dict


def process_city(df):
  city_dict = {'Semi-Urban ': 1,
          'Urban ':2,
          'Metropolitian ': 3 }
  df['City'] = df['City'].apply(lambda x: city_dict[x])
  return city_dict


def process_weather_conditions(df,target_column):
  weather_conditions_dict = df.groupby(['Weatherconditions'])[target_column].mean().to_dict()
  df['Weatherconditions'] = df['Weatherconditions'].apply(lambda x: weather_conditions_dict[x])
  return weather_conditions_dict


def process_type_of_order(df,target_column):
  type_of_order_dict = df.groupby(['Type_of_order'])[target_column].mean().to_dict()
  df['Type_of_order'] = df['Type_of_order'].apply(lambda x: type_of_order_dict[x])
  return type_of_order_dict


def process_type_of_vehicle(df,target_column):
  type_of_vehicle_dict = df.groupby(['Type_of_vehicle'])[target_column].mean().to_dict()
  weather_conditions_dict = df['Type_of_vehicle'] = df['Type_of_vehicle'].apply(lambda x: type_of_vehicle_dict[x])
  return type_of_vehicle_dict

def convert_ordinal(df):
  road_trafic_density_dict = process_road_trafic_density(df)
  festival_dict = process_festival(df)
  city_dict = process_city(df)

  # creating combined dictionary
  ordinal_dict= {"road_trafic_density_dict" : road_trafic_density_dict,
                 "festival_dict" : festival_dict,
                 "city_dict" : city_dict
                 }
  return ordinal_dict

def convert_nominal_columns(df,target_column):
  weather_conditions_dict = process_weather_conditions(df,target_column)
  type_of_order_dict = process_type_of_order(df,target_column)
  type_of_vehicle_dict = process_type_of_vehicle(df,target_column)

  # creating combined dictionary
  nominal_dict = {"weather_conditions_dict" : weather_conditions_dict,
                 "type_of_order_dict" : type_of_order_dict,
                 "type_of_vehicle_dict" : type_of_vehicle_dict
                 }
  return nominal_dict


def convert_categorical_columns(df,target_column,model_path):
  ordinal_dict = convert_ordinal(df)
  nominal_dict = convert_nominal_columns(df,target_column)

  # combining and saving dict as joblib
  encoded_dict = {"ordinal_dict": ordinal_dict,
                  "nominal_dict" : nominal_dict     
                  }
  with open(os.path.join(model_path, "encoded.pickle"), 'wb') as handle:
        pickle.dump(encoded_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)


