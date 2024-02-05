from math import floor as fl

def nb_year(p0, percent, aug, p):
    rate = percent / 100
    pop = p0
    counter = 0
    while pop < p:
        pop += fl(aug + (pop * rate))
        counter += 1
    return counter
