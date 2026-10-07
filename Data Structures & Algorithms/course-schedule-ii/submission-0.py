from collections import deque

class Solution:
    def findOrder(self, numCourses, prerequisites):

        # Create adjacency list
        graph = [[] for _ in range(numCourses)]

        # Indegree of every course
        indegree = [0] * numCourses

        # Build graph
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            indegree[course] += 1

        # Add courses with no prerequisites
        queue = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        # Store course order
        order = []

        # BFS / Kahn's Algorithm
        while queue:

            current = queue.popleft()
            order.append(current)

            # Process courses dependent on current
            for next_course in graph[current]:

                indegree[next_course] -= 1

                # All prerequisites completed
                if indegree[next_course] == 0:
                    queue.append(next_course)

        # Cycle detected
        if len(order) != numCourses:
            return []

        return order