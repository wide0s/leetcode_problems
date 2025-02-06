class Solution(object):
    # 4 ms, runtime beats 94%
    def removeAnagrams(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        singles = []
        prev_key = None
        for word in words:
            key = ''.join(sorted(word))
            if key != prev_key:
                singles.append(word)
                prev_key = key
        return singles

vectors = [
        ["abba","baba","bbaa","cd","cd"], ["abba","cd"],
        ["a","b","c","d","e"], ["a","b","c","d","e"],
        ["a","b","a"], ["a","b","a"]
        ]

for i in range(0, len(vectors), 2):
    words = vectors[i]
    print(words)
    expected = vectors[i+1]
    returned = Solution().removeAnagrams(words)
    assert expected == returned, f'for {words} expected {expected}, but returned {returned}!'
