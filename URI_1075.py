n = int(input())

if n < 10000:
    for index in range(1, 10000+1):
        if index%n == 2:
            print(index)
        