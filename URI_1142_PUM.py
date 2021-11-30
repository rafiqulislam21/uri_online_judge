n = int(input())
track_last = 1
for index in range(1,n+1):
    for i in range(track_last, track_last+3):
        track_last = i+2
        print("{} ".format(i), end="")
    print("PUM")