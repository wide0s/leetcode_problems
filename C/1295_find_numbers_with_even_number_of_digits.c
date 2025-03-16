int findNumbers(int* nums, int numsSize) {
    int n, d, x;
    if (!num || !numsSize)
        return 0;
    n = 0;
    for (int i = 0; i < numsSize; i++) {
        d = 0;
	x = nums[i];
	while (x > 0) {
            x /= 10;
	    d++;
	}
	n += (d % 2 == 0);
    }
    return n;
}
