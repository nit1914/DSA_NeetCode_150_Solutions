from collections import Counter

class Solution:
    def leastInterval(self, tasks, n):
        freq = Counter(tasks)

        max_freq = max(freq.values())

        max_count = sum(
            1 for count in freq.values()
            if count == max_freq
        )

        result = (max_freq - 1) * (n + 1) + max_count

        return max(len(tasks), result)