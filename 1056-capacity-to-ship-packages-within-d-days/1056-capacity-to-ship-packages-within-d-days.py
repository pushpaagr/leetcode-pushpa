class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def can_pass(capacity):
            days_taken = 1
            current_weight = 0
            for weight in weights:
                if weight > capacity:
                    return False
                current_weight += weight 
                if current_weight > capacity:
                    days_taken += 1
                    current_weight = weight
            return days_taken <= days

        lo = max(weights)
        hi = sum(weights)

        while lo <= hi:
            mid = (lo + hi) // 2
            if can_pass(mid):
                hi = mid - 1
            else:
                lo = mid + 1
        return lo 

# Time: O(Nlog(N))
# space: O(1)