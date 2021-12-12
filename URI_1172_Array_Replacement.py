arr = [None] * 10

for i in range(10):
    n = int(input())
    if n < 1:
        arr[i] = 1
    else:
        arr[i] = n

for index in range(10):
    print("X[{}] = {}".format(index, arr[index]))