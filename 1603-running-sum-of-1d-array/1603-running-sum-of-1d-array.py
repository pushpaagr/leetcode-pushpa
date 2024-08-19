class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix_sum = 0
        i = 0
        while i < len(nums):
            prefix_sum += nums[i]
            nums[i] = prefix_sum
            i += 1
        return nums

# TC: O(N)
# SC: O(1)