class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        
        def dfs(i, cur, total):
            # base case
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return
            
            # one decision
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            # 2nd decision
            cur.pop()
            dfs(i+1, cur, total)
        
        dfs(0, [], 0)
        return res

            














        #Time: O(2^n)
            

       
