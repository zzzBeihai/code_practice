from heapq import heappop, heappush

class Solution:
    def shortestPath(self, n: int, edges: list[list[int]], labels: str, k: int) -> int:
        g = [[] for _ in range(n)]

        for x, y, w in edges:
            g[x].append((y, w))

        inf = float('inf')
        dis = [[inf] * (k + 1) for _ in range(n)]
        h = [(0, 0, 1)]

        while h:
            d, x, cnt = heappop(h)
            if x == n - 1:
                return d
            if d > dis[x][cnt]:
                continue
            for y, w in g[x]:
                new_cnt = 1 if labels[y] != labels[x] else cnt + 1
                new_dis = d + w
                if new_cnt <= k and new_dis < dis[y][new_cnt]:
                    dis[y][new_cnt] = new_dis
                    heappush(h, (new_dis, y, new_cnt))
        return -1