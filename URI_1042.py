x,y,z = list(map(int,input().split()))
nums = [x,y,z]
sortedNums = []
for item in nums:
    sortedNums.append(item)
    
sortedNums.sort()

for item in sortedNums:
    print("{}".format(item))
    
print("")

for item in nums:
    print("{}".format(item))

