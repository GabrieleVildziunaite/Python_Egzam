# Turimas "audi" dict.

# Parašykite funkciją "showObjectKeys", kuri kaip argumentą priims objektą 
# ir grąžins visus jo "values" list'e.
import time
audi = {
  "make": 'audi',
  "model": 'A6',
  "year": 2005,
  "color": 'white',
}

def showObjectKeys (objektas):
# isvedame visas values liste
  time.sleep(1)
  print('VISOS VALUES: ')
  time.sleep(2)   
  print(list(objektas.values()))
  time.sleep(2) 
  print('VISI KEYS: ')
  time.sleep(2)   
# Nesu tikra ar tikrai uzduotis prase "values", nes uzduotyje finkcija pavadinta showObjectKeys 
# o ne values tai pridedu ir keys del visa ko  
  print(list(objektas.keys()))
  
# panaudojam funkcija su audi
showObjectKeys(audi)
time.sleep(2)