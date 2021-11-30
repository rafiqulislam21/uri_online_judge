n = int(input())
if 0 < n <1000:
    for i in range(1,n+1):
        num2 = i*i
        num3= i*i*i
        print("{} {} {}".format(i,num2,num3))
        num22=num2+1
        num33=num3+1
        print("{} {} {}".format(i,num22,num33))