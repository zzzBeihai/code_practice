import heapq
class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        idle = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(idle)

        busy = []

        ans = []
        now = 0

        def release(t: int) -> None:
            while busy and busy[0][0] <= t:
                _, i = heapq.heappop(busy)
                heapq.heappush(idle, (servers[i], i))

        for j, duration in enumerate(tasks):
            now = max(now, j)

            release(now)

            if not idle:
                now = busy[0][0]
                release(now)

            _, server_index = heapq.heappop(idle)
            ans.append(server_index)
            heapq.heappush(busy, (now + duration, server_index))

        return ans