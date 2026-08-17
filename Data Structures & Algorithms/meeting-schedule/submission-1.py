"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i:i.start)
        for indx in range(1,len(intervals)):
            
            if  intervals[indx].start< intervals[indx-1].end:
                return False
        return True
