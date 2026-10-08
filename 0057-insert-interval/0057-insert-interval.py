class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        res = []

        start = newInterval[0]
        end = newInterval[1]

        for i in range(len(intervals)):
            s = intervals[i][0]
            e = intervals[i][1]

            if e < start:
                # Before new interval
                res.append([s, e])

            elif s > end:
                # After new interval
                res.append([start, end])
                start = s
                end = e

            else:
                # Overlap → merge
                start = min(start, s)
                end = max(end, e)

        # Add final interval
        res.append([start, end])

        return res