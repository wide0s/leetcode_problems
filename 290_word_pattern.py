from collections import defaultdict
class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split()
        # reusing the code from 205_isomorphic_strings.py
        if len(pattern) != len(words):
            return False
        w2l = defaultdict(str)
        l2w = defaultdict(str)
        for i in range(len(words)):
            letter = pattern[i]
            if words[i] in w2l:
                if w2l[words[i]] != letter:
                    return False
            elif letter in l2w:
                return False
            else:
                w2l[words[i]] = letter
                l2w[letter] = words[i]
        return True

vectors = [
    ['abba', 'dog cat cat dog'], True, 
    ['abba', 'dog cat cat fish'], False,
    ['aaaa', 'dog cat cat dog'], False,
]

for i in range(0, len(vectors), 2):
    params = vectors[i]
    expected = vectors[i + 1]
    print(f'{params} {expected}')
    returned = Solution().wordPattern(*params)
    assert expected == returned, f'for {params} expected {expected}, returned {returned}!'
