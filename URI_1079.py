n = int(input())

for index in range(n):
    n1, n2, n3 = map(float, input().split())
    sumNums = (n1*2) + (n2*3) + (n3*5)

    avg = sumNums/(10)
    
    print("{:.1f}".format(avg))