class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        stack1, stack2 = [], []
        for i in range(0, max(len(s), len(t))):
            if i < len(s):
                if s[i] != '#':
                    stack1.append(s[i])
                elif len(stack1) > 0:
                    stack1.pop()
            if i < len(t):
                if t[i] != '#':
                    stack2.append(t[i])
                elif len(stack2) > 0:
                    stack2.pop()
        return stack1 == stack2

vectors = [
    ['ab#c', 'ad#c'], True,
    ['ab##', 'c#d#'], True,
    ['a#c', 'b'], False,
    ['a##c', '#a#c'], True
]

for i in range(0, len(vectors), 2):
    params = vectors[i]
    expected = vectors[i + 1]
    print(f'{params} {expected}')
    returned = Solution().backspaceCompare(*params)
    assert returned == expected, f'for {params} expected {expected}, returned {returned}!'

