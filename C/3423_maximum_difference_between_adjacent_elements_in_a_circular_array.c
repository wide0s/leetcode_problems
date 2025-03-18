static inline int max(int a, int b) {
    return a > b ? a : b;
}

int maxAdjacentDistance(int* nums, int numsSize) {
    int dist;
    if (!nums || numsSize < 2)
        return 0;
    dist = abs(nums[numsSize - 1] - nums[0]);
    for (int i = 1; i < numsSize; i++)
        dist = max(dist, abs(nums[i - 1] - nums[i]));
    return dist;
}
