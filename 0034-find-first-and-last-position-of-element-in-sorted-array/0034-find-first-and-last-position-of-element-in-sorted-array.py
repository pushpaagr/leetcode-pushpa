class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        #find starting position
        l = 0
        r = len(nums) - 1
        start_l = -1
        end_r = -1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] >= target:
                if nums[mid] == target:
                    start_l = mid
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
             
        if start_l == -1:
            return [start_l, end_r]    
        
        # find ending position
        l = 0
        r = len(nums) - 1

        while l<= r:
            mid = (l +r ) //2
            if nums[mid] <= target:
                if nums[mid] == target:
                    end_r = mid
                l = mid + 1
            else:
                r = mid - 1
        
        return[start_l, end_r]

# Time: O(log(N))
# Space: O(1)