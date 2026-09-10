class Solution:
    def countOfAtoms(self, formula):
        stack = [{}]
        i = 0
        n = len(formula)

        while i < n:
            if formula[i] == '(':
                stack.append({})
                i += 1

            elif formula[i] == ')':
                i += 1
                num = 0

                while i < n and formula[i].isdigit():
                    num = num * 10 + int(formula[i])
                    i += 1

                if num == 0:
                    num = 1

                top = stack.pop()

                for atom, count in top.items():
                    stack[-1][atom] = stack[-1].get(atom, 0) + count * num

            else:
                
                atom = formula[i]
                i += 1

                while i < n and formula[i].islower():
                    atom += formula[i]
                    i += 1

                
                num = 0
                while i < n and formula[i].isdigit():
                    num = num * 10 + int(formula[i])
                    i += 1

                if num == 0:
                    num = 1

                stack[-1][atom] = stack[-1].get(atom, 0) + num

        
        result = []

        for atom in sorted(stack[-1]):
            result.append(atom)
            count = stack[-1][atom]
            if count > 1:
                result.append(str(count))

        return ''.join(result)