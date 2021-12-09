n=int(input())
for i in range(n):
    x,y=list(map(int,input().split()))
    if(x%2==1):
        odd_sum=0
        for index in range(1,y+1):
            odd_sum += x
            x += 2
        print(odd_sum)
    else:
        x+=1
        odd_sum=0
        for index in range(1,y+1):
            odd_sum += x
            x += 2
        print(odd_sum)