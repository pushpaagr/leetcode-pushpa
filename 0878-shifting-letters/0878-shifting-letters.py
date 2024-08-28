class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        postfix_sum = sum(shifts)
        answer = []

        char_to_index = {char: i for i, char in enumerate('abcdefghijklmnopqrstuvwxyz')}
        print(char_to_index)
        index_to_char = "abcdefghijklmnopqrstuvwxyz"
        for i, char in enumerate(s):
            shifted_i = (char_to_index[char] + postfix_sum) % 26
            answer.append(index_to_char[shifted_i])
            postfix_sum -= shifts[i]
        return "".join(answer)
    # Time: O(N)
    # O(1)