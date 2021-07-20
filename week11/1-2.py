class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n = len(dist)
        take_time = list()

        for idx in range(n):
            take_time.append(dist[idx]/speed[idx])
        take_time.sort()

        for idx in range(n):
            if idx >= take_time[idx]:
                return idx
        return n
