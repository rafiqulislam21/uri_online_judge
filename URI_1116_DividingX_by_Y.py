n = int(input())
value_list = []

for i in range(n):
    x_y = list(map(int, input().split()))
    value_list.append(x_y)
    
for item in value_list:
    x,y = item
    try:
      result = x/y
      print("{}".format(result))
    except:
      print("divisao impossivel")

