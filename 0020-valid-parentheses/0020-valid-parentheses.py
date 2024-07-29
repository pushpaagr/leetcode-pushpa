class Solution:
    def isValid(self, s: str) -> bool:
        # can't start with a closed parenthesis
        # can't be a list of 1
        # if the size is odd won't work
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