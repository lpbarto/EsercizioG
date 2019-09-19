import numpy as np

def merge(A, p, q, r):
    n = q - p + 1
    m = r - q
    L = [0] * n
    R = [0] * m
    for i in range(0, n):
        L[i] = A[p + i]
    for j in range(0, m):
        R[j] = A[q + j + 1]

    i = 0
    j = 0
    k = p
    while i < n and j < m:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
    while i < n:
        A[k] = L[i]
        i += 1
        k += 1
    while j < m:
        A[k] = R[j]
        j += 1
        k += 1


def mergesort(A, p, r):
    if p < r:
        q = (p + (r - 1)) // 2
        mergesort(A, p, q)
        mergesort(A, q+1, r)
        merge(A, p, q, r)

def swap(A, a, b):
    temp = A[a]
    A[a] = A[b]
    A[b] = temp

def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            swap(A, i, j)
    swap(A, i + 1, r)
    return i + 1

def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)

def parent(i):
    return (i + 1) // 2
def left(i):
    return 2 * i + 1
def right(i):
    return 2 * i + 2

def maxHeapify(A, i):
    l = left(i)
    r = right(i)
    if l < A.heapLength and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r < A.heapLength and A[r] > A[largest]:
        largest = r
    if largest != i:
        swap(A, i, largest)
        maxHeapify(A, largest)

def buildMaxHeap(A):
    A.heapLength = len(A)
    for i in range((len(A) - 1) // 2, - 1, - 1):
        maxHeapify(A, i)

def heapsort(A):
    buildMaxHeap(A)
    for i in range(A.heapLength - 1, 0, -1):
        swap(A, 0, i)
        A.heapLength = A.heapLength - 1
        maxHeapify(A, 0)

class heapArray(np.ndarray):

    def __new__(cls, input_array, heapLength=None):
        # Input array is an already formed ndarray instance
        # We first cast to be our class type
        obj = np.asarray(input_array).view(cls)
        # add the new attribute to the created instance
        obj.heapLength = heapLength
        # Finally, we must return the newly created object:
        return obj

    def __array_finalize__(self, obj):
        # see InfoArray.__array_finalize__ for comments
        if obj is None: return
        self.heapLength = getattr(obj, 'info', None)



