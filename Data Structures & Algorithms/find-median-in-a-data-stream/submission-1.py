import heapq

class MedianFinder:

    def __init__(self):
        self.small = []   # max heap
        self.large = []   # min heap

    def addNum(self, num: int) -> None:

        # Add to small (max heap)
        heapq.heappush(self.small, -num)

        # Make sure every value in small <= every value in large
        if self.large and -self.small[0] > self.large[0]:
            value = -heapq.heappop(self.small)
            heapq.heappush(self.large, value)

        # Balance sizes
        if len(self.small) > len(self.large) + 1:
            value = -heapq.heappop(self.small)
            heapq.heappush(self.large, value)

        elif len(self.large) > len(self.small):
            value = heapq.heappop(self.large)
            heapq.heappush(self.small, -value)

    def findMedian(self) -> float:

        # Odd number of elements
        if len(self.small) > len(self.large):
            return -self.small[0]

        # Even number of elements
        return (-self.small[0] + self.large[0]) / 2.0