#graph , in degree and neighbours
from collections import defaultdict, deque
n, m = map(int, input().split())
#degree and neibours
deg = defaultdict(int)
nei = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    deg[b] += 1
    nei[a].append(b)
#bfs

queue = deque()
for i in range(1,n+1):
    # no pre-condition enqueue
    if deg[i] == 0:
        queue.append(i)
res = []
while queue:
    x = queue.popleft()
    res.append(x)
    for j in nei[x]:
        deg[j] -=1
        if deg[j] == 0:
            queue.append(j)

if len(res) == n:
    for i in res:
        print(i)
else:
    print('IMPOSSIBLE')