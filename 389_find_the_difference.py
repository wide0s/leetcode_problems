class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # my and slow, runtime beats 26%
        #f = [0] * 26
        #for c, e in zip(s, t):
        #    f[ord(c) - ord('a')] += 1
        #    f[ord(e) - ord('a')] -= 1
        #f[ord(t[len(t) - 1]) - ord('a')] -= 1
        #for e in t:
        #    if f[ord(e) - ord('a')] != 0:
        #        return e
        for i in t:
            if s.count(i) != t.count(i):
                return i
        assert True == False, 'should not be here!'

vectors = [
        'abcd', 'abcde', 'e',
        '', 'y', 'y',
        'abcdefghij', 'bcafedhigz', 'z',
        'a', 'aa', 'a'
        ]

for i in range(0, len(vectors), 3):
    s = vectors[i]
    t = vectors[i+1]
    print(f'{s} {t}')
    expected = vectors[i+2]
    returned = Solution().findTheDifference(s,t)
    assert expected == returned, f'for \'{s}\' and \'{t}\' expected \'{expected}\', but returned \'{returned}\'!'
