N = int(input())

if 1 <= N <= 100: 
    for i in range(N):
        n = int(input())
        isPrime = True
        if 1 < n <= pow(10,7):
            for item in range(2, n):
                if n%item == 0:
                    isPrime = False
        if isPrime:
            print("{} eh primo".format(n))
        else:
            print("{} nao eh primo".format(n))