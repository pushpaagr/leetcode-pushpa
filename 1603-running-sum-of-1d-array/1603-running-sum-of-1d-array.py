class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix = 0
        i = 0
        while i < len(nums):
            prefix += nums[i]
            nums[i] = prefix
            i += 1
        return nums

# TC: O(N)
# SC: O(1)