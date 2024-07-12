import pandas as pd
import numpy as np 
from calculation import Smootherpipe


if __name__ == "__main__":

    smoother = Smootherpipe()

    test = [1,3,4,2,13,4,2,3,4,2,3,4,2,3,4,2,3,4,2,3,4,2,3,4,2,3,4,2,3,4,2,3,4,2,3,4,2,3,4,2,4]

    print(smoother.convolution2D(test, kernel_size=10))
