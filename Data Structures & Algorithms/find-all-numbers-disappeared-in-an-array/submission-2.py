class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        allNums = set()
        for i in range(1, n+1, 1):
            allNums.add(i)
        for i in range(n):
            if nums[i] in allNums:
                allNums.remove(nums[i])
        return list(allNums)
