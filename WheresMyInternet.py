#union find problem
n, m  = map(int, input().split())
par = [i for i in range(n)]
rank = [1] * n
def find(n1):
    p = n1
    while p != par[p]:
        par[p] = par[par[p]]
        p = par[p]
    return p

def union(n1,n2):
    p1, p2 = find(n1), find(n2)

    #same parent
    if p1 == p2:
        return False

    #different
    if rank[p2] > rank[p1]:
        par[p1] = p2
        rank[p2] += rank[p1]
    else:
        par[p2] = p1
        rank[p1] += rank[p2]
    return True
for _ in range(m):
    n1, n2 = map(lambda x: int(x)-1, input().split())
    union(n1,n2)

p1 = find(0)
res = [x for x in range(n) if find(x) != p1]
if len(res) == 0:
    print('Connected')
else:
    for i in res:
        print(i+1)