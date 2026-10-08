class Solution:
    def validTree(self, n, edges):

        # A tree with n nodes must have exactly n - 1 edges
        if len(edges) != n - 1:
            return False

        # Create adjacency list
        graph = [[] for _ in range(n)]

        # Undirected graph
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        # DFS
        def dfs(node):
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        # Start DFS from node 0
        dfs(0)

        # All nodes must be connected
        return len(visited) == n