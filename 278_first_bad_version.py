# You are a product manager and currently leading a team
# to develop a new product. Unfortunately, the latest version
# of your product fails the quality check. Since each version
# is developed based on the previous version, all the versions
# after a bad version are also bad.
#
# Suppose you have n versions [1, 2, ..., n] and you want to
# find out the first bad one, which causes all the following ones
# to be bad.
#
# You are given an API bool isBadVersion(version) which returns
# whether version is bad. Implement a function to find the first
# bad version. You should minimize the number of calls to the API.

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        lo, hi = 1, n
        while lo < hi:
            mid = (hi + lo) // 2
            if not isBadVersion(mid):
                lo = mid + 1
            else:
                hi = mid
        return lo

vectors = [
        5, 4,
        1, 1,
        ]

first_bad_version = 1
def isBadVersion(version):
    return version >= first_bad_version

for i in range(0, len(vectors), 2):
    n = vectors[i]
    first_bad_version = vectors[i+1]
    print(f'{n} {first_bad_version}')
    returned = Solution().firstBadVersion(n)
    assert first_bad_version == returned, f'for {n} expected {first_bad_version}, but returned {returned}!'
