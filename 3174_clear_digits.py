class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        zero = ord('0')
        for c in s:
            if 0 <= ord(c) - zero <= 9:
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(c)
        return s if len(s) == len(stack) else ''.join(stack)

vectors = [
        'abc', 'abc',
        'cb34', '',
        'a1bced34d45', 'b',
        '12', '',
        '', '',
        'abcgfh', 'abcgfh',
        'dfmkdslfkdjfkljslfkjldskjfdslkjfldksfjldskjfdslkjf', 'dfmkdslfkdjfkljslfkjldskjfdslkjfldksfjldskjfdslkjf',
        'alkjdsa824n5n9800454moi0fdgp', 'mofdgp'
        ]

for i in range(0, len(vectors), 2):
    s = vectors[i]
    expected = vectors[i+1]
    print(f'{s}')
    returned = Solution().clearDigits(s)
    assert expected == returned, f'for {s} expected {expected}, returned {returned}!'
