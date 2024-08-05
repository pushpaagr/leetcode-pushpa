class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            guess = nums[mid]
            if guess > target:
                r = mid - 1
            elif guess < target:
                l = mid + 1
            else:
                return mid        
        return -1 

# time: O(log(N))
# space: O(1) 
