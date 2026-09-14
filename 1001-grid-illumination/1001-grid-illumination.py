class Solution:
    def gridIllumination(self, n, lamps, queries):
        rows = {}
        cols = {}
        diag1 = {}
        diag2 = {}
        active = set()

        def add(d, key):
            d[key] = d.get(key, 0) + 1

        def remove(d, key):
            d[key] -= 1
            if d[key] == 0:
                del d[key]


        for r, c in lamps:
            if (r, c) in active:
                continue

            active.add((r, c))
            add(rows, r)
            add(cols, c)
            add(diag1, r - c)
            add(diag2, r + c)

        ans = []

        for r, c in queries:
            
            if (r in rows or c in cols or
                r - c in diag1 or r + c in diag2):
                ans.append(1)
            else:
                ans.append(0)

            
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    nr, nc = r + dr, c + dc

                    if (nr, nc) in active:
                        active.remove((nr, nc))
                        remove(rows, nr)
                        remove(cols, nc)
                        remove(diag1, nr - nc)
                        remove(diag2, nr + nc)

        return ans