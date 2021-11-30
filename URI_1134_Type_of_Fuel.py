#1. Alcohol 2. Gasoline 3. Diesel 4. End
key = 0
alcohol=0
gasoline=0
diesel=0
while key != 4:
    key = int(input())
    if key == 1:
        alcohol += 1
    elif key == 2:
        gasoline += 1
    elif key == 3:
        diesel += 1
        
print("MUITO OBRIGADO")
print("Alcool: {}".format(alcohol))
print("Gasolina: {}".format(gasoline))
print("Diesel: {}".format(diesel))