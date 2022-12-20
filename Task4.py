# Sukurkite klasę "Movie", kuri gebės sukurti objektus 3 savybėm ir 1 metodu. 
# Naudojant šią klasę sukurkite bent du skirtingus objektus.

# Savybės:
# title: string
# director: string
# budget: number

# Metodas: 
# wasExpensive() - jeigu filmo "budget" yra daugiau nei 100 000 000 mln USD, tada grąžins True, kitu atveju False. 

import time
# kuriame klase su duotomis savybemis
class Movie:
    def __init__(self, title, director, budget):
        self.title = title
        self.director = director
        self.budget = budget
# programuojame repr kad lengviau butut patikrinti sukurtus elementus
    def __repr__(self):
        return (f'Title: {self.title}, director: {self.director}, budget: {self.budget}.')
# kuriame funkcija kuri tikrina ar tai buvo brangus filmas
    def wasExpensive(self):
        print(self.title, 'was expensive movie: ', self.budget > 100000000)
          
# kuriame 3 objektus su klase Movie
Maverik = Movie('Top Gun: Maverick', 'Joseph Kosinski', 170000000)
Jurassic_World  = Movie('Jurassic World: Dominion', 'Colin Trevorrow', 170000000)
Elvis = Movie('Elvis', 'Baz Luhrmann', 85000000)

# Patikrinam visus objektus
time.sleep(2)
print(Maverik)
time.sleep(1)
print(Jurassic_World)
time.sleep(1)
print(Elvis)
time.sleep(1)
time.sleep(2)
# Patikriman visus elemetus su funkcija wasExpensive
Maverik.wasExpensive()
time.sleep(2)
Jurassic_World.wasExpensive()
time.sleep(2)
Elvis.wasExpensive()
time.sleep(2)



