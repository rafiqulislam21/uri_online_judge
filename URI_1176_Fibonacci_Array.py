
def fib(n):
    list_fib = []
    for i in range(n+1):
        if i == 0 or i == 1:
            list_fib.append(i)
        else:
            list_fib.append(list_fib[i-1]+list_fib[i-2])
    return list_fib

t = int(input())
for i in range(t):
    n = int(input())
    if 0 <= n <= 60:
        fib_items = fib(n)
        print("Fib({}) = {}".format(n, fib_items[-1]))
    