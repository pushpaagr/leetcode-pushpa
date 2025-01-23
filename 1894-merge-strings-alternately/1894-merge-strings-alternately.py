class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        letter_array = []  
        if len(word1) == len(word2):
             i = 0
             while i < len(word1):
                letter_array.append(word1[i])
                letter_array.append(word2[i])
                i += 1
        elif len(word1) < len(word2):
            i = 0
            while i < len(word1):
                letter_array.append(word1[i])
                letter_array.append(word2[i])
                i += 1
            letter_array.append(word2[i:])
        else:
            i = 0
            while i < len(word2):
                letter_array.append(word1[i])
                letter_array.append(word2[i])
                i += 1
            letter_array.append(word1[i:])
        
        return "".join(letter_array)

        