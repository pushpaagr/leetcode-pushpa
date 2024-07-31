class Solution:
    def isPalindrome(self, s: str) -> bool:
    # [TC: O(N) SC: O(N)]
    #   newStr = "" 
    #   for char in s:
    #     if char.isalnum():
    #         newStr += char.lower()
    #   if newStr == newStr[::-1]:
    #     return True
    #   else:
    #     return False

    #[TC:O(N) SC: O(1)]
        l = 0
        r = len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                print(s[l])
                l += 1
            while l < r and not s[r].isalnum():
                print(s[r])
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        
        return True
            