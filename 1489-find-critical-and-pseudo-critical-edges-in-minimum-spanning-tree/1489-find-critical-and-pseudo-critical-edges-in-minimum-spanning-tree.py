class Solution:
    def findCriticalAndPseudoCriticalEdges(
        self, n: int, edges: list[list[int]]
    ) -> list[list[int]]:

    
        edges = [edge + [i] for i, edge in enumerate(edges)]


        edges.sort(key=lambda x: x[2])

        def kruskal(skip=-1, force=-1):
            parent = list(range(n))
            rank = [0] * n

            def find(x):
                while parent[x] != x:
                    parent[x] = parent[parent[x]]
                    x = parent[x]
                return x

            def union(a, b):
                a = find(a)
                b = find(b)

                if a == b:
                    return False

                if rank[a] < rank[b]:
                    a, b = b, a

                parent[b] = a

                if rank[a] == rank[b]:
                    rank[a] += 1

                return True

            total = 0
            count = 0

            
            if force != -1:
                u, v, w, idx = edges[force]

                if union(u, v):
                    total += w
                    count += 1

            
            for i, (u, v, w, idx) in enumerate(edges):
                if i == skip or i == force:
                    continue

                if union(u, v):
                    total += w
                    count += 1

                    if count == n - 1:
                        break

            if count != n - 1:
                return float("inf")

            return total

        
        mst_weight = kruskal()

        critical = []
        pseudo = []

        for i in range(len(edges)):

           
            if kruskal(skip=i) > mst_weight:
                critical.append(edges[i][3])

           
            elif kruskal(force=i) == mst_weight:
                pseudo.append(edges[i][3])

        return [critical, pseudo]