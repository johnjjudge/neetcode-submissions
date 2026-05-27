class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        for left in range(len(temperatures)):
            right = left
            while right < len(temperatures) and temperatures[right] <= temperatures[left]:
                right+=1
            if right != len(temperatures):
                result[left] = right - left
        return result

            
        