#this function will take an 1-D-Array and return a 3-D-Array with same values
#It will contain blocks, which contain 8 rows, which contain 8 pixels/colors
def blockArray8x8(bildArray, width, height):
    numberBlocks = int(width * height / 64)
    #this constant will be needed by filling the new Array
    blocksInRow = int(width / 8)
    array3D = []
    for i in range(0, numberBlocks):
        #appending blocks and rows in one step
        array3D.append([[],[],[],[],[],[],[],[]])

    #the array3D will be filled with values
    for j in range(0, len(bildArray)):
        #getting the y- and x-coordinates from the former picture
        x = j % width
        y = int((j - x) / width)
        #sorting into array3D and appending the value
        blockRow = int((y - (y % 8)) / 8)
        blockColumn = int((x - (x % 8)) / 8)
        block = blockRow * blocksInRow + blockColumn
        row = y - blockRow * 8
        array3D[block][row].append(bildArray[j])

    return array3D


#this functions removes what rhw blockArray8x8 did
def oneDArray(array3D, width, height):
    numberBlocks = int(width * height / 64)
    blocksInRow = int(width / 8)
    bildArray = []


    for j in range(0, width * height):
        x = j % width
        y = int((j - x) / width)
        blockRow = int((y - (y % 8)) / 8)
        blockColumn = int((x - (x % 8)) / 8)
        block = blockRow * blocksInRow + blockColumn
        row = y - blockRow * 8
        column = x % 8
        bildArray.append(array3D[block][row][column])

    return bildArray
