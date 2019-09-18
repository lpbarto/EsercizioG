
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
    return i // 2
def left(i):
    return 2 * i
def right(i):
    return 2 * i + 1

def maxHeapify(A, i):
    l = left(i)
    r = right(i)
    if l <= A.size() and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r <= A.size() and A[r] > A[largest]:
        largest = r
    if largest != i:
        swap(A, i, largest)
        maxHeapify(A, largest)

def buildMaxHeap(A):
