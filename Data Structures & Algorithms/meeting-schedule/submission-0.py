"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) == 0:
            return True
        sorted_data = sorted(intervals, key=lambda tup: (tup.start, tup.end))
        for i in range(len(sorted_data)-1):
            if sorted_data[i].end > sorted_data[i+1].start:
                return False
        return True
        

            
