inter = 0
gremio = 0
empates = 0
grenais = 0
response = 1

while response != 2:
    
    if response == 1:
        inter_goal, gremio_goal = list(map(int, input().split()))
        if inter_goal > gremio_goal:
            inter += 1
            grenais +=1
        elif inter_goal < gremio_goal:
            gremio += 1
            grenais +=1
        elif inter_goal == gremio_goal:
            empates +=1
    print("Novo grenal (1-sim 2-nao)")
    response = int(input())
            
print("{} grenais".format(grenais))
print("Inter:{}".format(inter))
print("Gremio:{}".format(gremio))
print("Empates:{}".format(empates))
if inter == gremio:
    print("Não houve vencedor")
elif inter > gremio:
    print("Inter venceu mais")
elif inter < gremio:
    print("Germio venceu mais")