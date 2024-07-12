import numpy as np
class Smootherpipe:
    def __init__(self):
        pass

    def kernel2D(self, actual_index, array_input, size : int): 

        #middle_point = round.(len(array_input)/2)
        half_kernel = int((size - 1)/2)
        sum_window = 0
        treshhold = np.average(array_input)

        #von -half_kernel bis half_kernel iterieren. Bessere logik
        for i in range(-half_kernel, half_kernel + 1):
            index = actual_index + i
            if 0 <= index < len(array_input):
                sum_window += array_input[index]
            #else:
            #    #maybe only usefull when noramlizing Data or kernelsize bigger
            #    sum_window += treshhold

        #devide by size of kernel not array
        return sum_window / size

    def convolution2D(self, input_array, kernel_size):
        result = []    
        for i in range(len(input_array)):
            result.append(self.kernel2D(i, input_array, kernel_size))
        #print(f"LENGTH INPUT ARRAY: {len(input_array)}  LENGTH SMOOTHED ARRAY: {len(result)}")
        return result 

    
