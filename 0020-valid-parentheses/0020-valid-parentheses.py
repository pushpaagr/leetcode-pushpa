class Solution:
    def isValid(self, s: str) -> bool:
        valid = {')':'(', '}':'{', ']':'['}
        chars = []

        if len(s) == 1:
            return False

        for c in s:
            if c == '(':
                chars.append(c)
            elif c == '{':
                chars.append(c)
            elif c == '[':
                chars.append(c)
            elif chars and chars[-1] == valid[']'] and c == ']':
                chars.pop()
            elif chars and chars[-1] == valid[')'] and c == ')':
                chars.pop()
            elif chars and chars[-1] == valid['}'] and c == '}':
                chars.pop()
            else:
                return False
            
        
        if not chars:
            return True
        else:
            return False 


