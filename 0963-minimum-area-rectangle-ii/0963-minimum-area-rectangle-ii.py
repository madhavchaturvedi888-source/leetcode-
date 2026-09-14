from collections import defaultdict

class Solution:
    def minAreaFreeRect(self, points):

        n = len(points)
        groups = defaultdict(list)


        for i in range(n):
            x1, y1 = points[i]

            for j in range(i + 1, n):
                x2, y2 = points[j]

                mid = (x1 + x2, y1 + y2)
                dist = (x1 - x2) ** 2 + (y1 - y2) ** 2

                groups[(mid, dist)].append((i, j))

        ans = float('inf')


        for pairs in groups.values():
            for a in range(len(pairs)):
                i, j = pairs[a]

                for b in range(a + 1, len(pairs)):
                    k, l = pairs[b]

                    
                    if len({i, j, k, l}) < 4:
                        continue

                    x1, y1 = points[i]
                    x2, y2 = points[k]
                    x3, y3 = points[j]

                    
                    area = abs(
                        (x2 - x1) * (y3 - y1)
                        - (y2 - y1) * (x3 - x1)
                    )

                    if area > 0:
                        ans = min(ans, area)

        return 0 if ans == float('inf') else ans