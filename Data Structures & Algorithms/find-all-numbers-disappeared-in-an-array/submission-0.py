class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        allNums = set()
        for i in range(1,len(nums)+1):
            allNums.add(i)
        for num in nums:
            if num in allNums:
                allNums.remove(num)
        return list(allNums)