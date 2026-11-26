
class Solution:
    def eraseOverlapIntervals(self, intervals):
        # Sort intervals by ending time
        intervals.sort(key=lambda x: x[1])

        count = 0
        end = intervals[0][1]

        for i in range(1, len(intervals)):

            # Check if intervals overlap
            if intervals[i][0] < end:
                count += 1

            else:
                # Keep the non-overlapping interval
                end = intervals[i][1]

        return count


# Example 1
intervals = [[1, 2], [2, 4], [1, 4]]

obj = Solution()
print(obj.eraseOverlapIntervals(intervals))

# Example 2
intervals = [[1, 2], [2, 4]]

print(obj.eraseOverlapIntervals(intervals))
