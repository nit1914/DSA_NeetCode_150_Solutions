from collections import deque

class Solution:
    def foreignDictionary(self, words):
        # Create graph for every unique character
        graph = {c: set() for word in words for c in word}
        indegree = {c: 0 for c in graph}

        # Build graph from adjacent words
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]

            # Invalid prefix case
            if len(w1) > len(w2) and w1.startswith(w2):
                return ""

            # Find first different character
            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    a = w1[j]
                    b = w2[j]

                    if b not in graph[a]:
                        graph[a].add(b)
                        indegree[b] += 1

                    break

        # Topological sort
        queue = deque()

        for char in indegree:
            if indegree[char] == 0:
                queue.append(char)

        result = []

        while queue:
            char = queue.popleft()
            result.append(char)

            for neighbor in graph[char]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # Cycle detected
        if len(result) != len(graph):
            return ""

        return "".join(result)