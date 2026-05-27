class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        solution = []
        for i in range(len(nums)):
            if nums[i] == 0:
                value = int(math.prod(nums[:i] + nums[i+1:]))
            else:
                value = int(math.prod(nums) / nums[i])
            solution.append(value)
                
        
        return solution