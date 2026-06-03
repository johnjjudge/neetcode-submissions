class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        i = len(temperatures)-2
        while i >= 0:
            j = i+1
            while j < len(temperatures) and temperatures[j] <= temperatures[i]:
                if result[j] == 0:
                    j = len(temperatures)
                    break
                j += result[j]
            if j < len(temperatures):
                result[i] = j - i
            i-=1
        return result
                
                