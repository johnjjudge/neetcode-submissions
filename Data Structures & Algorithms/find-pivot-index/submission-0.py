class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i == 0:
                nums[i] = (nums[i], 0)
            else:
                nums[i] = (nums[i], nums[i-1][1] + nums[i-1][0])
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums) -1:
                nums[i] = (nums[i][0], nums[i][1], 0)
            else:
                nums[i] = (nums[i][0], nums[i][1], nums[i+1][2] + nums[i+1][0])

        for i in range(len(nums)):
            if nums[i][1] == nums[i][2]:
                return i
        return -1

        
