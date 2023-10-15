import json
from load_data import load_data


def prepare_data(df,):
    '''
    This function is to prepare data for model building.
    '''

    



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