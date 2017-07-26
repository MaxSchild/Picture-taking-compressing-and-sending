#one-diemensional fourier-transform and test with complex numbers
import cmath

#setting a complex number
matrix = [1, 0, -1, 0]
coeff = []

z = 0 + 0 * 1j
z.real = 1
z.imag = 1
print(z)


#cmath.exp is the same like e ** x

firstCoefficient = cmath.exp(-2*cmath.pi*1j * 2 / 4) * (-1)
cos = cmath.cos(-2 * cmath.pi * 2 / 4)
sin = cmath.sin(-2 * cmath.pi * 2 / 4)
print(cos)#should be -1
print((sin)#should be 0
firstCoefficientTrig = (-1) * ((cos + sin * 1j))
print(firstCoefficient)#the real part is right
print(firstCoefficient.imag -1)#should be -1 and not -0.999999999
print(firstCoefficientTrig)

for k in range(0, len(matrix)):
    coefficient = 0
    for n in range(0, len(matrix)):
        coefficient += matrix[n] * cmath.exp(-2 * cmath.pi * 1j * k * n / 4)
    coeff.append(coefficient)

for real in coeff:
    print(real.real)

