class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        scores, stack = 0, []
        for op in operations:
            if op == 'C':
                scores -= stack.pop()
            elif op == 'D':
                stack.append(stack[-1] << 1)
                scores += stack[-1]
            elif op == '+':
                stack.append(stack[-1] + stack[-2])
                scores += stack[-1]
            else:
                stack.append(int(op))
                scores += stack[-1]
        return scores

vectors = [
    ["5","2","C","D","+"], 30,
    ["5","-2","4","C","D","9","+","+"], 27,
    ["1","C"], 0
]

for i in range(0, len(vectors), 2):
    operations = vectors[i]
    expected = vectors[i + 1]
    print(f'{operations} {expected}')
    returned = Solution().calPoints(operations)
    assert expected == returned, f'for {operations} expected {expected}, returned {returned}!'
