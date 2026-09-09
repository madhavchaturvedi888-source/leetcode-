class Solution:
    def findAnagrams(self, s: str, p: str):
        if len(p) > len(s):
            return []

        result = []

        need = [0] * 26
        window = [0] * 26

        for ch in p:
            need[ord(ch) - ord('a')] += 1

        k = len(p)

        for i in range(len(s)):
            window[ord(s[i]) - ord('a')] += 1

            
            if i >= k:
                window[ord(s[i - k]) - ord('a')] -= 1

            if window == need:
                result.append(i - k + 1)

        return result