class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numsSet = set(nums)
        for n in range(len(nums)+1):
            if n not in numsSet:
                return n
        