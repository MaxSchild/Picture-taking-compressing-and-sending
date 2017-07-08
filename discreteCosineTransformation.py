#discrete cosine transformation

import math
import cmath

def DCT(data, width, height):
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
                    #formula may be wrong, maybe change x and y in formula?
                    addend = value * math.cos(math.pi * (2 * i) * y /(2 * height)) * math.cos(math.pi * (2 * j) * x /(2 * width))
                    coefficient += addend
            #appending the coefficient to the coefficientArray and making the final multiplication
            cy = 1
            cx = 1
            if y == 0:
                cy = 1 / (math.sqrt(2))
            if x == 0:
                cx = 1 / (math.sqrt(2))
            coefficient = cy * cx * math.sqrt(4/(height + width))
            coefficientsArray[y].append(coefficient)
    return coefficientsArray


def iDCT(coefficientsArray, width, height):
    #creating an Array which will store the values of the pixels 
    data = []
    #giving the right structure to the array

    for i in range(0, height):
        data.append([])

    #creating an array of colour-values
    for y in range(0, height):
        for x in range(0, width):
            #creating a single value
            value = 0
            for i in range(0, height):
                for j in range(0, width):
                    #check what cx and cy have to be
                    cy = 1
                    cx = 1
                    if y == 0:
                        cy = 1 / (math.sqrt(2))
                    if x == 0:
                        cx = 1 / (math.sqrt(2))
                    #not sure at all about the calculating
                    coefficient = coefficientsArray[i][j]
                    addend = cx * cy * coefficient * math.cos(math.pi * (2 * y + 1) * i /(2 * height)) + math.cos(math.pi * (2 * x + 1) * j /(2 * width))
                    value += addend
            value = value * math.sqrt(4/(height * width)) #not sure if I have to do this
            #appending the value to the data-array
            data[y].append(value)
    return data


#main program
data = []
height = 8
width = 8

for i in range(0, height):
    data.append([])

for i in range(0, height):
    for j in range(0, width):
        if i % 2 == 0:
            data[i].append(1)
        else:
            data[i].append(0)

print(data)
print(DCT(data, width, height))
print(iDCT(DCT(data, width, height), width, height))
