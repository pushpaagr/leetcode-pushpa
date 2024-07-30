class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        current_sum = sum(arr[:k])  # Sum of the first k elements
        
        # Check the initial window
        if current_sum / k >= threshold:
            count += 1
        
        # Slide the window across the array
        for i in range(k, len(arr)):
            current_sum += arr[i] - arr[i - k]  # Update the sum by sliding the window
            if current_sum / k >= threshold:  # Compare average directly
                count += 1
        
        return count
        
        