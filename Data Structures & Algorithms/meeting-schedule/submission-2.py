"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        # an interval overlaps if the start time of interval B is before the end of interval A, sort by start time, check if interval B is before intervalA
        intervals.sort(key=lambda x: x.start)
        current_interval = intervals[0]
        for i in range(1, len(intervals)):
            b = intervals[i]
            if b.start < current_interval.end:
                return False
            current_interval = b
        
        return True