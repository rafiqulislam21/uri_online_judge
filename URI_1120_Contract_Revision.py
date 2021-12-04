while(True):
    D, N = list(map(int, input().split()))
    if D == 0:
        break
    if 1 <= D <=9 and 1 <= N < pow(10,100):
        d_str = str(D)
        n_str = str(N)
        new_n = n_str.replace(d_str,"")
        
        if new_n == "":
            new_n = "0"
            
        print(int(new_n))