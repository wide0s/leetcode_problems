def bisect(a, target, left=0, right=None):
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
