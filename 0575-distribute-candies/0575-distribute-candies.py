class Solution:
    def distributeCandies(self, candyType):
        n = len(candyType)
        unique = len(set(candyType))
        return min(unique, n // 2)