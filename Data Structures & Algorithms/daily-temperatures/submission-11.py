class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        i = len(temperatures) - 1
        while i >= 0:
            if i+1 >= len(temperatures):
                i -=1
                continue
            j = i+1
            while j < len(temperatures):
                if temperatures[j] > temperatures[i]:
                    result[i] = j-i
                    break
                if result[j] == 0:
                    break
                j += result[j]
            
            i-=1
        return result