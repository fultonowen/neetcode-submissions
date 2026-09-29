class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        min_seen_time = [float('inf')] * n

        for ui, vi, ti in times:
            graph[ui-1].append((vi-1, ti))
        
        min_heap = [(0, k-1)]
        min_seen_time[k-1] = 0
        while min_heap:
            t_curr, node = heapq.heappop(min_heap)
            if t_curr > min_seen_time[node]:
                continue

            for neighbor, time in graph[node]:
                if min_seen_time[neighbor] > t_curr + time:
                    heapq.heappush(min_heap, (t_curr + time, neighbor))
                    min_seen_time[neighbor] = t_curr + time
            
        
        max_seen_time = max(min_seen_time)
        
        return -1 if max_seen_time == float('inf') else int(max_seen_time)
