class Solution(object):
    # dump geedy implementation, runtime beats 100%, memory beats 63%
    def getLongestSubsequence(self, words, groups):
        """
        :type words: List[str]
        :type groups: List[int]
        :rtype: List[str]
        """
        n = len(words)
        assert n == len(groups)
        sentence = [words[0]]
        prev_group = groups[0]
        for word, group in zip(words[1::], groups[1::]):
            if group != prev_group:
                sentence += [word]
            prev_group = group
        return sentence

vectors = [
        ['e','a','b'], [0,0,1], ['e','b'],
        ['a','b','c','d'], [1,0,1,1], ['a','b','c']
        ]

for i in range(0, len(vectors), 3):
    words = vectors[i]
    groups = vectors[i+1]
    expected = vectors[i+2]
    returned = Solution().getLongestSubsequence(words, groups)
    assert expected == returned, f'for words {words} and groups {groups} expected {expected}, but returned {returned}!'
