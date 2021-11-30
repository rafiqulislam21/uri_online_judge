num1 = int(input())
num2 = int(input())

if num1 > num2:
    num1, num2 = num2, num1

for item in range(num1+1, num2):
    if item % 5 == 2 or item % 5 == 3:
        print(item)
