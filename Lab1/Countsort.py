def ReadFromFile(fileName):
    array = []
    f = open(fileName, "r")
    for character in f.read():
        array.append(character)
    f.close()
    return array


def Countsort(array):
    tempArray = [0] * 127
    sortedArray = []
    for character in array:
        charNum = ord(character)
        tempArray[charNum] += 1
    charNum = 0
    for entry in tempArray:
        for i in range(0, entry):
            sortedArray.append(chr(charNum))
        charNum += 1
    return sortedArray


if __name__ == "__main__":
    text = ReadFromFile("lorem_ipsum.txt")
    sorted = Countsort(text)
    print(sorted)
