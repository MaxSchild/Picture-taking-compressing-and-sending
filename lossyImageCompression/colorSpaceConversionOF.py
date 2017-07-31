#color space conversion and chroma subsampling

#creating the functions for the color space conversion
def rgbToY(red, green, blue):
    y = 0.299 * red + 0.587 * green + 0.114 * blue
    return y

def rgbToCb(red, green, blue):
    cb = (-0.1687) * red - 0.3313 * green + 0.5 * blue + 128
    return cb

def rgbToCr(red, green, blue):
    cr = 0.5 * red - 0.4187 * green - 0.0813 * blue + 128
    return cr

def yCbCrToR(y, cr):
    red = y + 1.402 * (cr - 128)
    return red

def yCbCrToG(y, cb, cr):
    green = y - (0.34414 * (cb - 128)) - (0.71414 * (cr - 128))
    return green

def yCbCrToB(y, cb):
    blue = y + 1.772 * (cb - 128)
    return blue

#this function does the space conversion and 4:2:0 chroma subsampling
def rgbToYCbCr_4_2_0(redArray, greenArray, blueArray, width, height):
    yArray = []
    cbArray = []
    crArray = []
    #getting the pixels of an image
    for color in range(0, width * height):
        red = redArray[color]
        green = greenArray[color]
        blue = blueArray[color]
        y = rgbToY(red, green, blue)
        yArray.append(y)
        #if column and row are multiples of 2 append pixels
        #there might be a better method to do the subsampling
        column = color % width
        row = int((color - column) / width)
        if column % 2 == 0 and row % 2 == 0:
            cb = rgbToCb(red, green, blue)
            cr = rgbToCr(red, green, blue)
            cbArray.append(cb)
            crArray.append(cr)
    return yArray, cbArray, crArray

def rgbToYCbCr_4_2_2(redArray, greenArray, blueArray, width, height):
    yArray = []
    cbArray = []
    crArray = []
    #getting the pixels of an image
    for color in range(0, width * height):
        red = redArray[color]
        green = greenArray[color]
        blue = blueArray[color]
        y = rgbToY(red, green, blue)
        yArray.append(y)
        #if column is a multiple of 2 append pixels
        #there might be a better method to do the subsampling
        column = color % width
        if column % 2 == 0:
            cb = rgbToCb(red, green, blue)
            cr = rgbToCr(red, green, blue)
            cbArray.append(cb)
            crArray.append(cr)
    return yArray, cbArray, crArray


def rgbToYCbCr_4_4_4(redArray, greenArray, blueArray, width, height):
    yArray = []
    cbArray = []
    crArray = []
    #getting the pixels of an image
    for color in range(0, width * height):
        red = redArray[color]
        green = greenArray[color]
        blue = blueArray[color]
        y = rgbToY(red, green, blue)
        yArray.append(y)
        cb = rgbToCb(red, green, blue)
        cr = rgbToCr(red, green, blue)
        cbArray.append(cb)
        crArray.append(cr)
    return yArray, cbArray, crArray

def rgbToYCbCr_4_1_1(redArray, greenArray, blueArray, width, height):
    yArray = []
    cbArray = []
    crArray = []
    #getting the pixels of an image
    for color in range(0, width * height):
        red = redArray[color]
        green = greenArray[color]
        blue = blueArray[color]
        y = rgbToY(red, green, blue)
        yArray.append(y)
        #if column is a multiples of 4 append pixels
        #there might be a better method to do the subsampling
        column = color % width
        if column % 4 == 0:
            cb = rgbToCb(red, green, blue)
            cr = rgbToCr(red, green, blue)
            cbArray.append(cb)
            crArray.append(cr)
    return yArray, cbArray, crArray

