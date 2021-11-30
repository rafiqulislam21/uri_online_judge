endNum = int(input())
oddCounter = 0

while True:
    if oddCounter >= 6:
        break
    else:
        if endNum%2 == 1:
            oddCounter += 1
            print(endNum)
        endNum += 1