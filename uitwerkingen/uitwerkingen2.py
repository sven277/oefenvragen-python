def plusSom():
    sum = 0
    while True:
        userInput = input("geef me een getal ")
        if userInput == "stop":
            return sum
        else:
            sum += int(userInput)

print(plusSom())