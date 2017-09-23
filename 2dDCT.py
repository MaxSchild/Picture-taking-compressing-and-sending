import math
import random #for testing
import time
def dct2D(bildArray):

  #ergebnisArray wird angelegt
  ergebnisArray = []
  #zeilen des Arrays werden mit Spalten befuellt
  for k in range(0,8):
    ergebnisArray.append([])
  #print(ergebnisArray)
  #print("Jetzt folgt etwas Gleitpunkt-Arithmetik.Bitte etwas Geduld.")
  #durch die zeilen des neuen Arrays gehen
  for k in range(0,8):
  #durch die Spalten des neuen Arrays gehen
    for l in range(0,8):
		
      #coefficient
      coefficient = 0
      #durch die Zeilen im alten Array gehen 
      for m in range(0,8):
        #durch die Spalten im alten Array gehen
        for n in range(0,8):
          wert = bildArray[m][n]
          coefficient +=  wert * math.cos(k * math.pi * ((2 * m) + 1) / 16) * math.cos(l * math.pi * ((2 * n) + 1) / 16)
      
      #schauen, ob am Rand -> anderer Faktor
      if k == 0 and l != 0: #((k==0)&&(l!=0))
        coefficient=coefficient*1/math.sqrt(2)
      elif l == 0 and k != 0: #((l==0)&&(k!=0))
        coefficient=coefficient*1/math.sqrt(2)
      elif l == 0 and k == 0: #((l==0)&&(k==0))
        coefficient = 0.5 * coefficient
  #anhaengen ins neue Array
      ergebnisArray[k].append(0.25 * coefficient)		

  return ergebnisArray


def iDct2D(ergebnisArray):
  bildArray = []
  for m in range(0, 8):
    bildArray.append([])
  #print("Jetzt folgt etwas Gleitpunkt-Arithmetik. Bitte etwas Geduld.")
  for m in range(0,8):
    for n in range(0,8):
      value = 0
      for k in range(0,8):
        for l in range(0,8):
          wert = ergebnisArray[k][l]
          summand = 0.25*wert*math.cos((((2*m)+1)*k*math.pi)/16)*math.cos((((2*n)+1)*l*math.pi)/16)
          if k != 0 and l == 0:
            summand=summand*1/math.sqrt(2)
          elif k==0 and l!=0:
            summand=summand*1/math.sqrt(2)
          elif k == 0 and l == 0:
            summand = 0.5 * summand 
          
          
          value += summand
      bildArray[m].append(value)
  return bildArray



#main programm
startTime = time.time()
tries = 100
bildArray = []
for i in range(0,8):
  bildArray.append([])
  for j in range(0,8):
    bildArray[i].append(random.randint(0,255))
for i in range(0, tries - 1):
  if i % 100 == 0:
    print("in the", i, "lap")

  ergebnisArray = dct2D(bildArray)
  neuesBildArray = iDct2D(ergebnisArray)
  #for m in range(0, 8):
  #  for n in range(0, 8):
  #    difference = bildArray[m][n] - neuesBildArray[m][n]
  #    if difference > 0.1 or difference < -0.1 :
  #      print("Too big difference")
  #      break
  for m in range(0,8):
    for n in range(0,8):
      bildArray[m][n] = random.randint(0,255)
endTime = time.time()
timeNeeded = endTime - startTime
seconds = timeNeeded % 60
minutes = (timeNeeded - seconds) / 60
print("finished all", tries, "tries!")
print("It needed", minutes, "minutes and", seconds, "seconds")