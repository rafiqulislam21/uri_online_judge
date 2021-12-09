
while(True):
    x=int(input())
    if x == 0:
        break
    
    if(x%2==0):
        even_sum=0
        for index in range(1,5+1):
            even_sum += x
            x += 2
        print(even_sum)
    else:
        x+=1
        even_sum=0
        for index in range(1,5+1):
            even_sum += x
            x += 2
        print(even_sum)