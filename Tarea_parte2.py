### Tarea parte 2 ###
import pandas as pd
import numpy as np
from scipy.signal import find_peaks
import matplotlib.pyplot as plt

df = pd.read_csv('file_name.csv')

df.fillna(0, inplace=True)

df.isna().sum()




power = df['Mean_global_active_power'].values

def moving_average(a, n=3) :
    """
Input:
    a: Numpy array
    n: Int

Output:
    ret[n - 1:] / n: Moving average
    
Description:
    This function takes the Mean_global_active_power arrays values and returns the moving average of lenght n
    """
    
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n


power_moving_average = moving_average(power, 20)

plt.plot(power_moving_average)

def detectar_minimos(df):
    
    """
Input:
    df: Pandas file of household power consumption data

Output:
    Data_frame: Pandas file of days and Mean_global_active_power
    
Description:
    This function takes the household_power_consumption pandas file return a pandas file with 
    the whole  mean Global_active_power for each day
    """
    
    X = df['Mean_global_active_power'].values
    x = moving_average(X, n=20)*-1
    peaks2, _ = find_peaks(x, prominence=0.5)
    
    plt.plot(peaks2, x[peaks2], "ob"); plt.plot(x); plt.legend(['prominence'])
    
    return peaks2 + 20

peaks = detectar_minimos(df)




    