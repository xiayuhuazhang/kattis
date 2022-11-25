ls = input().split()
if len(ls) == 1:
    print(2**(int(ls[0])+1)-1)
else:    
    h = int(ls[0])
    res = 0
    for s in ls[1]:
        if s=='L':
            res = 2*res+1
        else:
            res = 2*res+2
    print(2**(int(ls[0])+1)-1 - res)