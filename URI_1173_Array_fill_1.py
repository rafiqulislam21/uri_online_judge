arr = [None] * 10
n = int(input())
for i in range(10):
    if n < 50:
        if i == 0:
            arr[i] = n
        else:
            arr[i] = arr[i-1]*2

for index in range(10):
    print("N[{}] = {}".format(index, arr[index]))