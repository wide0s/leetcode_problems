#include <stddef.h>

void moveZeroes(int* nums, int numsSize) {
    size_t j;
    int temp;

    if (!nums || !numsSize)
        return;

    for (size_t i = 0, j = 0; i < numsSize; i++) {
        if (nums[i]) {
            temp = nums[j];
            nums[j] = nums[i];
            nums[i] = temp;
            j += 1;
        }
    }
}