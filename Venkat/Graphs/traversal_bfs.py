from collections import deque
## Adjacency List representation of Graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

def bfs(graph, start):
    queue = deque()
    visited = set()
    res = []
    queue.append(start)
    visited.add(start)
    while queue:
        cur_element = queue.popleft()
        res.append(cur_element)
        for neigh in graph[cur_element]:
            if neigh not in visited:
                queue.append(neigh)
                visited.add(neigh)
    return res

print(bfs(graph, 'A'))