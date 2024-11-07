class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_hash = {}
        output = []

        for num in nums:
            if num in nums_hash:
                nums_hash[num] += 1
            else:
                nums_hash[num] = 1
                
        sorted_items = sorted(nums_hash.items(), key=lambda item: item[1], reverse=True)

        for i in range(k):
            output.append(sorted_items[i][0])

        return output
        
        
            
                
        