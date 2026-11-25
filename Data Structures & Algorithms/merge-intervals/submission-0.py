
class Solution:
    def merge(self, intervals):
        intervals.sort()
        
        result = []

        for start, end in intervals:
            # If result is empty or intervals don't overlap
            if not result or start > result[-1][1]:
                result.append([start, end])
            else:
                # Merge overlapping intervals
                result[-1][1] = max(result[-1][1], end)

        return result


# Example
intervals = [[1, 3], [1, 5], [6, 7]]

obj = Solution()
print(obj.merge(intervals))
