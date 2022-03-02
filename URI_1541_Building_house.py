while(True):
    ABC = [int(item) for item in input().split()]
    if len(ABC) == 1 and ABC[0]==0:
        break;
    else:
        A,B,C = map(int, ABC)
        area = A * B
        area_pct = area *100 / C
        
        result = area_pct ** 0.5
        print(int(result))