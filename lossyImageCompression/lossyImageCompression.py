import colorSpaceConversionOF as CSC
import discreteFourierTransformOF as DFT
import extractingPixelDataOF as EPD
import sortingInto8x8BlocksOF as SIB

#testing how long it takes
import time

#image compression
startTime = time.time()
#necessary: imageName and position
imageName = "astronaut.bmp"

#getting image (rgb) values
width, height, redArray, greenArray, blueArray = EPD.takeBMPReturnSizeAndColorArrays(imageName)
print("Got the RGB values!")
newTime = time.time()
duration = int(newTime - startTime)
seconds = duration % 60
minutes = int((duration - seconds) / 60)
print("It took", minutes, "minutes and",seconds, "seconds!" )
startTime = newTime


#color space conversion into ycbcr and chroma subsampling
yArray, cbArray, crArray = CSC.rgbToYCbCr_4_2_0(redArray, greenArray, blueArray, width, height)
print("Converted into yCbCr!")
newTime = time.time()
duration = int(newTime - startTime)
seconds = duration % 60
minutes = int((duration - seconds) / 60)
print("It took", minutes, "minutes and",seconds, "seconds!" )
startTime = newTime

#sorting into 8x8-Blocks, separate for y, cb and cr
yArray3D = SIB.blockArray8x8(yArray, width, height)
subsamplingFactorWidth = 0.5
subsamplingFactorHeight = 0.5
#let's assume the subsampling for is 4:2:0 ...

cbArray3D = SIB.blockArray8x8(cbArray, int(subsamplingFactorWidth * width), int(subsamplingFactorHeight * height))
crArray3D = SIB.blockArray8x8(crArray, int(subsamplingFactorWidth * width), int(subsamplingFactorHeight * height))
print("Sorted into Blocks!")
newTime = time.time()
duration = int(newTime - startTime)
seconds = duration % 60
minutes = int((duration - seconds) / 60)
print("It took", minutes, "minutes and",seconds, "seconds!" )
startTime = newTime

#transformation, also for each "color"
coefficientsArrayY3D = []
coefficientsArrayCb3D = []
coefficientsArrayCr3D = []
for i in yArray3D:
    coefficientsArrayY = DFT.DFT(i, 8, 8)
    coefficientsArrayY3D.append(coefficientsArrayY)
for i in cbArray3D:
    coefficientsArrayCb = DFT.DFT(i,  8, 8)
    coefficientsArrayCb3D.append(coefficientsArrayCb)
for i in crArray3D:
    coefficientsArrayCr = DFT.DFT(i, 8, 8 )
    coefficientsArrayCr3D.append(coefficientsArrayCr)
print("Transformed into coefficients!")
newTime = time.time()
duration = int(newTime - startTime)
seconds = duration % 60
minutes = int((duration - seconds) / 60)
print("It took", minutes, "minutes and",seconds, "seconds!" )
startTime = newTime

#quantization
#no code yet

#coding
#no code yet

#--------------------------------------------------

#image decompression

#decoding
#no code yet

#dequantization
#no code yet

#inverse transformation
newYArray3D = []
newCbArray3D = []
newCrArray3D = []
for i in coefficientsArrayY3D:
    newYArray3D.append(DFT.iDFT(i, 8, 8))
for i in coefficientsArrayCb3D:
    newCbArray3D.append(DFT.iDFT(i, 8, 8))
for i in coefficientsArrayCr3D:
    newCrArray3D.append(DFT.iDFT(i,8, 8))
print("Transformed into Data again!")
newTime = time.time()
duration = int(newTime - startTime)
seconds = duration % 60
minutes = int((duration - seconds) / 60)
print("It took", minutes, "minutes and",seconds, "seconds!" )
startTime = newTime

#inverse 8x8-Sorting
newYArray = SIB.oneDArray(newYArray3D, width, height)
newCbArray = SIB.oneDArray(newCbArray3D, int(subsamplingFactorWidth * width), int(subsamplingFactorHeight * height))
newCrArray = SIB.oneDArray(newCrArray3D, int(subsamplingFactorWidth * width), int(subsamplingFactorHeight * height))
print("Sorted into an one-dimensional Array again!")
newTime = time.time()
duration = int(newTime - startTime)
seconds = duration % 60
minutes = int((duration - seconds) / 60)
print("It took", minutes, "minutes and",seconds, "seconds!" )
startTime = newTime

#color space conversion to rgb
newRedArray, newGreenArray, newBlueArray = CSC.yCbCrToRGBFrom4_2_0(newYArray, newCbArray ,newCrArray, width, height)
print("Converted back to RGB!")
newTime = time.time()
duration = int(newTime - startTime)
seconds = duration % 60
minutes = int((duration - seconds) / 60)
print("It took", minutes, "minutes and",seconds, "seconds!" )
startTime = newTime

#saving the picture as rgb
newImageName = "newAstronaut.bmp"
imageFormat = "bmp"
#look out for the parameters!
EPD.createNewImage(width, height, newRedArray, newGreenArray, newBlueArray, newImageName, imageFormat)


print("Finished!")
