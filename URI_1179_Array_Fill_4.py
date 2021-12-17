arr_size = 15
arr = [None] * arr_size
par = [None] * 5
impar = [None] * 5

par_count = 0
impar_count = 0
for i in range(arr_size):
    n = int(input())
    arr[i] = n
            
for i in range(arr_size):
    if arr[i]%2==0:
        if par_count < 5:
            par[par_count] = arr[i]
            par_count += 1
        else:
            for index in range(5):
                print("par[{}] = {}".format(index, par[index]))
            par_count = 0
            par[par_count] = arr[i]
            par_count += 1
    elif arr[i]%2 == 1:
        if impar_count < 5:
            impar[impar_count] = arr[i]
            impar_count += 1
        else:
            for index in range(5):
                print("impar[{}] = {}".format(index, impar[index]))
            impar_count = 0
            impar[impar_count] = arr[i]
            impar_count += 1
            
for index in range(impar_count):
    print("impar[{}] = {}".format(index, impar[index]))     
for index in range(par_count):
    print("par[{}] = {}".format(index, par[index]))