class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        i = len(temperatures)-2
        while i >= 0:
            j = i+1
            while j < len(temperatures) and temperatures[j] <= temperatures[i]:
                j+= 1
            if j < len(temperatures) and temperatures[j] > temperatures[i]:
                result[i] = j - i
            i-=1
        return result
                
                