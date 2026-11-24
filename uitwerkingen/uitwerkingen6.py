nummerlst = [0, 1, 1, 1, 2, 2, 3, 5, 7, 8, 8, 8, 8]
# Vraag aan de gebruiker een nummer en print hoe vaak dat nummer in de nummerlijst zit.

num_in = int(input("Nummer: "))
#korte manier
print(nummerlst.count(num_in))

#lange manier
count = 0
for number in nummerlst:
    if number == num_in:
        count += 1
print(count)