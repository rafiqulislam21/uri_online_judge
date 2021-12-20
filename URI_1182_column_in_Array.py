L = int(input())
T = input()
M=[]
for i in range(12):
    M.append([])

for i in range(12):
    for j in range(12):
        x = float(input())
        M[j].append(x)
        
sum = 0
for i in M[L]:
    sum = sum + i
        
if T == 'S':
    print("{:.1f}".format(sum))
elif T == 'M':
    median= sum/12
    print("{:.1f}".format(median))