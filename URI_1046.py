start, end = map(int, input().split())
if start < end:
    result = abs(start-end)
else:
    result = 24 - abs(start-end)
print("O JOGO DUROU {} HORA(S)".format(result))