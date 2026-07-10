class Solution:
    def topKFrequent(self, nums, k):

        # Step 1: Count frequencies
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        # Step 2: Create buckets
        bucket = [[] for _ in range(len(nums) + 1)]

        # Step 3: Put numbers into buckets
        for num, freq in count.items():
            bucket[freq].append(num)

        # Step 4: Collect top k frequent numbers
        result = []

        for freq in range(len(bucket) - 1, 0, -1):
            for num in bucket[freq]:
                result.append(num)

                if len(result) == k:
                    return result