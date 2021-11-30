nums = []
totalEven = 0
totalOdd = 0
totalPositive = 0
totalNegative = 0

for index in range(5):
    nums.append(float(input()))
    if nums[index]%2 == 0:
        totalEven += 1
    else: 
        totalOdd += 1
    
    if nums[index] > 0:
        totalPositive += 1
    elif nums[index] < 0: 
        totalNegative += 1

print("{} valor(es) par(es)".format(totalEven))
print("{} valor(es) impar(es)".format(totalOdd))
print("{} valor(es) positivo(s)".format(totalPositive))
print("{} valor(es) negativo(s)".format(totalNegative))