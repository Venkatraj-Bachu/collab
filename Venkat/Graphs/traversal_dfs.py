## Adjacency List representation of Graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

def dfs(graph, start) -> list:
    stack = []
    res = []
    visited = set()
    stack.append(start)
    while stack:
        cur_element = stack.pop()
        if cur_element in visited:
            continue
        visited.add(cur_element)
        res.append(cur_element)
        for neigh in graph[cur_element]:
            if neigh not in visited:
                stack.append(neigh)
    return res

print(dfs(graph, 'A'))