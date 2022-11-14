### Tarea parte 4 ###
import pandas as pd
import numpy as np
from numpy import mean, sqrt, square, mean
from scipy.fftpack import fft, fftfreq
import seaborn as sns


df = pd.read_csv('file_name.csv')

df.fillna(0, inplace=True)

df.isna().sum()


power = df['Mean_global_active_power'].values 

power = power-mean(power)

fourier = abs(fft(power))

from scipy.fft import fft, fftfreq

# Number of samples in normalized_tone
#N = SAMPLE_RATE * DURATION


xf = fftfreq(len(power), 1 / 1)

import matplotlib.pyplot as plt

plt.plot(fourier)

#plt.plot(xf[722:1400], fourier[722:1400])

plt.plot(xf[0:700], fourier[0:700])

# Craeate a graph for the Time rate#
sns.set()
plt.figure(figsize=(10, 7), dpi=150)
plt.plot(xf[0:700], fourier[0:700], '-ob')
#plt.plot(time, regre, '-g')
plt.title("Fourier transform", fontsize=14, fontweight="bold")
plt.xlabel("Fecuency in Day", fontsize=12, fontweight="bold", labelpad=10)
plt.ylabel("Power", fontsize=12, fontweight="bold", labelpad=10)






