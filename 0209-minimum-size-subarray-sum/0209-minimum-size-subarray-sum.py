class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        target_sum = 0
        L = 0 
        min_length = float("inf")
        
        for R in range(len(nums)):
            target_sum += nums[R]
            while target_sum >= target: 
                min_length = min(min_length, R - L + 1)
                target_sum -= nums[L]
                L += 1
        
        return 0 if min_length == float("inf") else min_length

            
