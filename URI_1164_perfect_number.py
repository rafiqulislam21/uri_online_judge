N = int(input())

if 1 <= N <= 100: 
    for i in range(N):
        n = int(input())
        div_sum = 0
        if 1 < n <= pow(10,8):
            for item in range(1, n):
                if n%item == 0:
                    div_sum += item

        if div_sum == n:
            print("{} eh perfeito".format(n))
        else:
            print("{} nao eh perfeito".format(n))