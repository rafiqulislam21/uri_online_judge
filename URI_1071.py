startNum = int(input())
endNum = int(input())

oddSum = 0

if startNum > endNum:
    temp = startNum
    startNum = endNum
    endNum = temp

for index in range(startNum+1, endNum):
    if index%2 == 1:
        oddSum += index

print(oddSum)