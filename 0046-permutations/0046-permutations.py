class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        sol = []

        def backtrack():
            #base case
            if len(sol) == len(nums):
                res.append(sol.copy())
                return
            
            for num in nums:
                if num not in sol:
                    sol.append(num)
                    backtrack()
                    sol.pop()
        backtrack()
        return res

        #Time: O(n!)
        # space: O(n)
