class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False

        closeToOpen = {")": "(", "]": "[", "}":"{" }
        stack = []

        for c in s:
            if c in closeToOpen:
                print(c)
                print(closeToOpen[c])
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False 