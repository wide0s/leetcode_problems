class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0
        for j in range(len(s) - 1, -1, -1):
            if length != 0 and s[j] == ' ':
                break
            elif s[j] != ' ':
                length += 1
        return length

vectors = [
        " ", 0,
        "a", 1,
        "a bb                              ", 2,
        "a                                 ", 1,
        "Hello World", 5,
        "   fly me   to   the moon  ", 4,
        "luffy is still joyboy", 6
        ]

for i in range(0, len(vectors), 2):
    s = vectors[i]
    print(s)
    expected = vectors[i+1]
    returned = Solution().lengthOfLastWord(s)
    assert expected == returned, f'for \'{s}\' expected {expected}, but returned {returned}'
