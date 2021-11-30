def productCode(code):
    if code == 1:
        return 4
    elif code == 2: 
        return 4.50
    elif code == 3: 
        return 5
    elif code == 4: 
        return 2
    elif code == 5: 
        return 1.50
        
        
x,y = map(int,input().split())
singleCost = productCode(x)
cost = singleCost * y
cost = "{:.2f}".format(cost)
print("Total: R$ {}".format(cost))

