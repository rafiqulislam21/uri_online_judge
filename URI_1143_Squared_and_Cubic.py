n = int(input())
if 0 < n <1000:
    for index in range(1,n+1):
        print("{} {} {}".format(index,index*index, index*index*index))