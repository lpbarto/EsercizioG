import sorts
import numpy as np
from timeit import default_timer as timer
import sys
import csv
import matplotlib.pyplot as plt

sys.setrecursionlimit(100000)

def test(nStart, nmax, gap):

    pmedia = 1

    row = ['n', 'mergeTime', 'quickTime', 'heatTime']
    with open('testInsert.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(row)
    csvFile.close()

    for n in range(nStart, nmax, gap):

        mergeTimes = np.arange(pmedia, dtype='f')
        heapTimes = np.arange(pmedia, dtype='f')
        quickTimes = np.arange(pmedia, dtype='f')

        for y in range(pmedia):
            B = np.arange(n)
            np.random.shuffle(B)
            A = sorts.heapArray(B)
            C = B.copy()

            startMerge = timer()
            sorts.mergesort(B, 0, n - 1)  # passare lunghezza - 1
            endMerge = timer()
            mergeTimes[y] = endMerge - startMerge

            startQuick = timer()
            sorts.quicksort(C, 0, n - 1)
            endQuick = timer()
            quickTimes[y] = endQuick - startQuick

            startHeap = timer()
            sorts.heapsort(A)
            endHeap = timer()
            heapTimes[y] = endHeap - startHeap

        mergeTime = np.mean(mergeTimes)
        quickTime = np.mean(quickTimes)
        heapTime = np.mean(heapTimes)

        dataCsv = [n, mergeTime, quickTime, heapTime]
        with open('testInsert.csv', 'a') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(dataCsv)
        csvFile.close()

    data = np.loadtxt('testInsert.csv', delimiter=",", skiprows=1, usecols=[0, 1, 2, 3])

    f = plt.figure(1)
    f.set_figheight(10)
    f.set_figwidth(10)
    plt.subplot(111)
    plt.plot(data[:, 0], data[:, 1], label='mergeTime')
    plt.plot(data[:, 0], data[:, 2], label='quickTime')
    plt.plot(data[:, 0], data[:, 3], label='heapTime')
    plt.xlabel('n')
    plt.ylabel('time(s)')
    plt.title("sort algorithms")
    plt.legend()

    plt.show()
