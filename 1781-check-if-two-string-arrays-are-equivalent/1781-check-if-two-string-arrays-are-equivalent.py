class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        char1 = 0
        char2 = 0
        
        string1 = 0
        string2 = 0

        while True:
            ch1 = word1[string1][char1]
            ch2 = word2[string2][char2]

            if ch1 != ch2:
                return False
            
            char1 += 1
            char2 += 1
            
            if char1 == len(word1[string1]):
                string1 += 1
                char1 = 0
            if char2 == len(word2[string2]):
                string2 += 1
                char2 = 0
            
            if string1 == len(word1) and string2 == len(word2):
                break
            if string1 == len(word1) or string2 == len(word2):
                return False
        
        return True

# Time: O(N)
# Space: O(1)
        