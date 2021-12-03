list_input = list(map(int, input().split()))
n1 = 'first'
n2 = 0
sumVal = 0
for i in list_input:
    if (n1 == 'first'):
        n1 = i
    else:
        if (i > 0):
            n2 = i
            break

for i in range(n2):
    sumVal += n1
    n1 += 1

print("{}".format(sumVal))