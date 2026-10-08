class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        res = []

        intervals.sort() # Sort by start time

        start = intervals[0][0]
        end = intervals[0][1]

        for i in range(1, len(intervals)):
            s = intervals[i][0]
            e = intervals[i][1]

            if end >= s:  # Overlap → extend
                end = max(end, e)
                continue

            res.append([start, end]) # No overlap → save
            start = s
            end = e

        res.append([start, end]) # Save last interval
        return res