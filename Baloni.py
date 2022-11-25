#greedy
from collections import defaultdict
n = int(input())
dic = defaultdict(int)
count = 0
for x in map(int, input().split()):
    #x+1 exist
    if dic[x+1] > 0:
        dic[x+1] -= 1
    #x+1 not exist
    else:
        count += 1
    #save this arrow
    dic[x] += 1

print(count)