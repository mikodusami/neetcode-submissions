class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        
        previous_end = float("-inf")
        removals = 0
        for start, end in intervals:
            if start >= previous_end:
                previous_end = end
            else:
                removals += 1
        
        return removals