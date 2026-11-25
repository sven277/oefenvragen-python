def klinkergetter(woord):
    klinkerlijst = ["a", "e", "i", "o", "u"]
    output = ""
    for letter in woord:
        if letter in klinkerlijst:
            output += letter
    return output

print(klinkergetter("alfabet"))