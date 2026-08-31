class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = [0] * 128

        for ch in s:
            count[ord(ch)] += 1

        length = 0
        odd = False

        for c in count:
            length += (c // 2) * 2

            if c % 2 == 1:
                odd = True

        if odd:
            length += 1

        return length