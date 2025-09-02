edges = [
    ['i', 'j'],
    ['k', 'i'],
    ['m', 'k'],
    ['k', 'l'],
    ['o', 'n']
]

from collections import defaultdict

graph = defaultdict(list)
for (i,j) in edges:
    graph[i].append(j)
    graph[j].append(i)

def has_path_dfs(graph:dict, start, end):
    if start == end:
        return True
    visited = set()
    stack = []
    stack.append(start)
    visited.add(start)
    while stack:
        node = stack.pop()
        if node == end:
            return True
        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append(neighbor)
                visited.add(neighbor)
    return False
    

print(has_path_dfs(graph, 'i', 'k'))
print(has_path_dfs(graph, 'i', 'l'))
print(has_path_dfs(graph, 'i', '0'))
    
    