class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            solution = target - nums[i]

            if solution in dic:
                if dic[solution] < i:
                    return [dic[solution], i]
                else:
                    return [i, dic[solution]]
            
            dic[nums[i]] = i