x,y = list(map(int, input().split()))

if x < y:
    if 1 < x < 20 and x < y < 100000:
        counter = 0
        for i in range(1,y+1):
            counter += 1
            if(counter%x==0):
                print("{}".format(i))
            else:
                print("{} ".format(i), end="")