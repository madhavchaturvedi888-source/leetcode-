from collections import Counter
from math import isqrt

class Solution:
    def numSquarefulPerms(self, nums):
        count = Counter(nums)
        n = len(nums)

        
        def square(a, b):
            x = a + b
            r = isqrt(x)
            return r * r == x

        
        graph = {x: [] for x in count}

        for a in count:
            for b in count:
                if a != b or count[a] > 1:
                    if square(a, b):
                        graph[a].append(b)

        def dfs(prev, used):
            if used == n:
                return 1

            ans = 0

            for nxt in graph[prev]:
                if count[nxt] > 0:
                    count[nxt] -= 1
                    ans += dfs(nxt, used + 1)
                    count[nxt] += 1

            return ans

        ans = 0

        for start in count:
            count[start] -= 1
            ans += dfs(start, 1)
            count[start] += 1

        return ans