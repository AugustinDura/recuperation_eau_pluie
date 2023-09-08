

import pandas as pd
import numpy as np
import datetime 


## Returns k distinct random dates between a start date and an end date
def generate_random_dates(start_date: datetime, end_date: datetime, k: int):
   date_range = (end_date - start_date).days + 1
   random_days = np.random.choice(date_range, size=k, replace=False)
   random_dates = pd.to_datetime(start_date) + pd.to_timedelta(random_days, unit='d')
   return random_dates

## Returns k random floats with given mean and standard deviation
def generate_random_rain(mean_rain:float, sigma_rain:float, k:int):
   random_rain = np.random.normal(mean_rain, sigma_rain, size=k).round(1)
   return random_rain

## Returns a year of daily rainfall
def generate_rainfall(avg_monthly_rainy_days: pd.DataFrame, avg_monthly_rainfall: pd.DataFrame):
   result = pd.DataFrame({"rainfall" : np.zeros(365)}, index=pd.date_range("20230101", periods=365))
   for month in range(len(avg_monthly_rainy_days)):
    #Number of rainy days in month
    avg_days_obs = round(avg_monthly_rainy_days.loc[month])
    avg_days = round(np.random.normal(avg_days_obs, avg_days_obs/4))
    
    #Picking days that are rainy
    start_date = result.loc[result.index.month == month+1].index.min()
    end_date =result.loc[result.index.month == month+1].index.max()
    rainy_days = generate_random_dates(start_date, end_date, avg_days)

    #Actual rainfall
    avg_rain = avg_monthly_rainfall.loc[month]/avg_days
    obs_rain = generate_random_rain(avg_rain, avg_rain/4, avg_days)
    
    #fill in result dataframe
    result.loc[result.index.isin(rainy_days), "rainfall"] = obs_rain
   return result

## Returns minimal reservoir volume
# Pas fini
def min_reservoir_volume(water_input: pd.DataFrame, water_consumption: pd.DataFrame):
   reservoir = pd.DataFrame({"volume" : np.zeros(365)}, index=pd.date_range("20230101", periods=365))
   for i in range(len(reservoir.index)-1):
      reservoir["volume"].iloc[i+1] = min(0,reservoir["volume"].iloc[i] + water_input.iloc[i] - water_consumption.iloc[i])
   result = - reservoir["volume"].min()
   return result