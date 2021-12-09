s = 1
down_val = 2
for i in range(3, 39+1, 2):
    # print("{}/{}+".format(i,down_val), end="")
    s += i/(down_val)
    down_val *= 2
print("{:.2f}".format(s))