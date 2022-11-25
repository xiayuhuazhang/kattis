from collections import defaultdict, deque

def split(n, nodes, edges):
    #two groups
    group = [set(), set()]
    stack = deque()
    for node in nodes:
        if any(node in s for s in group):
            continue
        #different trees in forest
        stack.append((len(group[0]) > len(group[1]) , node))
        #tree triverse
        while stack:
            i,w = stack.pop()
            if w in group[not i]:
                print('impossible')
                return
            if w in group[i]:
                continue
            group[i].add(w)
            
            for z in edges[w]:
                stack.append((not i, z))
    
    for s in group:
        #* for unzip the element in set
        print(*(u for u in s))
        
n = int(input())
nodes = [input() for _ in range(n)]
e = int(input())
edges = defaultdict(set)
for _ in range(e):
    u1, u2 = input().split()
    edges[u1].add(u2)
    edges[u2].add(u1)
split(n, nodes, edges)