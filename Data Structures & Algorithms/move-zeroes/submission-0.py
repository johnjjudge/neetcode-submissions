class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        numZeros = 0
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                nums.pop(i)
                numZeros+=1
            else:
                i += 1
        while numZeros > 0:
            nums.append(0)
            numZeros -=1
