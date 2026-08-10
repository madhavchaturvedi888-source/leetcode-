class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        sign = '+'

        for i in range(len(s)):
            ch = s[i]

            if ch.isdigit():
                num = num * 10 + int(ch)

            
            if (not ch.isdigit() and ch != ' ') or i == len(s) - 1:

                if sign == '+':
                    stack.append(num)

                elif sign == '-':
                    stack.append(-num)

                elif sign == '*':
                    stack.append(stack.pop() * num)

                elif sign == '/':
                    prev = stack.pop()

        
                    if prev < 0:
                        stack.append(-((-prev) // num))
                    else:
                        stack.append(prev // num)

                sign = ch
                num = 0

        return sum(stack)