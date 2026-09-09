import bisect

class Solution:
    def medianSlidingWindow(self, nums, k):
        window = sorted(nums[:k])
        result = []

        def get_median():
            if k % 2 == 1:
                return float(window[k // 2])
            return (window[k // 2 - 1] + window[k // 2]) / 2

        result.append(get_median())

        for i in range(k, len(nums)):
  
            old = nums[i - k]
            pos = bisect.bisect_left(window, old)
            window.pop(pos)

         
            bisect.insort(window, nums[i])

            result.append(get_median())

        return result