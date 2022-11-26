# simple math problem
import math
a, b, n = map(int, input().split())
res = []
for i in range(n):
    x, y, r = map(int, input().split())
    #compute the distance and minus the r
    d = math.sqrt((a - x)**2 + (b - y)**2) - r
    res.append(d)
res.sort()
# if res[2]<0 means two already in the range
print(int(res[2]) if int(res[2]) >= 0 else 0)