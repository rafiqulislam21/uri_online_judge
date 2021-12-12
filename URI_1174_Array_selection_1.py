arr_size = 100
arr = [None] * arr_size

for i in range(arr_size):
    n = float(input())
    arr[i] = n

for index in range(arr_size):
    if arr[index] <= 10:
        print("A[{}] = {}".format(index, arr[index]))