class Solution(object):
    def convertDateToBinary(self, date):
        """
        :type date: str
        :rtype: str
        """
        y = date[0:4]
        m = date[5:7]
        d = date[8:]
        return '{0:b}-{1:b}-{2:b}'.format(int(y), int(m), int(d))

vectors = [
        '2080-02-29', '100000100000-10-11101',
        '1900-01-01', '11101101100-1-1'
        ]

for i in range(0, len(vectors), 2):
    date = vectors[i]
    expected = vectors[i+1]
    returned = Solution().convertDateToBinary(date)
    assert expected == returned, f'for {date} expected {expected}, but returned {returned}!'
