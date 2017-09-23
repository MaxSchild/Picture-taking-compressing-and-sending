import math

def dct2D(bildArray):

  #ergebnisArray wird angelegt
  ergebnisArray = []
  #zeilen des Arrays werden mit Spalten befuellt
  for k in range(0,8):
    ergebnisArray.append([])

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
	#added int rounding because you need integers for an rgb image	
      bildArray[m].append(int(value))
  return bildArray

