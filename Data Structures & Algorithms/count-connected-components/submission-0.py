class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for ai, bi in edges:
            graph[ai].append(bi)
            graph[bi].append(ai)
        
        seen = [False] * n
        def dfs(i: int):
            nonlocal graph, seen
            for neighbor in graph[i]:
                if not seen[neighbor]:
                    seen[neighbor] = True
                    dfs(neighbor)
        ans = 0
        for node in range(n):
            if not seen[node]:
                seen[node] = True
                ans += 1
                dfs(node)
        return ans
