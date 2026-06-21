class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(x: int, y: int) -> float:
            return -math.sqrt(x *x + y*y)
        k_closest = []

        for x_i, y_i in points:
            heapq.heappush(k_closest, [distance(x_i, y_i), x_i, y_i])
            while len(k_closest) > k:
                heapq.heappop(k_closest)
        
        res = []
        for i in range(len(k_closest)-1, -1, -1):
            res.append([k_closest[i][1], k_closest[i][2]])
        return res
