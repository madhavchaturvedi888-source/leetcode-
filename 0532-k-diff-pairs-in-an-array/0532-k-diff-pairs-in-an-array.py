class Solution:
    def findPairs(self, nums, k):
        if k < 0:
            return 0

        count = {}
        ans = 0

        for num in nums:
            count[num] = count.get(num, 0) + 1

        if k == 0:
            for num in count:
                if count[num] > 1:
                    ans += 1
        else:
            for num in count:
                if num + k in count:
                    ans += 1

        return ans
        