nums = []
totalEven = 0

for index in range(5):
    nums.append(float(input()))
    if nums[index]%2 == 0:
        totalEven += 1

print("{} valores pares".format(totalEven))