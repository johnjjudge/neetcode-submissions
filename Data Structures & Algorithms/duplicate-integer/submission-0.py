class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = {}
        for i in range(len(nums)):
            if nums[i] in counts:
                return True
            else: 
                counts[nums[i]] = 1
        return False
        