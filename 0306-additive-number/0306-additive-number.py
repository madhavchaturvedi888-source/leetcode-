class Solution:
    def isAdditiveNumber(self, num: str) -> bool:

        def add(a, b):
    
            i = len(a) - 1
            j = len(b) - 1
            carry = 0
            result = []

            while i >= 0 or j >= 0 or carry:
                x = int(a[i]) if i >= 0 else 0
                y = int(b[j]) if j >= 0 else 0

                total = x + y + carry
                result.append(str(total % 10))
                carry = total // 10

                i -= 1
                j -= 1

            return ''.join(reversed(result))

        def check(a, b, start):
            if start == len(num):
                return True

            c = add(a, b)

            
            if not num.startswith(c, start):
                return False

            return check(b, c, start + len(c))

        n = len(num)

        
        for i in range(1, n):
            
            if num[0] == '0' and i > 1:
                break

            a = num[:i]

            
            for j in range(i + 1, n):
                
                if num[i] == '0' and j > i + 1:
                    break

                b = num[i:j]

                
                if i + len(b) >= n:
                    break

                if check(a, b, j):
                    return True

        return False