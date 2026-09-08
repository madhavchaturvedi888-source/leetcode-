class Solution:
    def findMinDifference(self, timePoints: list[str]) -> int:
        minutes = []

        for time in timePoints:
            h, m = map(int, time.split(":"))
            minutes.append(h * 60 + m)

        minutes.sort()

        ans = 1440  

        for i in range(1, len(minutes)):
            ans = min(ans, minutes[i] - minutes[i - 1])

        
        ans = min(ans, 1440 - minutes[1] + minutes[0])

        return ans