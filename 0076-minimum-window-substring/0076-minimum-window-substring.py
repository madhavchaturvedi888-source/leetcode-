class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        from collections import Counter

        need = Counter(t)
        window = {}

        left = 0
        right = 0

        have = 0
        need_count = len(need)

        min_len = float("inf")
        start = 0

        while right < len(s):
            ch = s[right]
            window[ch] = window.get(ch, 0) + 1

            if ch in need and window[ch] == need[ch]:
                have += 1

            
            while have == need_count:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start = left

                left_ch = s[left]
                window[left_ch] -= 1

                if left_ch in need and window[left_ch] < need[left_ch]:
                    have -= 1

                left += 1

            right += 1

        if min_len == float("inf"):
            return ""

        return s[start:start + min_len]