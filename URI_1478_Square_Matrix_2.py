while True:
    N = int(input())

    if (N == 0):
        break

    res =  []

    for i in range(1,(N+1)):
        tmp = []
        count = i
        for j in range(N):
            tmp.append(abs(count))
            if(count == 1):
                count -= 3
            else:
                count -= 1
        res.append(tmp)

    for i in range(N):
        tx = ''
        for j in range(N):
            tx += " %3d" %res[i][j]
        print(tx[1:])
    print("")