from pyfirmata import Arduino, util
import sorts
import numpy as np
from timeit import default_timer as timer
import sys
sys.setrecursionlimit(100000)

def main():
   # board = Arduino("/dev/cu.usbmodem14301")

    n = 15000

    A = np.arange(n)
    np.random.shuffle(A)
    B = A.copy()
    print(A)
    startMerge = timer()
    sorts.mergesort(A, 0, n-1)
    endMerge = timer()
    print(A)
    print(endMerge - startMerge)
    startQuick = timer()
    sorts.quicksort(B, 0, n-1)
    endQuick = timer()
    print(B)
    print(endQuick - startQuick)

if __name__ == "__main__":
    main()