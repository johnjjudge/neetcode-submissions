class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        vals = {}
        lenNums = len(nums)
        for i in range(lenNums):
            if nums[i] not in vals:
                vals[nums[i]] = 1
            else:
                vals[nums[i]] += 1
            if vals[nums[i]] > lenNums/2:
                return nums[i]
        