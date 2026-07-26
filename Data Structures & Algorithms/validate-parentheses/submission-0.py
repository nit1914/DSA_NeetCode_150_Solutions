class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for ch in s:
            if ch in closeToOpen:
                if stack and stack[-1] == closeToOpen[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)

        return len(stack) == 0