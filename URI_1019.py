N = int(input())

hour = int(N/3600)
minute = int(((N/60) - (hour*60)))
second = int(N - ((minute*60)+(hour*3600)))

print("{}:{}:{}".format(hour,minute,second))

