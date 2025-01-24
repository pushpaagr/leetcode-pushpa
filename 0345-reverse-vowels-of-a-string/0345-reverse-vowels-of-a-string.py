class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a': 1, 'A':1, 'e': 1, 'E':1, 'i':1, 'I':1, 'o':1, 'O':1, 'u':1, 'U':1}
        new_s = list(s)
        j = len(s) - 1
        i = 0

        while i < j:
            if new_s[i] not in vowels:
                i += 1
            if new_s[j] not in vowels:
                j -= 1
            if new_s[i] in vowels and new_s[j] in vowels:
                new_s[i], new_s[j] = new_s[j], new_s[i]
                i += 1
                j -= 1
        return "".join(new_s)
            
