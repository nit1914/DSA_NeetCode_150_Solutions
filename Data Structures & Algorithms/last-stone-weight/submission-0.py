import heapq

class Solution:
    def lastStoneWeight(self, stones):
        # Convert to max heap using negative values
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            # Get two heaviest stones
            y = -heapq.heappop(heap)
            x = -heapq.heappop(heap)

            # If weights are different, push the difference
            if x != y:
                heapq.heappush(heap, -(y - x))

        # Return remaining stone
        return -heap[0] if heap else 0