from collections import deque

class Solution:
    def canFinish(self, numCourses, prerequisites):

        # Create adjacency list
        graph = [[] for _ in range(numCourses)]

        # indegree[i] = number of prerequisites of course i
        indegree = [0] * numCourses

        # Build graph
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            indegree[course] += 1

        # Courses having no prerequisites
        queue = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        # Count completed courses
        completed = 0

        while queue:
            course = queue.popleft()
            completed += 1

            # Remove this course from the graph
            for next_course in graph[course]:
                indegree[next_course] -= 1

                # All prerequisites completed
                if indegree[next_course] == 0:
                    queue.append(next_course)

        # If every course was completed, no cycle exists
        return completed == numCourses