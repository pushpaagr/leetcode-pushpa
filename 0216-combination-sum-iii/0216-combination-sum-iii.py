class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [1,2,3,4,5,6,7,8,9]

        res = []

        def dfs(i, cur, total):
            # base case
            if total == n and len(cur) == k:
                res.append(cur.copy())
                return
            if i >= len(nums) or total > n or len(cur) > k:
                return
            

            cur.append(nums[i])
            dfs(i+1, cur, total + nums[i])
            
            cur.pop()
            dfs(i+1, cur, total)
        
        dfs(0,[],0)
        return res
            