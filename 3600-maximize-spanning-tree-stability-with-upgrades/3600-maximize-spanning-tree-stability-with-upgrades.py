class Solution:
    def maxStability(self, n: int, edges: list[list[int]], k: int) -> int:

        class DSU:
            def __init__(self, n):
                self.parent = list(range(n))
                self.count = n

            def find(self, x):
                while self.parent[x] != x:
                    self.parent[x] = self.parent[self.parent[x]]
                    x = self.parent[x]
                return x

            def union(self, a, b):
                a = self.find(a)
                b = self.find(b)

                if a == b:
                    return False

                self.parent[b] = a
                self.count -= 1
                return True

    
        mandatory = []
        optional = []

        for u, v, s, must in edges:
            if must == 1:
                mandatory.append((u, v, s))
            else:
                optional.append((u, v, s))

        
        dsu = DSU(n)

        for u, v, s in mandatory:
            if not dsu.union(u, v):
                return -1

        def possible(target):
            dsu = DSU(n)

            
            for u, v, s in mandatory:
                if s < target:
                    return False

                if not dsu.union(u, v):
                    return False

            upgrades = 0

        
            for u, v, s in optional:
                if s >= target:
                    dsu.union(u, v)

        
            for u, v, s in optional:
                if s < target and 2 * s >= target:
                    if dsu.union(u, v):
                        upgrades += 1

                        if upgrades > k:
                            return False

            return dsu.count == 1


        low = 1
        high = max(s * 2 for _, _, s, _ in edges)
        answer = -1

        while low <= high:
            mid = (low + high) // 2

            if possible(mid):
                answer = mid
                low = mid + 1
            else:
                high = mid - 1

        return answer