from collections import deque

#Adjacency list
graph = {
    'f': ['g', 'i'],
    'g': ['h'],
    'h': [],
    'i': ['g', 'h'],
    'j': ['i'],
    'k': []
}

def has_path_bfs(graph, start, end) -> bool:
    queue = deque()
    visited = set()
    queue.append(start)
    visited.add(start)
    while queue:
        node = queue.popleft()
        if node == end:
            return True
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
    return False

def has_path_dfs(graph, start, end) ->bool:
    stack = []
    visited = set()
    stack.append(start)
    while stack:
        node = stack.pop()
        if node == end:
            return True
        if node in visited:
            continue
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append(neighbor)
    return False



print(has_path_bfs(graph, 'f', 'k'))
print(has_path_bfs(graph, 'f', 'h'))
print(has_path_bfs(graph, 'j', 'h'))

print(has_path_dfs(graph, 'f', 'k'))
print(has_path_dfs(graph, 'f', 'h'))
print(has_path_dfs(graph, 'j', 'h'))