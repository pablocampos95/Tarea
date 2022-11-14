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
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n


power_moving_average = moving_average(power, 20)

plt.plot(power_moving_average)

def detectar_minimos(df):
    X = df['Mean_global_active_power'].values
    x = moving_average(X, n=20)*-1
    peaks2, _ = find_peaks(x, prominence=0.5)
    
    plt.plot(peaks2, x[peaks2], "ob"); plt.plot(x); plt.legend(['prominence'])
    
    return peaks2 + 20

peaks = detectar_minimos(df)
    
fig = px.line(New_data_frame, x='Dates', y='Mean_global_active_power')
fig.write_html("Minimos.html")




    