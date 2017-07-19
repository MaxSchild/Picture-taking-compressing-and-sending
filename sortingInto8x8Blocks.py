import random
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

#main programm------------------------------


#creating the arguments, the function will take
bildArray = [] #the one-dimensional Array 
width = 64
height = 16
#filling the Array with values
for i in range(0, height * width):
    bildArray.append(random.randint(0, 255))
#print(bildArray)
#print("--------------------------------------------")
array3D = blockArray8x8(bildArray, width, height)
#print(array3D)
oldArray = oneDArray(array3D, width, height)
#print(oldArray)
#print("Length bilArray:", len(bildArray), "Length oldArray:", len(oldArray))
#check if input and output are the same:

for i in range(0, width * height):
    if bildArray[i] != oldArray[i]:
        print("Fail!")
        print("bildArray:", bildArray[i], "oldArray:", oldArray[i])
print("Sucess!")
