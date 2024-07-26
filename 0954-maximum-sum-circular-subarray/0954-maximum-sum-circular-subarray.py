class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        global_max = nums[0]
        curr_max = 0
        global_min = nums[0]
        curr_min = 0
        total = 0
        
        for n in nums:
            curr_max = max(curr_max + n, n)
            curr_min = min(curr_min + n, n)
            total += n
            global_max = max(global_max, curr_max)
            global_min = min(global_min, curr_min)
        
        return max(global_max, total - global_min) if global_max > 0 else global_max