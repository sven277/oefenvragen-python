treintijden = {"Utrecht-Schiphol":"12:30", "Utrecht-Rotterdam": "14:10", "Rotterdam-Amsterdam Centraal": "13:45", "Driebergen-Utrecht":"15:05" }

# Je hebt een dictionary met treintijden,
# maar met de stakingen in het OV gebeurt het soms dat er een trein te laat vertrekt.

# Schrijf hieronder code waar je de gebruiker voor route vraagt (o.a Utrecht-Schiphol).
# Zorg er dan voor dat de gebruiker een latere tijd in kan voeren die de huidige vertektijd vervangt.

route = input("Welke route wilt u aanpassen?")
nieuweTijd = input("Wanneer is de vertrektijd?")
treintijden[route] = nieuweTijd

print(treintijden[route])