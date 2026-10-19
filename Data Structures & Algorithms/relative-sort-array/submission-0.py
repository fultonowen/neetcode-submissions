class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        idx_map = {}
        for idx, num in enumerate(arr2):
            idx_map[num] = idx
        
        arr1.sort(key= lambda x: idx_map.get(x, x + 1000))
        return arr1
        
        