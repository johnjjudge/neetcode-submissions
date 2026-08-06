class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            numI = nums[i]
            searchNumJ = target - numI
            j = i + 1
            while j < len(nums):
                if searchNumJ == nums[j]:
                    return [i, j]
                j+=1
        return []