def yCbCrToRGBFrom4_2_0(yArray, cbArray ,crArray, width, height):
    newRedArray = []
    newGreenArray = []
    newBlueArray = []
    #need to define them here because they don't have to be calculate new for each pixel
    cb = 0
    cr = 0
    for color in range(0, width * height):
        y = yArray[color]
        column = color % width
        row = int((color - column) / width)
        if column % 2 == 0: 
            indexCbCr = int(int(row / 2) * (width / 2) + int(column / 2))
            cb = cbArray[indexCbCr]
            cr = crArray[indexCbCr]
        red = yCbCrToR(y, cr)
        green = yCbCrToG(y, cb, cr)
        blue = yCbCrToB(y, cb)
        newRedArray.append(red)
        newGreenArray.append(green)
        newBlueArray.append(blue)

    return newRedArray, newGreenArray, newBlueArray

def yCbCrToRGBFrom4_2_2(yArray, cbArray ,crArray, width, height):
    newRedArray = []
    newGreenArray = []
    newBlueArray = []
    #need to define them here because they don't have to be calculate new for each pixel
    cb = 0
    cr = 0
    for color in range(0, width * height):
        y = yArray[color]
        column = color % width
        if column % 2 == 0: 
            indexCbCr =  int(color / 2)
            cb = cbArray[indexCbCr]
            cr = crArray[indexCbCr]
        red = yCbCrToR(y, cr)
        green = yCbCrToG(y, cb, cr)
        blue = yCbCrToB(y, cb)
        newRedArray.append(red)
        newGreenArray.append(green)
        newBlueArray.append(blue)

    return newRedArray, newGreenArray, newBlueArray


def yCbCrToRGBFrom4_4_4(yArray, cbArray ,crArray, width, height):
    newRedArray = []
    newGreenArray = []
    newBlueArray = []
    for color in range(0, width * height):
        y = yArray[color]
        cb = cbArray[color]
        cr = crArray[color]
        red = yCbCrToR(y, cr)
        green = yCbCrToG(y, cb, cr)
        blue = yCbCrToB(y, cb)
        newRedArray.append(red)
        newGreenArray.append(green)
        newBlueArray.append(blue)

    return newRedArray, newGreenArray, newBlueArray

def yCbCrToRGBFrom4_1_1(yArray, cbArray ,crArray, width, height):
    newRedArray = []
    newGreenArray = []
    newBlueArray = []
    #need to define them here because they don't have to be calculate new for each pixel
    cb = 0
    cr = 0
    for color in range(0, width * height):
        y = yArray[color]
        column = color % width
        row = int((color - column) / width)
        if column % 4 == 0: 
            indexCbCr =  int(color / 4)
            cb = cbArray[indexCbCr]
            cr = crArray[indexCbCr]
        red = yCbCrToR(y, cr)
        green = yCbCrToG(y, cb, cr)
        blue = yCbCrToB(y, cb)
        newRedArray.append(red)
        newGreenArray.append(green)
        newBlueArray.append(blue)

    return newRedArray, newGreenArray, newBlueArray

#making settings depending on subsampling mode
def colorSCAndChromaSS(redArray, greenArray, blueArray, width, height, subSMode):
    #let's create mode numbers for different subsamplings
    subS4_2_0 = 0
    subS4_2_2 = 1
    subS4_2_2 = 2
    subS4_4_4 = 3
    subS4_1_1 = 4
    subSWidthChroma = 1
    subSHeightChroma = 1

    yArray, cbArray, crArray = [], [], []

    if subSMode == subS4_2_0:
        yArray, cbArray, crArray = rgbToYCbCr_4_2_0(redArray, greenArray, blueArray, width, height)
        subSWidthChroma = int(width / 2)
        subSHeightChroma = int(height / 2)
    elif subSMode == subS4_2_2:
        yArray, cbArray, crArray = rgbToYCbCr_4_2_2(redArray, greenArray, blueArray, width, height)
        subSWidthChroma = int(width / 2)
    elif subSMode == subS4_4_4:
        yArray, cbArray, crArray = rgbToYCbCr_4_4_4(redArray, greenArray, blueArray, width, height)
    elif subSMode == subS4_1_1:
        yArray, cbArray, crArray = rgbToYCbCr_4_1_1(redArray, greenArray, blueArray, width, height)
        subSWidthChroma = int(width / 4)
    else:
        print("Problem with chroma subsampling!")
    return yArray, cbArray, crArray, subSWidthChroma, subSHeightChroma
