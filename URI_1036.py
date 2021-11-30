import math

A,B,C = map(float,input().split())
D = (B**2)-(4*A*C)
if(D <0 or A==0):
    print("Impossivel calcular")
else:
    D=math.sqrt(D)
    R1 = (-B+D)/(2*A)
    R2 = (-B-D)/(2*A)
    R1 = round(R1, 5)
    R2 = round(R2, 5)
    print('R1 = {}\nR2 = {}'.format(R1, R2))