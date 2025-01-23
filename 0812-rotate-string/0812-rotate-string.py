class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if s == goal:
            return True
        if len(s) != len(goal):
            return False

        length = len(s) - 1
        for _ in range(len(s)):
            s = s[1:] + s[0]
            if s == goal:
                return True
        return False


