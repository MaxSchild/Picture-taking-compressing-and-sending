#one-diemensional fourier-transform and test with complex numbers
import cmath

#this function doesn't deliver the right results
def oneDDFT(matrix):
    coeff = []
    for k in range(0, len(matrix)):
        coefficient = 0
        for n in range(0, len(matrix)):
            #cmath.exp is the same like e ** x
            coefficient += matrix[n] * cmath.exp(-2 * cmath.pi * 1j * k * n / 4)
        coeff.append(coefficient)
    return coeff

#this function delivers the correct result
def oneDDFTWithRound(matrix):
    coeff = []
    for k in range(0, len(matrix)):
        coefficient = 0
        for n in range(0, len(matrix)):
            result = matrix[n] * cmath.exp(-2 * cmath.pi * 1j * k * n / 4)
            #here the result will be rounded to 14 digits behind the comma
            resultToReturn = round(result.real, 14) + round(result.imag, 14) * 1j
            coefficient += resultToReturn
        coeff.append(coefficient)
    return coeff


def iOneDDFT(coeff):
    matrix = []
    for n in range(0, len(coeff)):
        value = 0
        for k in range(0, len(coeff)):
            value += coeff[k] * cmath.exp(2 * cmath.pi * 1j * k * n / 4)
        matrix.append((1/4) * value)
    return matrix

def iOneDDFTWithRound(coeff):
    matrix = []
    for n in range(0, len(coeff)):
        value = 0
        for k in range(0, len(coeff)):
            result = coeff[k] * cmath.exp(2 * cmath.pi * 1j * k * n / 4)
            resultToReturn = round(result.real, 14) + round(result.imag, 15)
            value += resultToReturn
        matrix.append((1/4) * value)
    return matrix

#main programm
matrix = [1, 0, -1, 0]
print(iOneDDFTWithRound(oneDDFTWithRound(matrix)))
