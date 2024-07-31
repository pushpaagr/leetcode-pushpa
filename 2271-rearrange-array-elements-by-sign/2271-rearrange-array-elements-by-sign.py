class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = []
        negative = []
        combined = []
        for i in range(len(nums)):
            # positive
            if nums[i] > 0:
                positive.append(nums[i])
            else:
                negative.append(nums[i])
        
        for pos, neg in zip(positive, negative):
            combined.append(pos)
            combined.append(neg)
        
        return combined