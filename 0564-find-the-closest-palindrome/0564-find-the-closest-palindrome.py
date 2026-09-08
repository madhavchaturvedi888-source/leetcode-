class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length = len(n)
        num = int(n)

        candidates = set()

        
        candidates.add(10 ** length + 1)
        candidates.add(10 ** (length - 1) - 1)

        
        half = int(n[:(length + 1) // 2])

        
        for x in [half - 1, half, half + 1]:
            s = str(x)

            if length % 2 == 0:
                palindrome = s + s[::-1]
            else:
                palindrome = s + s[:-1][::-1]

            candidates.add(int(palindrome))

        
        candidates.discard(num)

        
        return str(min(candidates, key=lambda x: (abs(x - num), x)))