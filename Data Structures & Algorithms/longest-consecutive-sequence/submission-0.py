class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        seen = set(nums)
        maxCons = 0
        for num in seen:
            count = 1
            while num+count in seen:
                count +=1
            maxCons = max(maxCons, count)
        return maxCons
            

        