class Solution:
    def minStickers(self, stickers: list[str], target: str) -> int:
        sticker_count = []

        for sticker in stickers:
            count = [0] * 26
            for ch in sticker:
                count[ord(ch) - ord('a')] += 1
            sticker_count.append(count)

        memo = {"": 0}

        def dfs(rem):
            if rem in memo:
                return memo[rem]

            target_count = [0] * 26
            for ch in rem:
                target_count[ord(ch) - ord('a')] += 1

            ans = float('inf')

            for sticker in sticker_count:
                
                first = ord(rem[0]) - ord('a')
                if sticker[first] == 0:
                    continue

                new_rem = []

                for i in range(26):
                    if target_count[i] > sticker[i]:
                        new_rem.extend(
                            [chr(i + ord('a'))] * (target_count[i] - sticker[i])
                        )

                new_rem = ''.join(new_rem)

                ans = min(ans, 1 + dfs(new_rem))

            memo[rem] = ans
            return ans

        result = dfs(target)

        return -1 if result == float('inf') else result