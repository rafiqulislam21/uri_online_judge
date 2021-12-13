arr_size = 20
arr = [None] * arr_size

for i in range(arr_size):
    n = int(input())
    arr[i] = n

arr.reverse()
for index in range(arr_size):
    print("N[{}] = {}".format(index, arr[index]))