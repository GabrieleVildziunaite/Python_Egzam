import time

users = [
  { "id": '1', "name": 'John Smith', "age": 20 },
  { "id": '2', "name": 'Ann Smith', "age": 24 },
  { "id": '3', "name": 'Tom Jones', "age": 31 },
  { "id": '4', "name": 'Rose Peterson', "age": 17 },
  { "id": '5', "name": 'Alex John', "age": 25 },
  { "id": '6', "name": 'Ronald Jones', "age": 63 },
  { "id": '7', "name": 'Elton Smith', "age": 16 },
  { "id": '8', "name": 'Simon Peterson', "age": 30 },
  { "id": '9', "name": 'Daniel Cane', "age": 51 },
]
# 1. funkcija "getUserAverageAge" - kaip argumentą priims masyvą ir duoto masyvo 
# atveju grąžins visų "users" amžiaus visurkį kaip skaičių.

def getUsersAverageAge(masyvas):
  # susikuriam tuscia masyva i kuri desime age elementus
  masyvas2 = []
  # kuriam for loopa kuriuo pereinam per kiekviena elementa ir randam visas age vertes
  for x in masyvas:
    # pridedam tik age value i nauja masyva
    masyvas2.append(x['age'])
    # randame vidutine naujo masyvo verte
    average_age = round(sum(masyvas2)/len(masyvas2))
  time.sleep(2)
  # isvedame nauja masyva su age vertemis
  print('Visi users age viename masyve: ', masyvas2)
  time.sleep(2)
  # isvedame users amziaus vidurki
  print('Vidutinis users amzius suapvalinus: ', average_age)

# panaudojam funkcija su users masyvu
getUsersAverageAge(users)

# 2. funkcija "getUsersNames" -  kaip argumentą priims masyvą ir duoto masyvo 
# atveju grąžins visų "users" vardus naujame list'e pvz., ['Alex John', 'Ann Smith'...].

# Pastaba: rezultatai turi būti išrikiuoti abėcėlės tvarka

def getUsersNames(masyvas):
  # susikuriam tuscia masyva i kuri desime name elementus
  masyvas3 = []
  # kuriam for loopa kuriuo pereinam per kiekviena elementa ir randam visas name vertes
  for x in masyvas:
    # pridedam tik name value i nauja masyva
    masyvas3.append(x['name'])
    # surikiuojame nauja masyva pagal abecele
    masyvas3.sort()
  time.sleep(2)
  # isvedame nauja masyva su vardais abeceles tvarka
  print('Visi users name viename masyve pagal abecele: ', masyvas3)

# panaudojam funkcija su users masyvu
getUsersNames(users)
time.sleep(2)

