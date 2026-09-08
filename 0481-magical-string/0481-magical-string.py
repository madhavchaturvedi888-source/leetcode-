class Solution:
    def magicalString(self, n: int) -> int:
        if n <= 0:
            return 0
        if n <= 3:
            return 1

        s = [1, 2, 2]
        i = 2
        count = 1

        while len(s) < n:
            next_num = 3 - s[-1]

            for _ in range(s[i]):
                s.append(next_num)

                if next_num == 1 and len(s) <= n:
                    count += 1

            i += 1

        return count