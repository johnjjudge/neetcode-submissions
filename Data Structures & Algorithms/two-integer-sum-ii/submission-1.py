class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            searchTarget = target - numbers[i]
            j = len(numbers)-1 # last index
            while numbers[i] < numbers[j]:
                if numbers[i] + numbers[j] == target:
                    return [i+1, j+1]
                else:
                    j-=1



        