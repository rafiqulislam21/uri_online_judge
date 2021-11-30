maxNum = 0
maxIndex = 1

for index in range(1, 100+1):
    num = int(input())
    if maxNum < num:
            maxNum = num
            maxIndex = index

print(maxNum)
print(maxIndex)