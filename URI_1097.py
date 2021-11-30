i = 1
j_start = 7
j_end = j_start - 3
for index in range(5):
    for j in range(j_start, j_end, -1):
        print("I={} J={}".format(i, j))

    i += 2
    j_start += 2
    j_end = j_start - 3
