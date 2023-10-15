# from lightgbm import LGBMRegressor
from catboost import CatBoostRegressor
from xgboost import XGBRegressor, XGBRFRegressor

model_list = [("XgBoost ", XGBRegressor()),
              ("CatBoost", CatBoostRegressor(verbose=False)),
            #   ("LGBM ",LGBMRegressor(verbose=-1))
              ]