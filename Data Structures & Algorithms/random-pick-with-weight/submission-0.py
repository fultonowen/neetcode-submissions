class Solution:

    def __init__(self, w: List[int]):
        self.idx_weight = []
        sum1 = sum(w)
        for idx, w_i in enumerate(w):
            for i in range(0, w_i):
                self.idx_weight.append(idx)
        print(self.idx_weight)
        self.original = w

    def pickIndex(self) -> int:
        idx = self.idx_weight[random.randint(0, len(self.idx_weight)-1)]
        return idx


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()