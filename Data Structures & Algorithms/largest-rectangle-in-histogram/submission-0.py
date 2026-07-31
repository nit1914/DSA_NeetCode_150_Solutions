class Solution:
    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0
        n = len(heights)

        for i in range(n + 1):
            curr_height = 0 if i == n else heights[i]

            while stack and heights[stack[-1]] > curr_height:
                h = heights[stack.pop()]
                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i
                max_area = max(max_area, h * width)

            stack.append(i)

        return max_area