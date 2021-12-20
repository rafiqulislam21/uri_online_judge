arr_size = 12
T = input()
M=[]

for i in range(arr_size):
    for j in range(arr_size):
        x = float(input())
        if j < i:
            M.append(x)
        
sum = 0
for i in M:
    sum = sum + i
        
if T == 'S':
    print("{:.1f}".format(sum))
elif T == 'M':
    median= sum/len(M)
    print("{:.1f}".format(median))