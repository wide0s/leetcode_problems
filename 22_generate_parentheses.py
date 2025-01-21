class Solution(object):
    # lookup table for n in [0, 3]
    lookup = { 0: ['()'], 1: ['()()', '(())'], 2: ['()(())', '((()))', '(())()', '(()())', '()()()'], 3: ['()(()())', '(()())()', '((()()))', '(()()())', '((())())', '(()(()))', '()()()()', '(())()()', '()(())()', '()()(())', '((()))()', '(())(())', '()((()))', '(((())))'] }

    def generate(self, _list):
        h = {}
        for e in _list:
            for key in { '()' + e, e + '()', '(' + e + ')' }:
                if key not in h:
                    h[key] = ''
            index = 0
            while index < len(e):
                if e[index:index + 2] == '()':
                    for key in [ e[0:index] + '()()' + e[index + 2:], e[0:index] + '(())' + e[index + 2:] ]:
                        if key not in h:
                            h[key] = ''
                    index += 1
                index += 1
        return list(h.keys())

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        index = min(len(Solution.lookup), n) - 1
        permutations = Solution.lookup[index]
        for i in range(n - index - 1):
            permutations = self.generate(permutations)
            if index + i + 1 < 8 and (index + i + 1 not in Solution.lookup):
                Solution.lookup[index + i + 1] = permutations
        return permutations

n = 8
Solution().generateParenthesis((n))
print(Solution().generateParenthesis((n)))
