class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [ -stone for stone in stones ]
        heapq.heapify(stones)

        while len(stones) > 1:
            x, y = heapq.heappop(stones), heapq.heappop(stones)
            if x!=y:
                stone_weight = abs(x - y)
                heapq.heappush(stones, -stone_weight)
        
        return -stones[-1] if stones else 0
            


        