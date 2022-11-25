# bfs classic question
from sys import stdin
from collections import deque

def bfs(r,c):
    q = deque()
    visit.add((r,c))
    q.append((r,c))
    while q:
        row, col = q.popleft()
        dir = [(1,0), (-1,0), (0,-1), (0,1)]
        for dr, dc in dir:
            r, c = row + dr, col + dc
            if r in range(rows) and \
            c in range(cols) and \
            (r,c) not in visit and \
            grid[r][c] =="-":
                q.append((r,c))
                visit.add((r,c))

# input process                
lines = stdin.readlines()
i = 0
t = 1
while i < len(lines):
    grid = []
    line = [int(x) for x in lines[i].split()]
    rows, cols = line[0], line[1]
    
    for j in range(1, rows + 1):
        grid.append([x for x in lines[i+j].strip()])
    #renew to next case
    i += rows + 1
    #main func
    count = 0
    visit = set()
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "-" and (r,c) not in visit:
                bfs(r,c)
                count += 1
    print("Case {}: {}".format(t, count))
    t += 1