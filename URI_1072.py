n = int(input())
numList = []
inCounter = 0
outCounter = 0

if n < 10000:
    for index in range(n):
        x = int(input())
        if pow(-10,7) < x < pow(10,7):
            numList.append(x)
            if 10 <= numList[index] <= 20:
                inCounter += 1
            else:
                outCounter += 1

print("{} in".format(inCounter))
print("{} out".format(outCounter))