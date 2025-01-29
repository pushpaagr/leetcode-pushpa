class Solution:
    def isValid(self, s: str) -> bool:
        valid = {')':'(', '}':'{', ']':'['}
        chars = []

        if len(s) == 1:
            return False

        for c in s:
            if c in valid.values():
                chars.append(c)
            elif chars and chars[-1] == valid.get(c):
                chars.pop()
            else:
                return False
        return not chars


