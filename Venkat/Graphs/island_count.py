grid = [
    [0,1,0,0,0],
    [0,1,0,0,0],
    [0,0,0,1,0],
    [0,0,1,1,0],
    [1,0,0,1,1],
    [1,1,0,0,0]
]

from collections import deque

def bfs(grid:list[list], visited:set, r:int, c:int, directions):
    queue = deque([(r,c)])
    visited.add((r,c))
    while queue:
        cr, cc = queue.popleft()
        if grid[cr][cc] == 1:
            for r_dir ,c_dir in directions:
                nr = cr+r_dir
                nc = cc+c_dir
                if 0 <= nr <= len(grid)-1 and 0 <= nc <= len(grid[0]) - 1 and grid[nr][nc] == 1 and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc))

def island_count(grid:list[list], visited:set):
    if not grid:
        return 0
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    directions = [(0,-1), (0,1), (1,0), (-1,0)]
    for R in range(rows):
        for C in range(cols):
            if grid[R][C] == 1 and (R, C) not in visited:
                bfs(grid, visited, R, C, directions)
                count += 1
    return count

visited = set()
print(island_count(grid=grid, visited=visited))