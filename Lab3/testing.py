import heap2
import random
import time
import matplotlib.pyplot as plt

numbers = random.sample(range(0, 300000), 100000)


def testInsertion2():
    times = []
    for i in range(10):
        heap = [-1]
        start = time.perf_counter()
        for j in range(i*10000):
            heap2.insert(heap, j)
        stop = time.perf_counter()
        times.append(stop-start)
    return times


def testRemove2():
    times = []
    for i in range(10):
        heap = [-1]
        for j in numbers:
            heap2.insert(heap, j)
        start = time.perf_counter()
        for j in range(i*10000):
            heap2.remove(heap)
        stop = time.perf_counter()
        times.append(stop-start)
    return times


if __name__ == "__main__":
    insertionTimes2 = testInsertion2()
    removeTimes2 = testRemove2()
    plt.plot(insertionTimes2)
    plt.title("Tworzenie kopca n elementów")
    plt.xlabel("Liczba elementów (w 10 tys.)")
    plt.ylabel("Czas (w sekundach)")
    plt.legend(["Kopiec 2-arny"])
    plt.savefig("insertionPlot.png")
    plt.clf()
    plt.plot(removeTimes2)
    plt.title("Usuwanie n elementów z kopca 300000 elementów")
    plt.xlabel("Liczba usuwanych elementów (w 10 tys.)")
    plt.ylabel("Czas (w sekundach)")
    plt.legend(["Kopiec 2-arny"])
    plt.savefig("removePlot.png")
