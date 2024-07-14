import pandas as pd
import numpy as np 
from smootherpipe import Smootherpipe as sp
import matplotlib.pyplot as plt


if __name__ == "__main__":

    x = np.linspace(-10,10,300)
    y_true = np.sin(x)
    noise = 0.9 * np.random.normal(size=len(x))

    #apply noise to data
    y_noise = y_true + noise
    #smooth data using smoothingpipe
    y_smoothed = sp.convolution2D(y_noise, kernel_size=15)
    #y_smoothed = sp.convolution2D(y_noise,kernel_size=5, algo="gaussian" )


    #Plotting 
    plt.figure(figsize=(8, 6))
    plt.scatter(x, y_noise, label='Noisy data', color='blue', marker='o')
    plt.scatter(x, y_smoothed, label='Smoothed data', color='red', marker = 'o')
    plt.title('Sinc Curve with Added Noise')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()
    

