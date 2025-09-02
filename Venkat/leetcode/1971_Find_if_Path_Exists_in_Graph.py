class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        graph = defaultdict(list)

        for (i, j) in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        queue = deque()
        visited = set()
        queue.append(source)
        visited.add(source)

        while queue:
            cur_node = queue.popleft()
            if cur_node == destination:
                return True
            for neig in graph[cur_node]:
                if neig not in visited:
                    visited.add(neig)
                    queue.append(neig)
        
        return False