nums = []
positiveVal = 0
positiveSum = 0

for index in range(6):
    nums.append(float(input()))
    if nums[index] > 0:
        positiveVal += 1
        positiveSum += nums[index]

print("{} valores positivos".format(positiveVal))
print("{:.1f}".format(positiveSum/positiveVal))