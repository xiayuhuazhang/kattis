#bfs record moves
from collections import deque
dim = int(input())
grid = []

xx = [-2, -2, -1, -1, 1, 1, 2, 2]
yy = [1, -1, 2, -2, -2, 2, 1, -1]

def bfs(start, end, grid, dim):
    queue = deque()
    visit = set()
    queue.append((start,0))
    visit.add(start)
    
    while queue:
        cur, move = queue.popleft()
        if cur == end:
            return move
        x, y = cur    
        for dx, dy in zip(xx,yy):
            if x+dx in range(0,dim) and y+dy in range(0,dim) and (x+dx,y+dy) not in visit and grid[x+dx][y+dy] != '#':
                queue.append(((x+dx,y+dy), move+1))
                visit.add((x+dx,y+dy))
    return -1

for x in range(dim):
    grid.append(input())
    y = grid[-1].find('K')
    #find K
    if y != -1:
        start = (x,y)
        
print(bfs(start,(0,0), grid, dim))