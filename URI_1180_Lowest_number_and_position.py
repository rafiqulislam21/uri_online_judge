N = int(input())
smallest_index = 0   
if 1 <= N <= 1000:
    X = list(map(int, input().split()))
    
    for index in range(N):
        if X[index] < X[smallest_index]:
            smallest_index = index
                
    print("Menor valor: {}".format(X[smallest_index]))
    print("Posicao: {}".format(smallest_index))
        