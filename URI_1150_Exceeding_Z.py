x = int(input())
z = int(input())
while(True):
    if z > x:
        sum_val = 0
        counter_val = 1
        for i in range(x, z+1):
            sum_val += i
            if sum_val <= z:
                counter_val += 1
            else:
                break
        print(counter_val)
        break
    else:
        z = int(input())