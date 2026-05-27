class Solution:
    def rob(self, nums: List[int]) -> int:
        lenNums = len(nums)
        if lenNums == 1:
            return nums[0]
        if lenNums == 2:
            return max(nums[0], nums[1])
        if lenNums == 3:
            return max(nums[0]+ nums[2], nums[1])
        cache = {}
        cache[0] = nums[0]
        cache[1] = nums[1]
        cache[2] = nums[2] + nums[0]
        i = 3
        while i < lenNums:
            cache[i] = max(nums[i] + cache[i-2], nums[i] + cache[i-3])
            i+=1
        return max(cache[lenNums-1], cache[lenNums-2])
        
        