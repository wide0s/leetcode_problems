# Given an array of strings strs, group the anagrams together.
# You can return the answer in any order.
#
# Example 1:
#  Input: strs = ["eat","tea","tan","ate","nat","bat"]
#  Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# 
# Explanation:
#  There is no string in strs that can be rearranged to form
#  "bat".
#  The strings "nat" and "tan" are anagrams as they can be
#  rearranged to form each other.
#  The strings "ate", "eat", and "tea" are anagrams as they
#  can be rearranged to form each other.
#
# Constraints:
#  1 <= strs.length <= 104
#  0 <= strs[i].length <= 100
#  strs[i] consists of lowercase English letters

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = {}
        for word in strs:
            group = ''.join(sorted(word))
            if group in anagrams:
                anagrams[group].append(word)
            else:
                anagrams[group] = [word]
        return [ v for v in anagrams.values() ]

vectors = [
        ["eat","tea","tan","ate","nat","bat"], [["bat"],["nat","tan"],["ate","eat","tea"]],
        [""], [[""]],
        ["a"], [["a"]]
        ]

for i in range(0, len(vectors), 2):
    strs = vectors[i]
    print(strs)
    expected = vectors[i+1]
    for value in expected:
        value.sort()
    expected = sorted(expected)
    returned = Solution().groupAnagrams(strs)
    for value in returned:
        value.sort()
    returned = sorted(returned)
    assert expected == returned, f'for {strs} expected {expected}, but returned {returned}!'
