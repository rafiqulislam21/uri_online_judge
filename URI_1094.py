N = int(input())

total = 0
c=0
r=0
s=0
for index in range(N):
    
    animals, animalType = map(str, input().split())
    animals = int(animals)
    
    if 1 <= animals <= 15:
        if animalType == "C":
            c += animals
        elif animalType == "R":
            r += animals
        elif animalType =="S":
            s += animals
    
total = c+r+s
cPercent = (c/total)*100
rPercent = (r/total)*100
sPercent = (s/total)*100
    
print("Total: {} cobaias".format(total))
print("Total de coelhos: {}".format(c))
print("Total de ratos: {}".format(r))
print("Total de sapos: {}".format(s))
print("Percentual de coelhos: {} %".format("{:.2f}".format(cPercent)))
print("Percentual de ratos: {} %".format("{:.2f}".format(rPercent)))
print("Percentual de sapos: {} %".format("{:.2f}".format(sPercent)))