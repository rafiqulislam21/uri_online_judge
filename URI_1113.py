list_res = []
while True:
    x,y = list(map(int, input().split()))
    if(x==y):
        break
    else:
        if x > y:
            list_res.append("Decrescente")
        else:
            list_res.append("Crescente")
                
    
for item in list_res:
    print(item)