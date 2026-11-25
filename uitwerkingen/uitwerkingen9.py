
spelers =  {"Zwab":10, "Ruben": 3, "Tijs":5}

def puntAftrekken(spelers, naam_in):
    for naam in spelers.keys():
        if naam == naam_in:
            spelers[naam] -= 1

def puntGeven(spelers, naam_in):
    for naam in spelers.keys():
        if naam == naam_in:
            spelers[naam] += 1

puntAftrekken(spelers, "Zwab")
print(spelers)
puntGeven(spelers, "Ruben")
print(spelers)