from datetime import timedelta

startHr, startMin, endHr, endMin = map(int, input().split())

startTime = timedelta(hours=startHr, minutes=startMin)
endTime = timedelta(hours=endHr, minutes=endMin)

result = endTime - startTime

totalSeconds = result.seconds

hours = totalSeconds//3600
minutes = (totalSeconds//60)%60

if result.seconds == 0:
    hours = 24
    
print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(hours, minutes))