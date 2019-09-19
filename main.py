from pyfirmata import Arduino, util
import sorts
import numpy as np
from timeit import default_timer as timer
import sys
sys.setrecursionlimit(100000)

def main():
   # board = Arduino("/dev/cu.usbmodem14301")

    n = 100
    B = np.arange(n)
    np.random.shuffle(B)
    A = sorts.heapArray(B)
    C = B.copy()
    print(A)
    startMerge = timer()
    sorts.mergesort(B, 0, n - 1) #passare lunghezza - 1
    endMerge = timer()
    print(B)
    print(endMerge - startMerge)
    startQuick = timer()
    sorts.quicksort(C, 0, n-1)
    endQuick = timer()
    print(B)
    print(endQuick - startQuick)
    startHeap = timer()
    sorts.heapsort(A)
    endHeap = timer()
    print(A)
    print(endHeap - startHeap)


if __name__ == "__main__":
    main()