a, b, c = map(float, input().split())
numList = [a,b,c]
numList.sort(reverse=True)
a = numList[0]
b = numList[1]
c = numList[2]
a2 = a*a
b2 = b*b
c2 = c*c

if a >= (b+c):
    print("NAO FORMA TRIANGULO")
elif a2 == (b2+c2):
    print("TRIANGULO RETANGULO")
elif a2 > (b2+c2):
    print("TRIANGULO OBTUSANGULO")
elif a2 < (b2+c2):
    print("TRIANGULO ACUTANGULO")
if a==b==c:
    print("TRIANGULO EQUILATERO")
elif a==b or b==c or c==a:
    print("TRIANGULO ISOSCELES")
