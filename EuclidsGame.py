#game theory DP
while True:
    a, b = map(int, input().split())
    if a==0:
        break
    x, y = max(a,b), min(a,b)
    #flag 0 means Stan wins, 1 means Ollie wins
    flag = 0
    while x != y:
        #x//y >1 means Stan/Ollie at this stemp (x'+ky, y)can control to reach ...
        #(x'+y,y) or (x',y), which is opposite result
        if (x//y) > 1:
            break
        x = x % y
        x, y = y, x
        #change flag
        flag = 1 - flag
        
    if flag:
        print('Ollie wins')
    else:
        print('Stan wins')