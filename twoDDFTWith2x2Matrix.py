#test programm for 2D DFT with a 2x2 matrix
import cmath
#meaning of the variables m, n, k, l
#m is the row of the array storing the values
#n in the column ""  "" ...
#k is the row of the array storing the frequency coefficients
#l is the column "" "" ...

def twoDDFT(matrix):
    coeff = [[], []]
    for k in range(0, len(matrix)):
        for l in range(0, len(matrix[k])):
            coefficient = 0
            for m in range(0, len(matrix)):
                for n in range(0, len(matrix[m])):
                    fn = matrix[m][n] #fn is the value
                    #the formula isn't kept general
                    #it's already adapted to the size of the matrix
                    coefficient += fn * cmath.exp((-1) * cmath.pi * 1j * (m * k + n * l))
            coeff[k].append(coefficient)
    return coeff

def twoDiDFT(coeff):
    matrix = [[],[]]
    for m in range(0, len(coeff)):
        for n in range(0, len(coeff[m])):
            value = 0
            for k in range(0, len(coeff)):
                for l in range(0, len(coeff[k])):
                    coefficient = coeff[k][l]
                    value += coefficient * cmath.exp(cmath.pi * 1j * (m * k + n * l))
            matrix[m].append((1/4) * value)
    return matrix


#main programm
matrix = [[1, 0], [0, 1]]
print(twoDiDFT(twoDDFT(matrix))) # works!
