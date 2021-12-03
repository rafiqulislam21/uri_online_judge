
while(True):
    num = int(input())
    result = ""
    if num == 0:
        break
    for i in range(1,num+1):
        result += str(i)+" "
    print(result[:-1])