class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        i = len(temperatures)-2
        while i >= 0:
            r = i+1
            while temperatures[r] <= temperatures[i]:
                if result[r] == 0:
                    r = i
                    break
                r += result[r]
            result[i] = r - i
            i-=1
        return result