# Importuokite reikiamus modulius, kad veiktų žemiau nurodytos funkcijos

# Importuojame visus modulius pagal folderiu kuriuose jie yra,
# kelis reikia pervadinti kad veiktu funkcijos (addition/division) 

from modules.math.composition import composition as addition
from modules.math.division import  division as divivsion
from modules.math.multiplication import *
from modules.math.subtraction import *
from modules.numbers.numbers import *

# Kitų failų ir žemiau esančio kodo nekeiskite
a = addition(one, four);
b = divivsion(four, two);
c = substraction(three, two);
d = multiplication(five, two);

print(a);
print(b);
print(c);
print(d);
