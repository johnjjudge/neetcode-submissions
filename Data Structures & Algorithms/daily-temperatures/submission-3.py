class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        left = 0
        result = [0] * len(temperatures)
        while left < len(temperatures):
            right = left + 1
            while right < len(temperatures) and temperatures[right] <= temperatures[left]:
                right += 1
            if right < len(temperatures):
                result[left] = right - left
            left += 1
        return result
