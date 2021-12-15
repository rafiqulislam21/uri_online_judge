arr_size = 1000
arr = [None] * arr_size
t = int(input())
if 2 <= t <= 50:
    counter = 0
    for i in range(arr_size):
        if counter >= t:
            counter = 0
           
        arr[i] = counter
        counter += 1

for index in range(arr_size):
    print("N[{}] = {}".format(index, arr[index]))