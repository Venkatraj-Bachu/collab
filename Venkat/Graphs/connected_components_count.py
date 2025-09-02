graph = {
    1: [2],
    2: [1],
    3: [],
    4: [6],
    5: [6],
    6: [4,5,7,8],
    7: [6],
    8: [6],
}


from collections import deque
def bfs(node, graph, visited):
    queue = deque([node])
    visited.add(node)
    while queue:
        cur_node = queue.popleft()
        for neighbor in graph[cur_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

def recursive_dfs(node, graph, visited):
    visited.add(node)
    for nei in graph[node]:
        if nei not in visited:
            dfs(nei, graph, visited)

def iterative_dfs(node, graph, visited):
    visited.add(node)
    stack = [node]
    while stack:
        cur_node = stack.pop()
        for nei in graph[cur_node]:
            if nei not in visited:
                visited.add(nei)
                stack.append(nei)

visited = set()
count = 0
for node in graph.keys():
    if node not in visited:
        iterative_dfs(node, graph, visited)
        count += 1

print(count)
