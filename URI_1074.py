n = int(input())

if n < 10000:
    for index in range(n):
        x = int(input())
        if pow(-10,7) < x < pow(10,7):
            if x == 0:
                print("NULL")
            elif x < 0 and x%2 == 0:
                print("EVEN NEGATIVE")
            elif x > 0 and x%2 == 0:
                print("EVEN POSITIVE")
            elif x < 0 and x%2 == 1:
                print("ODD NEGATIVE")
            elif x > 0 and x%2 == 1:
                print("ODD POSITIVE")