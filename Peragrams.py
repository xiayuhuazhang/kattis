from collections import Counter
s = input()
dic = Counter(s)
res = 0
for k,v in dic.items():
    if v%2:
        res += 1
if res ==0:
    print(0)
else:
    print(res-1)