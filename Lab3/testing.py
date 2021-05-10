import heap2
import heap3
import heap4
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
    heap2.printXML(heap, "heap2.xml")
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


def testInsertion3():
    times = []
    for i in range(10):
        heap = [-1]
        start = time.perf_counter()
        for j in range(i*10000):
            heap3.insert(heap, j)
        stop = time.perf_counter()
        times.append(stop-start)
    heap3.printXML(heap, "heap3.xml")
    return times


def testRemove3():
    times = []
    for i in range(10):
        heap = [-1]
        for j in numbers:
            heap2.insert(heap, j)
        start = time.perf_counter()
        for j in range(i*10000):
            heap3.remove(heap)
        stop = time.perf_counter()
        times.append(stop-start)
    return times


def testInsertion4():
    times = []
    for i in range(10):
        heap = [-1]
        start = time.perf_counter()
        for j in range(i*10000):
            heap4.insert(heap, j)
        stop = time.perf_counter()
        times.append(stop-start)
    heap4.printXML(heap, "heap4.xml")
    return times


def testRemove4():
    times = []
    for i in range(10):
        heap = [-1]
        for j in numbers:
            heap4.insert(heap, j)
        start = time.perf_counter()
        for j in range(i*10000):
            heap4.remove(heap)
        stop = time.perf_counter()
        times.append(stop-start)
    return times


if __name__ == "__main__":
    insertionTimes2 = testInsertion2()
    removeTimes2 = testRemove2()
    insertionTimes3 = testInsertion3()
    removeTimes3 = testRemove3()
    insertionTimes4 = testInsertion4()
    removeTimes4 = testRemove4()
    plt.plot(insertionTimes2)
    plt.plot(insertionTimes3)
    plt.plot(insertionTimes4)
    plt.title("Tworzenie kopca n elementów")
    plt.xlabel("Liczba elementów (w 10 tys.)")
    plt.ylabel("Czas (w sekundach)")
    plt.legend(["Kopiec 2-arny", "Kopiec 3-arny", "Kopiec 20-arny"])
    plt.savefig("insertionPlot.png")
    plt.clf()
    plt.plot(removeTimes2)
    plt.plot(removeTimes3)
    plt.plot(removeTimes4)
    plt.title("Usuwanie n elementów z kopca 300000 elementów")
    plt.xlabel("Liczba usuwanych elementów (w 10 tys.)")
    plt.ylabel("Czas (w sekundach)")
    plt.legend(["Kopiec 2-arny", "Kopiec 3-arny", "Kopiec 20-arny"])
    plt.savefig("removePlot.png")
