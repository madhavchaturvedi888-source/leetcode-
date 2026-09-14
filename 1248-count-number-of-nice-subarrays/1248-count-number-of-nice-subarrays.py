class Solution:
    def numberOfSubarrays(self, nums, k):
        def atMost(k):
            left = 0
            ans = 0

            for right in range(len(nums)):
                if nums[right] % 2 == 1:
                    k -= 1

                while k < 0:
                    if nums[left] % 2 == 1:
                        k += 1
                    left += 1

                ans += right - left + 1

            return ans

        return atMost(k) - atMost(k - 1)