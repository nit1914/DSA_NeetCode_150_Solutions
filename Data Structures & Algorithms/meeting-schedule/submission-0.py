
class Solution:
    def canAttendMeetings(self, intervals):
        # Sort by start time
        intervals.sort(key=lambda x: x.start)

        # Check overlapping meetings
        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i - 1].end:
                return False

        return True
