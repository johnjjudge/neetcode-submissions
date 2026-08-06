class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            solution = target - nums[i]
            if solution in dic:
                return [dic[solution], i]
            dic[nums[i]] = i 