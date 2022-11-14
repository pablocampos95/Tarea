##### Load archive #####

import pandas as pd
import numpy as np
from numpy import mean, sqrt, square, nanmean
import plotly.express as px





df = pd.read_csv('household_power_consumption.txt',sep = ';',
                infer_datetime_format=True,
                low_memory=False, na_values=['nan','?'])

### Se leen los archivos ###

#import plotly.express as px

#fig =px.scatter(x=range(10), y=range(10))
#fig.write_html("file.html")

Global_active_power = df['Global_active_power']

def get_days(df):
    
    """
Input:
    df: Pandas file of household power consumption data

Output:
    L: Array with the days non-repeated
    
Description:
    This function takes the date household power consumption and return a list of non-repeated days
    
    """
    
    L = []
    dates = df['Date']
    for elem in dates:
        if elem not in L:
            L.append(elem)
    return L


L = get_days(df)

date = L[0]

def Mean_day(df, date):
    
    """
Input:
    df: Pandas file of household power consumption data
    date: A date 

Output:
    mean(L1[index[0]:index[-1]]): mean Global_active_power in the day date selected
    
Description:
    This function takes the household_power_consumption pandas file and a date and return the mean
    mean Global_active_power in the day date selected
    
    """
    
    L1 = df['Global_active_power']
    L2 = df['Date']
    index = []
    
    for i in range(len(L2)):
        if L2[i] == date:
            index.append(i)
    
    return mean(L1[index[0]:index[-1]])


indices =  Mean_day(df, date)

def get_mean_day(df):
    
    """
Input:
    df: Pandas file of household power consumption data

Output:
    Data_frame: Pandas file of days and Mean_global_active_power
    
Description:
    This function takes the household_power_consumption pandas file return a pandas file with 
    the whole  mean Global_active_power for each day
    """
    
    
    dates = get_days(df)
    means = []
    j = 1
    for date in dates:
        nanmean.append(Mean_day(df, date))
        print(j)
        j = j+1
    
    Data_frame = pd.DataFrame()
    
    Data_frame['Dates'] = dates
    Data_frame['Mean_global_active_power'] = means
    
    return Data_frame

New_data_frame = get_mean_day(df)

New_data_frame.to_csv('file_name.csv')

fig = px.line(New_data_frame, x='Dates', y='Mean_global_active_power')
fig.write_html("Mean_global_active_power.html")








    