from collections import deque

class Solution:
    def minimumTime(self, n: int, relations, time) -> int:
        g = [[] for _ in range(n)]
        indeg = [0] * n

        for u, v in relations:
            g[u - 1].append(v - 1)
            indeg[v - 1] += 1

        dp = time[:]
        q = deque(i for i in range(n) if indeg[i] == 0)

        while q:
            u = q.popleft()
            for v in g[u]:
                dp[v] = max(dp[v], dp[u] + time[v])
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        return max(dp)