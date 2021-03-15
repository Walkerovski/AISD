dictionary = {
    "A": ".-",
    "J": ".---,",
    "S": "...",
    "B": "-...",
    "K": "-.-",
    "T": "-",
    "C": "-.-.",
    "L": ".-..",
    "U": "..-",
    "D": "-..",
    "M": "--",
    "V": "...-",
    "E": ".",
    "N": "-.",
    "W": ".--",
    "F": "..-.",
    "O": "---",
    "X": "-..-",
    "G": "--.",
    "P": ".--.",
    "Y": "-.--",
    "H": "....",
    "Q": "--.-",
    "Z": "--..",
    "I": "..",
    "R": ".-.",
    " ": "/",
}

with open ("plik.txt", "r") as data:
    input_user = data.read().replace('\n', 'z')
output = "  "
for x in input_user:
    if (x == "z"):
        print(output[2:])
        output = "  "
        continue
    if (output[-2] != "/" or dictionary[x.upper()] != "/"):
        output += dictionary[x.upper()]
        output += " "
print(output[2:])