n = int(input())

if 5 < n < 2000:
    for index in range(1, n+1):
        if index%2 == 0:
            print("{}^2 = {}".format(index, pow(index, 2)))
