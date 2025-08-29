# https://www.youtube.com/watch?v=rw4s4M3hFfs

# greatest number of consecutive build runs that have a strictly decreasing green percentage

builds = [
    [True, True, True, False, False], # 60%
    [True, True, True, True, False], #  80%
    [True, True, True, True, True, True, False, False, False], # ~67%
    [True, False, False, False, False, False], # ~17%
    [True, True, True, True, True, True, True, True, True, True, True, True, False], # ~92%
    [True, False],  # 50%
    [True, True, True, False, False], # 60%
]

def pc(a): # O(log(N))
    left = 0
    right = len(a)
    while left < right:
        mid = (right + left) // 2
        if a[mid] == True:
            left = mid + 1
        else:
            right = mid
    return (left / len(a)) * 100

n_builds = l = r = 0
for r in range(1, len(builds)): # O(N*log(N))
    if (pc(builds[r]) >= pc(builds[r - 1])):
        n_builds = max(n_builds, r - l)
        l = r

print(f'n_builds: {n_builds}')