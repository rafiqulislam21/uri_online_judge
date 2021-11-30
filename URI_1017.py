spendTime = int(input())
averageSpeed = int(input())

distance = spendTime*averageSpeed
fuelNeed = format(distance/12, ".3f")

print(fuelNeed)