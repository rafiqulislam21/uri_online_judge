i = 1
for index in range(5):
    counter = 0
    for j in range(7, 4, -1):
        counter += 1
        print("I={} J={}".format(i,j))
        if counter==3:
            i += 2