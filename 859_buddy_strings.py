class Solution(object):
    def buddyStrings(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if len(s) != len(goal):
            return False
        if s == goal:
            # check for duplicate characters
            return len(set(s)) < len(s)
        # find positions where characters differ
        diffs = [(a, b) for a, b in zip(s, goal) if a != b]
        # exactly two mismatches and swapping should fix it
        return len(diffs) == 2 and diffs[0] == diffs[1][::-1]

vectors = [
    ['ab', 'ba'], True,
    ['ab', 'ab'], False,
    ['aa', 'aa'], True,
    ['abc', 'cba'], True,
    ['abcaa', 'abcbb'], False
]

for i in range(0, len(vectors), 2):
    params = vectors[i]
    expected = vectors[i + 1]
    print(f'{params} {expected}')
    returned = Solution().buddyStrings(*params)
    assert returned == expected, f'for {params} expected {expected}, returned {returned}!'
