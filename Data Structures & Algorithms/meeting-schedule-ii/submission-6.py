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
        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])
        maxOcc = 0
        overlaps = 0
        s_ptr, e_ptr = 0, 0
        while s_ptr < len(intervals):
            if starts[s_ptr] < ends[e_ptr]:
                overlaps += 1
                s_ptr += 1
            else:
                overlaps -= 1
                e_ptr += 1
            maxOcc = max(maxOcc, overlaps)
        return maxOcc
