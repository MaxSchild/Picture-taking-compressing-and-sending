#print minutes and seconds
import time

def printMinutesAndSeconds(startTime):
    newTime = time.time()
    duration = int(newTime - startTime)
    seconds = duration % 60
    minutes = int((duration - seconds) / 60)
    print("It took", minutes, "minutes and",seconds, "seconds!" )
    startTime = newTime
    return startTime
