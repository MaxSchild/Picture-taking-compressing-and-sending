#quantisation
matrixMidQ = [[16, 11, 10, 16, 24, 40, 51, 61],
[12, 12, 14, 19, 26, 58, 60, 55],
[14, 13, 16, 24, 40, 57, 69, 56],
[14, 17, 22, 29, 51, 87, 80, 62],
[18, 22, 37, 56, 68, 109, 103, 77],
[24, 35, 55, 64, 81, 104, 113, 92],
[49, 64, 78, 87, 103, 121, 120, 101],
[72, 92, 95, 98, 112, 100, 103, 99]]

matrixHighQ = [[8, 16, 19, 22, 26, 27, 29, 34],
[16, 16, 22, 24, 27, 29, 34, 37],
[19, 22, 26, 27, 29, 34, 34, 38],
[22, 22, 26, 27, 29, 34, 37, 40],
[22, 26, 27, 29, 32, 35, 40, 48],
[26, 27, 29, 32, 35, 40, 48, 58],
[26, 27, 29, 34, 38, 46, 56, 69],
[27, 29, 35, 38, 46, 56, 69, 83]]

matrixLowQ = [[62, 65, 57, 60, 72, 63, 60, 82],
[57, 55, 56, 82, 108, 87, 62, 71],
[58, 50, 60, 111, 148, 114, 67, 65],
[65, 55, 66, 120, 155, 114, 68, 70],
[70, 63, 67, 101, 122, 88, 60, 78],
[71, 71, 64, 70, 80, 62, 56, 81],
[75, 82, 67, 54, 63, 65, 66, 83],
[81, 94, 75, 54, 68, 81, 81, 87]]



print(matrix)
def quantize(matrix, block8x8):
  quantizedArray = []
  for row in range(0,8):
    quantizedArray.append([])

  #for rows
  for k in range(0, 8):
    #for columns
    for l in range(0,8):
      #quantize values and apend to quantizedArray
      quantizedCoeff = int(block8x8[k][l] / matrix[k][l])
      quantizedArray[k].append(quantizedCoeff)
  return quantizedArray

def dequantize(matrix, qBlock8x8):
  dequantizedArray = []
  for row in range(0,8):
    dequantizedArray.append([])
  for k in range(0, 8):
  #for columns
    for l in range(0,8):
      #quantize values and apend to quantizedArray
      deQuantizedCoeff = qBlock8x8[k][l] * matrix[k][l]
      dequantizedArray[k].append(deQuantizedCoeff)
  return dequantizedArray

