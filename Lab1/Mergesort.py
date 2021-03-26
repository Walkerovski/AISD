def ReadFromFile(fileName):
    array = []
    f = open(fileName, "r")
    for character in f.read():
        array.append(character)
    f.close()
    return array


def MergeArrays(fragment1, fragment2, array):
    i = 0
    j = 0
    k = 0
    while i < len(fragment1) and j < len(fragment2):
        if fragment1[i] < fragment2[j]:
            array[k] = fragment1[i]
            i += 1
        else:
            array[k] = fragment2[j]
            j += 1
        k += 1
    while i < len(fragment1):
        array[k] = fragment1[i]
        i += 1
        k += 1
    while j < len(fragment2):
        array[k] = fragment2[j]
        j += 1
        k += 1


def Mergesort(array):
    if len(array) > 1:
        middle = len(array)//2
        fragment1 = array[:middle]
        fragment2 = array[middle:]
        Mergesort(fragment1)
        Mergesort(fragment2)
        MergeArrays(fragment1, fragment2, array)
    return array


if __name__ == "__main__":
    text = ReadFromFile("lorem_ipsum.txt")
    sorted = Mergesort(text)
    print(sorted)
