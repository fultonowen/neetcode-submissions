class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_eat(rate: int) -> bool:
            nonlocal piles, h
            time = 0
            for num in piles:
                time += int(math.ceil(num / rate))
            
            return time <= h
        
        l, r = 1, max(piles)

        while l <= r:
            mid = (l + r) // 2
            if can_eat(mid) == True:
                r = mid - 1
            else:
                l = mid + 1
        
        return l