class Solution:
    def reverseVowels(self, s: str) -> str:
        vowles = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

        i = 0
        j = len(s) - 1
        charArray = list(s)
        while i < j:
            print("i:", i)
            print("j:", j)
            if charArray[j] not in vowles:
                j -= 1
            elif charArray[i] not in vowles:
                i += 1
            else:
                charArray[i], charArray[j] =  charArray[j], charArray[i]
                i += 1
                j -= 1
        return "".join(charArray)