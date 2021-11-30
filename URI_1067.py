endNum = int(input())

if 1 <= endNum <= 1000:
    for index in range(1,endNum+1):
        if index%2 == 1:
            print(index)
