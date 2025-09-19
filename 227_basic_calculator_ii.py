# copy of 224_basic_calculator.py

import math

class Solution(object):
    def toRPN(self, s):
        """
        Converts the given string to reverse Polish notation.
        :type tokens: str
        :rtype: List[str]
        """

        operators = {
            "+": {'precedence': 1, 'associative': "left"},
            "-": {'precedence': 1, 'associative': "left"},
            "*": {'precedence': 2, 'associative': "left"},
            "/": {'precedence': 2, 'associative': "left"},
        }

        stack = []
        rpn = []
        prev_tok = None
        number = ''
        for tok in s:
            if tok == ' ':
                continue

            if tok in "0123456789":
                number += tok
                continue

            if number != '':
                rpn.append(number)
                number = ''
                prev_tok = number # makes unary - detection better

            if tok == '-' and (prev_tok is None or prev_tok in operators or prev_tok == '('):
                rpn.append('0') # hack: prepend 0 to convert it to a binary operator
                stack.append(tok)
            elif tok in operators:
                while (len(stack) > 0 and stack[-1] in operators and \
                       (operators[stack[-1]]['precedence'] > operators[tok]['precedence'] or \
                        (operators[stack[-1]]['precedence'] == operators[tok]['precedence'] and \
                         operators[tok]['associative'] == 'left'))):
                    rpn.append(stack.pop())
                stack.append(tok)
            elif tok == "(":
                stack.append(tok)
            elif tok == ")":
                while stack[-1] != '(':
                    rpn.append(stack.pop())
                assert len(stack) > 0, 'invalid expression: missing ('
                stack.pop() # pop '('

            prev_tok = tok

        # add last number
        if number != '':
            rpn.append(number)

        while len(stack) > 0:
            tok = stack.pop()
            assert tok != '()', 'invalid expression: missing ('
            rpn.append(tok)

        return rpn

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

    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        rpn = self.toRPN(s)
        print(' RPN: \'' + ''.join(rpn) + '\'')
        return self.evalRPN(rpn)

vectors = [
    ["3+2*2", 7],
    [" 3/2 ", 1],
    [" 3+5 / 2 ", 5]
]

for vector in vectors:
    params = vector[0]
    expected = vector[1]
    print(f'infix notation is \'{params}\', answer = {expected}')
    returned = Solution().calculate(params)
    assert returned == expected, f'for {params} expected {expected}, but returned {returned}!'