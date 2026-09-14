class Solution:
    def minMoves(self, nums):
        mn = min(nums)
        return sum(num - mn for num in nums)
        