
import time

users = [
  { "id": '1', "name": 'John Smith', "age": 20, "hasDog": True },
  { "id": '2', "name": 'Ann Smith', "age": 24, "hasDog": False },
  { "id": '3', "name": 'Tom Jones', "age": 31, "hasDog": True },
  { "id": '4', "name": 'Rose Peterson', "age": 17, "hasDog": False },
  { "id": '5', "name": 'Alex John', "age": 25, "hasDog": True },
  { "id": '6', "name": 'Ronald Jones', "age": 63, "hasDog": True },
  { "id": '7', "name": 'Elton Smith', "age": 16, "hasDog": True },
  { "id": '8', "name": 'Simon Peterson', "age": 30, "hasDog": False },
  { "id": '9', "name": 'Daniel Cane', "age": 51, "hasDog": True },
]

time.sleep(2)

# 1. funkcija "filterDogOwers" - kaip argumentą priims masyvą ir duoto masyvo 
# atveju grąžins "users", kurie turi augintinį.

print('SUNU SEIMININKAI')

time.sleep(1)
def filterDogOwners(masyvas):
  # ieskome masyve users elementu kurie turi desired_result key ''hasDog"
  dog_owners = [x for x in masyvas if x['hasDog'] == True]
  # isvedame tik sunu augintiniu duomenis
  print (dog_owners)
  # panaudojame funkcija paduodant masyva
filterDogOwners(users)

# ANTRA VERSIJA

# def filterDogOwners2(masyvas):
#   masyvas4 = []
#   # naudojam for loopa
#   for x in masyvas:
#     # pridedam users kurie turi sunis nauja masyva
#     if x['hasDog'] == True:
#       masyvas4.append(x)
#   print(masyvas4)

# filterDogOwners2(users)
# ......................................................................

# 2. funkcija "filterAdults" - kaip argumentą priims masyvą ir duoto masyvo 
# atveju grąžins masyvą su "users", kurie yra pilnamečiai.

time.sleep(2)

print('SUAUGUSIEJI')

time.sleep(1)
def filterAdults(masyvas):
  # ieskome masyve users kuru key 'age' yra daugiau arba lygu 18
  adults = [x for x in masyvas if x['age'] >= 18]
  # isvedame tik suaugusiu users duomenis
  print (adults)
  # panaudojam funkcija paduodant masyva
filterAdults(users)
time.sleep(2)

# ANTRA VERSIJA

# def filterAdults2(masyvas):
#   masyvas5 = []
#   # naudojam for loopa
#   for x in masyvas:
#     if x['age'] >= 18:
#       # pridedam prie naujo masyvo
#       masyvas5.append(x)
#   print(masyvas5)

# filterAdults2(users)