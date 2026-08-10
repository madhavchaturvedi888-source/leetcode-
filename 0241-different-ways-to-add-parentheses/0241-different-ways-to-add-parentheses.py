class Solution:
    def diffWaysToCompute(self, expression: str) -> list[int]:
        memo = {}

        def solve(exp):
            if exp in memo:
                return memo[exp]

            result = []

            for i, ch in enumerate(exp):
                if ch in "+-*":
                    left = solve(exp[:i])
                    right = solve(exp[i + 1:])

                    for a in left:
                        for b in right:
                            if ch == '+':
                                result.append(a + b)
                            elif ch == '-':
                                result.append(a - b)
                            else:
                                result.append(a * b)

            
            if not result:
                result.append(int(exp))

            memo[exp] = result
            return result

        return solve(expression)