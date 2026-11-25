dobbelsteen1 = [1, 2, 3, 4, 5, 6]
dobbelsteen2 = [1, 2, 3, 4, 5, 6]

# Op 2 standaard dobbelstenen is 7 het makkelijkste nummer om te werpen.
# Schrijf Python code die berekend hoeveel manieren er zijn om een 7 te gooien.
# Let op:
# In deze opdracht worden de uitkomsten (dobbelsteen 1: 1, dobbelsteen 2: 6) en (dobbelsteen 1: 6, dobbelsteen 2: 1)
# als twee afzonderlijke mogelijkheden beschouwd.

# Deze uitwerking werkt zelfs als de dobbelsteen2 lijst verandert.
# Als je de combinaties hardcoded heb gecodeerd dan faalt de uitwerking bij het veranderen van de dobbelsteen2 lijst
sevensAantal = 0
for waarde1 in dobbelsteen1:
    for waarde2 in dobbelsteen2:
        if waarde1 + waarde2 == 7:
            sevensAantal += 1
print(sevensAantal)

dobbelsteen2 = [0, 2, 3, 4, 5, 7]

# Wat als de waardes op de tweede dobbelsteen veranderen?
# Werkt de code die je hebt geschreven voor de normale dobbelstenen nog steeds?