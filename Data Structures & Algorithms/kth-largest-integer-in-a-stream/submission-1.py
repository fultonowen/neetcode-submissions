import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.stack: List[int] = []
        for num in nums:
            heapq.heappush(self.stack, num)
            while len(self.stack) > k:
                heapq.heappop(self.stack)


    def add(self, val: int) -> int:
        heapq.heappush(self.stack, val)
        while len(self.stack) > self.k:
            heapq.heappop(self.stack)
        return self.stack[0]
        
