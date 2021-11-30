num1 = int(input())
num2 = int(input())
sum = 0
if num1 > num2:
    num1, num2 = num2, num1

for item in range(num1, num2+1):
    if item % 13:
        sum += item
        
print(sum)
