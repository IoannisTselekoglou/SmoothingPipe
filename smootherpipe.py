import numpy as np

class Smootherpipe:
    def __init__(self):
        pass

    #@staticmethod
    def kernel2D(actual_index, array_input, size : int, algo): 

        #middle_point = round.(len(array_input)/2)
        half_kernel = int((size - 1)/2)
        sum_window = 0
        treshhold = np.average(array_input)

        #von -half_kernel bis half_kernel iterieren. Bessere logik
        def average():
            nonlocal sum_window  
            for i in range(-half_kernel, half_kernel + 1):
                index = actual_index + i
                if 0 <= index < len(array_input):
                    sum_window += array_input[index]
                    #else:
                    #    #maybe only usefull when noramlizing Data or kernelsize bigger
                    #    sum_window += treshhold
            return sum_window / size

        #TODo : make this function work
        def gausian():
            nonlocal sum_window  
            sigma = 1
            gaussian_sum = 0 
            index = actual_index + i
            if 0 <= index < len(array_input):
                distance = i
                weight = (1 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(-0.5 * (distance / sigma) ** 2)
                sum_window += array_input[index] * weight
                gaussian_sum += weight
                #distance  = i
                #x_input = array_input[index] 
                #sum_window += x_input * 1/(np.sqrt(2*np.pi))*np.exp((distance**2)/2)
                #gauisan_sum += 1/(np.sqrt(2*np.pi))*np.exp((-x_input**2)/2)
            return sum_window / gaussian_sum

        if algo == "gausian":
            return gauisan()
        if algo == "average":
            return average()

    @staticmethod
    def convolution2D(input_array, kernel_size, algo = "average"):
        result = []    
        for i in range(len(input_array)):
            result.append(Smootherpipe.kernel2D(i, input_array, kernel_size, algo))
        #print(f"LENGTH INPUT ARRAY: {len(input_array)}  LENGTH SMOOTHED ARRAY: {len(result)}")
        return result 

    ##non static way to create function with self
    #def convolution2D(self, input_array, kernel_size):
    #    result = []    
    #    for i in range(len(input_array)):
    #        result.append(self.kernel2D(i, input_array, kernel_size))
    #    #print(f"LENGTH INPUT ARRAY: {len(input_array)}  LENGTH SMOOTHED ARRAY: {len(result)}")
    #    return result 