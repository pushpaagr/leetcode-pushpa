class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = [''] * len(s)
        print(ans)
        for i, char in enumerate(s):
            new_position = indices[i]
            ans[new_position] = char
        return ''.join(ans)