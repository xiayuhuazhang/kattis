#tried heap and get TLE in huge cases
#B is superlarge than N so cannot iterate B in any cases
while True:
    n, b =  list(map(int,input().split()))
    if n == -1:
        break
    a = []
    lo, hi = 1, 0
    for i in range(n):
        x = int(input())
        hi = max(hi,x)
        a.append(x)
    #deal with the space
    space = input()
    
    #ans range from 1 to max(x)
    #binary search
    while lo <= hi:
        mi = (lo+hi)//2
        c = 0
        for i in range(n):
            c += (a[i]+ mi - 1)//mi
        if c > b:
            lo = mi +1
        else:
            hi = mi-1
    print(lo)