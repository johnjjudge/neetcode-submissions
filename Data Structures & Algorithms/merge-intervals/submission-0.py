class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        intervals.sort()
        result = []
        l = 0
        while l < len(intervals):
            start = intervals[l][0]
            end = intervals[l][1]
            r = l + 1
            while r < len(intervals) and intervals[r][0] <= end:
                end = max(end, intervals[r][1])
                r += 1
            result.append([start, end])
            l = r
        if l == len(intervals) - 1:
            result.append(intervals[l])
        return result
