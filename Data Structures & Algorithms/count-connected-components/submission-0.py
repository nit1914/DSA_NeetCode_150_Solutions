
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Step 1: Build adjacency list
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Step 2: Track visited nodes
        visited = [False] * n
        components = 0

        # Step 3: DFS traversal
        def dfs(node):
            visited[node] = True

            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor)

        # Step 4: Count connected components
        for node in range(n):
            if not visited[node]:
                components += 1
                dfs(node)

        return components
