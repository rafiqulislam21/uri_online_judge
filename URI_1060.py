nums = []
positiveVal = 0

for index in range(6):
    nums.append(float(input()))
    if nums[index] > 0:
        positiveVal += 1

print("{} valores positivos".format(positiveVal))