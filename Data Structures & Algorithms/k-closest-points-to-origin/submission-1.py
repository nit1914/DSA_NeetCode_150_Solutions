import heapq

class Solution:
    def kClosest(self, points, k):
        max_heap = []

        for x, y in points:
            distance = x * x + y * y

            # Negative distance -> Python's min heap acts like max heap
            heapq.heappush(max_heap, (-distance, x, y))

            # Keep only k closest points
            if len(max_heap) > k:
                heapq.heappop(max_heap)

        return [[x, y] for _, x, y in max_heap]