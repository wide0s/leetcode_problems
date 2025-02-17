class Solution(object):
    # ?O(log(m))
    def distanceTraveled(self, mainTank, additionalTank):
        """
        :type mainTank: int
        :type additionalTank: int
        :rtype: int
        """
        d = 0
        m = mainTank
        a = additionalTank
        # return 10 * (m + min((m - 1) // 4, a))
        while m > 4:
            k = m // 5
            m = m % 5  + min(a, k)
            a -= min(a, k)
            d += 5 * k
        d += m
        return 10 * d

vectors = [
        5, 10, 60,
        1, 2, 10,
        9, 2, 110,
        29, 7, 360
        ]

for i in range(0, len(vectors), 3):
    mainTank = vectors[i]
    additionalTank = vectors[i+2]
    print(f'mainTank={mainTank} additionalTank={additionalTank}')
    expected = vectors[i+2]
    returned = Solution().distanceTraveled(mainTank, additionalTank)
    assert expected == returned, f'for {mainTank} liters and {additionalTank} liters expected {expected} km, but returned {returned} km!'
