n = int(input())
ls = [int(x) for x in input().split()]
ls.sort()
res = [0] * n
res[::2] = ls[n//2:]
res[1::2] = ls[n//2-1::-1] 
print(' '.join([str(x) for x in res]))