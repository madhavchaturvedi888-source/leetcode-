class Solution:
    def findDiagonalOrder(self, mat):
        m = len(mat)
        n = len(mat[0])
        ans = []

        for d in range(m + n - 1):
            diagonal = []

            
            r = 0 if d < n else d - n + 1
            c = d if d < n else n - 1

            while r < m and c >= 0:
                diagonal.append(mat[r][c])
                r += 1
                c -= 1

            if d % 2 == 0:
                ans.extend(diagonal[::-1])
            else:
                ans.extend(diagonal)

        return ans