fact_sum = 1
N = int(input())

if 0 < N < 13:
    for i in range(1, N+1):
        fact_sum *= i        
    print("{} ".format(fact_sum))