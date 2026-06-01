"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        
        maxOcc = 0
        
        min_start = min(t.start for t in intervals)
        max_end = max(t.end for t in intervals)

        for i in range(min_start, max_end + 1):
            occHour = 0
            for j in range(len(intervals)):
                if intervals[j].start <= i < intervals[j].end:
                    occHour += 1
            maxOcc = max(maxOcc, occHour)
        return maxOcc
