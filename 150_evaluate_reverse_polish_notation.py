import math

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for tok in tokens:
            if tok == '+':
                stack.append(stack.pop() + stack.pop())
            elif tok == '*':
                stack.append(stack.pop() * stack.pop())
            elif tok == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif tok == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(math.trunc(float(b) / a))) # for python3: stack.append(int(float(b) / a))
            else:
                stack.append(int(tok))
        return stack[0]

vectors = [
    [["18"], 18],
    [["2","1","+","3","*"], 9],
    [["4","13","5","/","+"], 6],
    [["10","6","9","3","+","-11","*","/","*","17","+","5","+"], 22]
]

for vector in vectors:
    params = vector[0]
    expected = vector[1]
    print(f'reverse polish notation is {params}, answer = {expected}')
    returned = Solution().evalRPN(params)
    assert returned == expected, f'for {params} expected {expected}, but returned {returned}!'