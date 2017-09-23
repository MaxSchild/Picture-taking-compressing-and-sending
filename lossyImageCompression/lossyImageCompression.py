import colorSpaceConversionOF as CSC
import discreteFourierTransformOF as DFT
import extractingPixelDataOF as EPD
import sortingInto8x8BlocksOF as SIB
import printMinutesAndSecondsOF as PMS
import discreteCosineTransformOF as DCT
import quantizationOF as QTZ


#testing how long it takes
import time


def compressImageAndSaveNewOne(imageName, subSMode, quantMatrix, newImageName):
    #image compression
    startTime = time.time()
    #necessary: imageName and position
    #imageName = "spaceSmall.bmp"

    #getting image (rgb) values
    width, height, redArray, greenArray, blueArray = EPD.takeBMPReturnSizeAndColorArrays(imageName)
    print("Got the RGB values!")
    startTime = PMS.printMinutesAndSeconds(startTime)


    #color space conversion into ycbcr and chroma subsampling
    yArray, cbArray, crArray, subSWidthChroma, subSHeightChroma = CSC.colorSCAndChromaSS(redArray, greenArray, blueArray, width, height, subSMode)

    print("Converted into yCbCr!")
    startTime = PMS.printMinutesAndSeconds(startTime)

    #sorting into 8x8-Blocks, separate for y, cb and cr
    yArray3D = SIB.blockArray8x8(yArray, width, height)

    cbArray3D = SIB.blockArray8x8(cbArray, subSWidthChroma, subSHeightChroma)
    crArray3D = SIB.blockArray8x8(crArray, subSWidthChroma, subSHeightChroma)
    print("Sorted into Blocks!")
    startTime = PMS.printMinutesAndSeconds(startTime)

    #transformation, also for each "color"
    coefficientsArrayY3D = []
    coefficientsArrayCb3D = []
    coefficientsArrayCr3D = []
    for i in yArray3D:
        coefficientsArrayY = DCT.dct2D(i) #DFT.DFT(i, 8, 8)
        coefficientsArrayY3D.append(coefficientsArrayY)
    for i in cbArray3D:
        coefficientsArrayCb = DCT.dct2D(i) #DFT.DFT(i,  8, 8)
        coefficientsArrayCb3D.append(coefficientsArrayCb)
    for i in crArray3D:
        coefficientsArrayCr = DCT.dct2D(i) #DFT.DFT(i, 8, 8 )
        coefficientsArrayCr3D.append(coefficientsArrayCr)
    print("Transformed into coefficients!")
    startTime = PMS.printMinutesAndSeconds(startTime)

    #quantization
    quantizedArrayY3D = []
    quantizedArrayCb3D = []
    quantizedArrayCr3D = []
    
    for i in coefficientsArrayY3D:
        quantizedArrayY3d.append(QTZ.quantize(quantMatrix, i))
    for i in coefficientsArrayCb3D:
        quantizedArrayCb3d.append(QTZ.quantize(quantMatrix, i))
    for i in coefficientsArrayCr3D:
        quantizedArrayCr3d.append(QTZ.quantize(quantMatrix, i))
        

    #coding
    #no code yet

    #--------------------------------------------------

    #image decompression

    #decoding
    #no code yet

    #dequantization
    dequantizedArrayY3D = []
    dequantizedArrayCb3D = []
    dequantizedArrayCr3D = []
    
    for i in coefficientsArrayY3D:
        dequantizedArrayY3D.append(QTZ.dequantize(quantMatrix), i)
    for i in coefficientsArrayCb3D:
        dequantizedArrayCb3D.append(QTZ.dequantize(quantMatrix), i)
    for i in coefficientsArrayCr3D:
        dequantizedArrayCr3D.append(QTZ.dequantize(quantMatrix), i)
        
        
    #inverse transformation
    newYArray3D = []
    newCbArray3D = []
    newCrArray3D = []
    for i in dequantizedArrayY3D:
        newYArray3D.append(iDct2D(i)) #DFT.iDFT(i, 8, 8))
    for i in dequantizedArrayCb3D:
        newCbArray3D.append((iDct2D(i)) #DFT.iDFT(i, 8, 8))
    for i in dequantizedArrayCr3D:
        newCrArray3D.append((iDct2D(i)) #DFT.iDFT(i,8, 8))
    print("Transformed into Data again!")
    startTime = PMS.printMinutesAndSeconds(startTime)

    #inverse 8x8-Sorting
    newYArray = SIB.oneDArray(newYArray3D, width, height)
    newCbArray = SIB.oneDArray(newCbArray3D, subSWidthChroma, subSHeightChroma)
    newCrArray = SIB.oneDArray(newCrArray3D, subSWidthChroma, subSHeightChroma)
    print("Sorted into an one-dimensional Array again!")
    startTime = PMS.printMinutesAndSeconds(startTime)

    #color space conversion to rgb
    newRedArray, newGreenArray, newBlueArray = CSC.yCbCrToRGBFrom4_2_0(newYArray, newCbArray ,newCrArray, width, height)
    print("Converted back to RGB!")
    startTime = PMS.printMinutesAndSeconds(startTime)

    #saving the picture as rgb
    #newImageName = "newSpace.bmp"
    imageFormat = "bmp"
    #look out for the parameters!
    EPD.createNewImage(width, height, newRedArray, newGreenArray, newBlueArray, newImageName, imageFormat)


    print("Finished!")

#possible subsampling modes
subS4_2_0 = 0
subS4_2_2 = 1
subS4_4_4 = 2
subS4_1_1 = 3


#main programm:
#don't forget to set names and suffixes!
imageName = "spaceSmall.bmp"
subSMode = subS4_2_0 #set mode for color subsampling
newImageName = "newSpaceSamll.bmp"
compressImageAndSaveNewOne(imageName, subSMode, newImageName)


