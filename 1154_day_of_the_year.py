class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        # days for previous months
        days_passed = [0,31,59,90,120,151,181,212,243,273,304,334]
        y, m, d = (int(d) for d in date.split('-'))
        doy = days_passed[m - 1] + d
        # A leap year must be divisble by 4 and not divisible by 100
        # or divisible by 400
        if m > 2 and ((y % 4 == 0 and y % 100 != 0) or y % 400 == 0):
            doy += 1
        return doy

vectors = [
        "2019-01-09", 9,
        "2019-02-10", 41,
        "1904-03-05", 65
        ]

for i in range(0, len(vectors), 2):
    date = vectors[i]
    doy = vectors[i + 1]
    print(f'{date} DOY is {doy}')
    returned = Solution().dayOfYear(date)
    assert returned == doy, f'for {date} day of the year is {doy}, returned {returned}!'
