import tests
from timeit import default_timer as timer
def main():


    nStart = 10000
    nmax = 100000
    gap = 1000
    startTime = timer()
    tests.test(nStart, nmax, gap)
    stopTime = timer()
    print(stopTime - startTime)



if __name__ == "__main__":
    main()