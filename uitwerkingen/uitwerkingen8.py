
common = ["The legend of Zelda", "Mario", "GTA6"]
uncommon= ["Dispatch", "Undertale", "Spider-Man"]
rare = ["PEAK", "Portal", "Helldivers"]

punten = 0
while True:
    game_in = input("raad een game: ")
    if game_in in common:
        print("common")
        punten += 10
    elif game_in in uncommon:
        punten += 30
        print("uncommen")
        break
    elif game_in in rare:
        punten += 50
        print("rare")
        break
    else:
        print("game niet gevonden probeer opnieuwe")

print(f'je hebt {punten} punten')