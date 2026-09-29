class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        visited = {}

        def dfs(curr):
            # If already cloned, return the existing clone
            if curr in visited:
                return visited[curr]

            # Create a copy of the current node
            clone = Node(curr.val)

            # Store the clone before visiting neighbors
            visited[curr] = clone

            # Clone all neighbors
            for neighbor in curr.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        return dfs(node)