list_fib = []

N = int(input())

if 0 < N < 46:
    for i in range(N):
        if i == 0 or i == 1:
            list_fib.append(i)
        else:
            list_fib.append(list_fib[i-1]+list_fib[i-2])
    
    fib_str = ' '.join(list(map(str, list_fib)))
    print(fib_str)
    