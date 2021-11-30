item_list = []
while True:
    track_min_max = {
        'min': 0,
        'max': 0,
    }
    x,y = list(map(int, input().split()))
    if x <= 0 or y <= 0:
        break
    else:
        if x > y: 
            x , y = y , x
    
        track_min_max['min'] = x
        track_min_max['max'] = y
        item_list.append(track_min_max)
        
    
for item in item_list:
    sum_single = 0
    for index in range(item['min'], item['max']+1):
        sum_single += index
        print("{} ".format(index), end="")
        
    print("Sum={}".format(sum_single))