import json
from load_data import *
from prepare_data import *
from preprocessing import *


if  __name__ == "__main__":

    # reading configuration from config file.
    with open ("config.json",'r') as file:
        config = json.load(file)
    train = config["train_path"]
    na_values = config["na_values"]
    model_path = config["model_path"]
    target_column = config["target_column"]

    # Reading Train data
    df = load_data(train,na_values)

    # Data processing
    df = prepare_data(df)
    convert_float(df)
    convert_categorical_columns(df,target_column,model_path)

