class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        currDay = len(temperatures) - 2
        while currDay > -1:
            nextDay = currDay + 1
            while nextDay < len(temperatures) and temperatures[nextDay] <= temperatures[currDay]:
                if result[nextDay] == 0:
                    nextDay = len(temperatures)
                    break
                nextDay += result[nextDay]
            if nextDay < len(temperatures):
                result[currDay] = nextDay - currDay
            else:
                result[currDay] = 0
            currDay -= 1

        return result