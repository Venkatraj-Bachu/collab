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
    size = 0
    queue = deque([node])
    visited.add(node)
    while queue:
        cur_node = queue.popleft()
        size += 1
        for neighbor in graph[cur_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return size

max_size = float('-inf')
visited = set()
for node in graph.keys():
    if node in visited:
        continue
    max_size = max(max_size, bfs(node, graph, visited))

print(max_size)
