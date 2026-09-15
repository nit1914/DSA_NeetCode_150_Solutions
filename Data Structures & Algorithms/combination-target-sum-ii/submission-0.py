class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        result = []

        def backtrack(start, remaining, path):
            if remaining == 0:
                result.append(path.copy())
                return

            for i in range(start, len(candidates)):
                # Skip duplicates at the same recursion level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # Since candidates is sorted, no later value can work
                if candidates[i] > remaining:
                    break

                # Choose candidates[i]
                path.append(candidates[i])

                # Move to i + 1 because each element can be used once
                backtrack(i + 1, remaining - candidates[i], path)

                # Undo choice
                path.pop()

        backtrack(0, target, [])
        return result 