# Time complixity: O(log(len(a))
# Space complexity: O(1)
def bisection(a, target, left=0, right=None):
    assert left >= 0
    assert not right or right >= 0
    if not right:
        right = len(a)
    while left < right:
        mid = (right + left) // 2
        if a[mid] < target:
            left = mid + 1
        elif a[mid] > target:
            right = mid
        else:
            return mid
    return -1

# Time complexity: O(log(x))
def perfect(x):
    """
    Calculates the nearest perfect square less or equal than x.
    type: x: int
    rtype: int
    """
    assert x >= 0
    lo, hi = 0, int(x)
    while lo < hi:
        mid = (hi + lo) // 2
        if mid * mid < x:
            lo = mid + 1
        else:
            hi = mid
    if lo * lo > x:
        lo = lo - 1
    return lo

# https://www.geeksforgeeks.org/program-to-find-gcd-or-hcf-of-two-numbers/
# Time complexity: O(log(min(a, b)))
# Space complexity: O(1)
def gcd(a, b):
    """
    Calculates the greatest common divisor of a and b.
    type: a: int
    type: b: int
    rtype: int
    """
    while (a > 0 and b > 0):
        if a > b:
            a = a % b
        else:
            b = b % a
    if a == 0:
        return b
    return a

# Time complexity O(N)
def prod(a):
    """
    Calculates the product of an array of integers.
    type: a: List[int]
    rtype: int
    """
    v = 1
    for e in a:
        if e == 0:
            return 0
        v *= e
    return v
