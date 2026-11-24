gebruiker = "Sven"
wachtwoord = "RubenHeeftEenMooieBaard"

gebruiker_in = input("gebruikersnaam: ")
wachtwoord_in = input("wachtwoord: ")

if gebruiker_in == gebruiker and wachtwoord_in == wachtwoord:
    print("welkom")
elif gebruiker_in == gebruiker and wachtwoord_in != wachtwoord:
    print("incorrect wachtwoord")
else:
    print("incorrecte combinatie van gebruikersnaam en wachtwoord")