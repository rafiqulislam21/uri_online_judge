arr_size = 100
arr = [None] * arr_size
t = float(input())
half = round(t,4)
for i in range(arr_size):
    arr[i] = half
    half /= 2

for index in range(arr_size):
    print("N[{}] = {:.4f}".format(index, arr[index]))