class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        prevEnd = intervals[0][1]
        removed = 0

        for i in intervals[1:]:
            if i[0] < prevEnd:
                removed += 1
                prevEnd = min(i[1], prevEnd)
            else:
                prevEnd = i[1]
            
        
        return removed