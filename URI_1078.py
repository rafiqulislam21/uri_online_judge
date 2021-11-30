n = int(input())

if 2 < n < 1000:
    for index in range(1, 10+1):
            print("{} x {} = {}".format(index, n, index*n))
        