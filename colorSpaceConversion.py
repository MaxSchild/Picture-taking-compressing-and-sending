#color space conversion and chroma subsampling
import random

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

def rgbToYCbCr_4_1_1(redArray, greenArray, blueArray):
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


#main programm

#informations about the image
#numbers are just exmamples
width = 16
height = 8

#creating one-dimensional arrays, containing the pixel values of an image
redArray = []
greenArray = []
blueArray = []

#also one-dimensional arrays
yArray = []
cbArray = []
crArray = []

"""
#test if space color conversion works:
red = random.randint(0, 255)
green = random.randint(0, 255)
blue = random.randint(0, 255)

y = rgbToY(red, green, blue)
cb = rgbToCb(red, green, blue)
cr = rgbToCr(red, green, blue)
print("r, g, b:", red, green, blue)
print("y, cb, cr:", y, cb, cr)


red2 = yCbCrToR(y, cr)
green2 = yCbCrToG(y, cb, cr)
blue2 = yCbCrToB(y, cb)

difRed = red2 - red
difGreen = green2 - green
difBlue = blue2 - blue
print(type(red2))
print("Differences:")
print("red:", difRed , "green:", difGreen , "blue:", difBlue)#difference is nearly zero -> seems to be right
"""

for i in range(0, width * height):
    redArray.append(random.randint(0, 255))
    blueArray.append(random.randint(0,255))
    greenArray.append(random.randint(0, 255))
print("Created image")

yArray, cbArray, crArray = rgbToYCbCr_4_2_0(redArray, greenArray, blueArray, width, height)
#print(crArray)
print(len(yArray), len(cbArray))
print(len(yArray) / len(cbArray))

#seems to work !!!


