edges = [
    ['w', 'x'],
    ['x', 'y'],
    ['z', 'y'],
    ['z', 'v'],
    ['w', 'v']
]

from collections import defaultdict, deque
graph = defaultdict(list)
for (i, j) in edges:
    graph[i].append(j)
    graph[j].append(i)


def find_shortest_path(graph, start, target):
    if not graph or start == target:
        return 0
    
    queue = deque([(start, 0)])
    visited = set()
    visited.add(start)
    while queue:
        cur_node, cur_dist = queue.popleft()
        if cur_node == target:
            return cur_dist
        for neig in graph[cur_node]:
            if neig not in visited:
                visited.add(neig)
                queue.append((neig, cur_dist+1))
    return -1

print(find_shortest_path(graph, 'w', 'z'))
print(find_shortest_path(graph, 'w', 'i'))
