train_path =  "data/train.csv"

test_path = "data/test.csv"

model_path = "models/encoded.pickle"

target_column = "Time_taken(min)"

na_values =    [
                    "", 
                    "NaN ", 
                    "#N/A", 
                    "#N/A N/A", 
                    "#NA", 
                    "-1.#IND", 
                    "-1.#QNAN", 
                    "-NaN", 
                    "-nan", 
                    "1.#IND", 
                    "1.#QNAN", 
                    "<NA>", 
                    "N/A", 
                    "NA", 
                    "NULL", 
                    "NaN", 
                    "n/a", 
                    "nan", 
                    "null"
                ]