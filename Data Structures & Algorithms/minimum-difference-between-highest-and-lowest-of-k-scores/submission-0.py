class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1: return 0
        nums.sort()
        i = 0
        minSpread = nums[len(nums)-1] - nums[0]
        while i + k - 1 < len(nums):
            minSpread = min(minSpread, nums[k+i-1]-nums[i])
            i+=1
        return minSpread