product1 = list(map(float, input().split()))
product2 = list(map(float, input().split()))

totalCost = (product1[1]*product1[2])+(product2[1]*product2[2])
print("VALOR A PAGAR: R$ %0.2f" %totalCost)