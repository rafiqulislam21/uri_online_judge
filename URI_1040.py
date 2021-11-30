n1, n2, n3, n4 = map(float, input().split())
n1 = round(n1,1)
n2 = round(n2,1)
n3 = round(n3,1)
n4 = round(n4,1)

withWeightSum = (n1*2)+(n2*3)+(n3*4)+(n4*1)
weightSum = 2+3+4+1
average = withWeightSum/weightSum

print("Media: {}".format(round(average,1)))

if average >= 7:
    print("Aluno aprovado.")
elif average < 5:
    print("Aluno reprovado.")
elif average >= 5 and average <=6.9:
    print("Aluno em exame.")
    n5 = float(input())
    newAverage = (average + n5)/2
    print("Nota do exame: {}".format(n5))
    if newAverage >= 5:
        print("Aluno aprovado.")
    elif newAverage <= 4.9:
        print("Aluno reprovado.")
    print("Media final: {}".format(newAverage))