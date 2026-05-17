class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet_size = 0
        position2 = sorted([(i, v) for i, v in enumerate(position)], key=lambda x: x[1])

        group_arrival_time = -1
        for idx, init_pos in reversed(position2):
            arrival_time = (target - init_pos) / speed[idx]
            if arrival_time > group_arrival_time:
                group_arrival_time = arrival_time
                fleet_size +=1
        return fleet_size
