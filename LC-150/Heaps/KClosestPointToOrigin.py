import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []

        for i in points:
            dist = math.sqrt((i[0] - 0)**2 + (i[1] - 0)**2)
            heapq.heappush(heap, (dist, i))

        for i in range(k):
            pt = heapq.heappop(heap)[1]
            res.append(pt)

        return res
