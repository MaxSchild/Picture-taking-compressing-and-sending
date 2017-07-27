# discrete Fourier Transformation

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
                    #formula may be wrong, maybe change x and y in formula?
                    addend = value * cmath.exp(-(1) * cmath.sqrt(-1) * 2 * cmath.pi * (i * y + j * x) / (height * width))
                    coefficient += addend
            #appending the coefficient to the coefficientArray
            coefficientsArray[y].append(coefficient)
    return coefficientsArray

def iDFT(coefficientsArray, width, height):
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
                    coefficient = coefficientsArray[i][j]
                    addend = coefficient * cmath.exp(cmath.sqrt(-1) * 2 * cmath.pi * (i * y + j * x) / (height * width))
                    value += addend
            value = value * (1 / (height * width)) #sometihing
            #appending the value to the data-array
            data[y].append(value)
    return data

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
        if i % 2 == 0:
            data[i].append(1)
        else:
            data[i].append(0)
#print(data)

#print(iDFT(DFT(data, width, height), width, height))
coefficientsArray = []
for i in range(0, height):
    coefficientsArray.append([])

for i in range(0, height):
    for j in range(0, width):
        if (i == 0 and j == 0) or (i == 4 and j == 0):
            coefficientsArray[i].append(32 + 0 * cmath.sqrt(-1))
        else:
            coefficientsArray[i].append(0 + 0 * cmath.sqrt(-1))

print(coefficientsArray) 
print(iDFT(coefficientsArray, height, width)) # should be: 1,1,1,1..0,0,0,0,0...1,1,1,1...

