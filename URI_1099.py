N = int(input())
sum_list = []
for i in range(N):
    x,y = list(map(int, input().split()))
    if x > y: 
        x , y = y , x
        
    sum_single = 0
    for j in range(x+1,y):
        if j%2==1:
            sum_single += j
    sum_list.append(sum_single)
    
    
for index in range(N):
    print(sum_list[index])