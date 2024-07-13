import pandas as pd
import numpy as np 
from calculation import Smootherpipe as sp


if __name__ == "__main__":


    test = [1,3,4,2,13,4,2,3,4,2,3,4,2,3,4,2,3,4,2,3,4,2,3,4,2,3,4,2,3,4,2,3,4,2,3,4,2,3,4,2,4]

    #smoother = ca()
    #print(smoother.convolution2D(test, kernel_size=10))

    print(sp.convolution2D(test,kernel_size=10))
