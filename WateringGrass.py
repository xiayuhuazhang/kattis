#greedy and geometry
from math import sqrt
try:
    while True:
        n, l ,w = map(int, input().split())
        ls = []
        for _ in range(n):
            cen, r = map(int, input().split())
            #filter small sprinkkers
            if 2*r > w:
                dx = sqrt(r**2 - (w/2)**2)
                ls.append([cen-dx, cen+dx])
        ls.sort()
        nn = len(ls)
        
        #interval cover
        count = 0
        left, i = 0, 0 
        while True:
            further = -1
            while i < nn and ls[i][0] <= left:
                further = max(further, ls[i][1])
                i += 1
            # no overlap
            if further == -1:
                count = -1
                break
            count += 1
            #renew left
            left = further
            if left >= l:
                break
        print(count)
except EOFError:
    pass