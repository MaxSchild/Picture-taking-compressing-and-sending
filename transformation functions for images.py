# transformation functions for images

import math
import cmath

def DFT(data, width, height):
    #creating an Array which will later contain the fourier-coefficients
    coefficientsArray = []
    #giving the right structure to the array
    for i in range(0, height):
        coefficientsArray.append([])
    
    #creating an array of fourier-coefficients
    for y in range(0, height):
        for x in range(0, width):
            # creating a single fourier-coefficient
            coefficient = 0
            for i in range(0, height):
                for j in range(0, width):
                    #value shows the intensity, e.g. of a colour of a pixel
                    value = data[i][j]
                    #formula may be wrong
                    coefficient += value * math.e ** ((-1) * cmath.sqrt(-1) * 2 * math.pi * (i * y + j * x)/ (height * width))
            #appending the coefficient to the coefficientArray
            coefficientsArray[y].append(coefficient)
    return coefficientsArray


#main programm

#creating some data
data = []
width = 8
height = 8

#creating a data-array
for i in range(0, height):
    data.append([])

#filling the data-array with values
for i in range(0, height):
    for j in range(0, width):
        data[i].append(i * 8 + j + 1)
print(data)

print(DFT(data, width, height))
        
















    
