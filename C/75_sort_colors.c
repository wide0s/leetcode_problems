void sortColors(int* nums, int numsSize) {
    int colors[] = {0, 0, 0};
    int i, j, start = 0;
    if (!nums || !numsSize)
        return;
    for (i = 0; i < numsSize; i++) {
        colors[nums[i]]++;
    }
    for (j = 0; j < sizeof(colors)/sizeof(colors[0]); j++) {
        for (i = start; i < start + colors[j]; i++) {
            nums[i] = j;
        }
        start += colors[j];
    }
}
