class Solution:
    def intervalIntersection(self, firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
        res = []

        i = 0
        j = 0
        n = len(firstList)
        m = len(secondList)

        while i < n and j < m:
            start1 = firstList[i][0]
            end1 = firstList[i][1]

            start2 = secondList[j][0]
            end2 = secondList[j][1]

            # Check overlap
            if max(start1, start2) <= min(end1, end2):
                s = max(start1, start2)
                e = min(end1, end2)
                res.append([s, e])

            # Move the pointer of the interval that ends first
            if end1 <= end2:
                i += 1
            else:
                j += 1

        return res