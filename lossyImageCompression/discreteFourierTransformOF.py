# discrete Fourier Transformation

import cmath

def DFT(data, width, height):
    #creating an Array which will later contain the fourier-coefficients
    coefficientsArray = []
    #giving the right structure to the array
    for i in range(0, height):
        coefficientsArray.append([])
    
    #creating an array of fourier-coefficients
    for k in range(0, height):
        for l in range(0, width):
            # creating a single fourier-coefficient
            coefficient = 0
            for m in range(0, height):
                for n in range(0, width):
                    #value shows the intensity, e.g. of a colour of a pixel
                    value = data[m][n]
                    #formula is right!!!
                    addend = value * cmath.exp((-2) * 1j  * cmath.pi * ((m * k / height) + (n * l / width)))
                    coefficient += addend
            #appending the coefficient to the coefficientArray
            coefficientsArray[k].append(coefficient)
    return coefficientsArray

def iDFT(coefficientsArray, width, height):
    #creating an Array which will store the values of the pixels 
    data = []
    #giving the right structure to the array

    for i in range(0, height):
        data.append([])

    #creating an array of colour-values
    for m in range(0, height):
        for n in range(0, width):
            #creating a single value
            value = 0
            for k in range(0, height):
                for l in range(0, width):
                    coefficient = coefficientsArray[k][l]
                    addend = coefficient * cmath.exp(2 * cmath.pi * 1j * ((m * k / height) + (n * l / width)))
                    value += addend
            value = value * (1 / (height * width))
            #it makes more sense only to return the rounded real part of the numbers,
            #because the input is an integer
            realValue = round(value.real)
            #appending the real part of the value to the data-array
            data[m].append(realValue)
    return data
