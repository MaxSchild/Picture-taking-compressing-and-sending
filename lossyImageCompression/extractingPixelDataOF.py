from PIL import Image

def takeBMPReturnSizeAndColorArrays(imageName):
    image = Image.open(imageName)
    #image.convert("RGB")
    width = image.size[0]
    height = image.size[1]
    
    #creating arrays conating the RGB-Values of the image
    redArray = []
    greenArray = []
    blueArray = []

    for y in range(0, height):
        for x in range(0, width):
            red, green, blue = image.getpixel((x,y))
            redArray.append(red)
            greenArray.append(green)
            blueArray.append(blue)
    #works
    return width, height, redArray, greenArray, blueArray

def createNewImage(width, height, redArray, greenArray, blueArray, newImageName, imageFormat):
    #creating a new picture
    newImage = Image.new("RGB", (width, height))
    #pixels first will be black
    pix = newImage.load()

    for i in range(0, width * height):
        x = i % width
        y = int((i - x) / width)
        #let's try round the values!
        #Because RGB values are integers!
        colorTuple = round(redArray[i]), round(greenArray[i]), round(blueArray[i])
        #pixels are filled with colors
        pix[x,y] = colorTuple

    newImage.save(newImageName, imageFormat)
