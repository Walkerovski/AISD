import stringSearchN
import time
import matplotlib.pyplot as plt


def readFirstWords(fileName, n):
    array = []
    with open(fileName, 'r') as file:
        for line in file:
            for word in line.split():
                array.append(word)
                if(len(array) == n):
                    return array


def readWholeFile(fileName):
    with open(fileName, 'r') as file:
        text = file.read().replace('\n', '')
    return text


def testNaive():
    times = []
    text = readWholeFile('pan-tadeusz.txt')
    for i in range(1, 11):
        strings = readFirstWords('pan-tadeusz.txt', i * 100)
        start = time.perf_counter()
        for string in strings:
            stringSearchN.find(string, text)
        stop = time.perf_counter()
        times.append(stop-start)
    return times


if __name__ == "__main__":
    naiveTimes = testNaive()
    plt.plot(naiveTimes)
    plt.title("Wyszukiwanie pierwszych n słów w całym pliku")
    plt.xlabel("Liczba elementów (w 100)")
    plt.ylabel("Czas (w sekundach)")
    plt.legend(["Algorytm naiwny"])
    plt.savefig("stringPlot.png")
