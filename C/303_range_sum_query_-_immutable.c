typedef struct {
    long long partial[0];
} NumArray;

NumArray* numArrayCreate(int* nums, int numsSize) {
    NumArray *pna;

    if (!nums || !numsSize)
        return NULL;
    pna = calloc(1, sizeof(long long) * (numsSize + 1));
    if (pna) {
        for (size_t i = 0; i < numsSize; i++)
            pna->partial[i + 1] = nums[i] + pna->partial[i];
    }
    return pna;
}

int numArraySumRange(NumArray* obj, int left, int right) {
    return obj->partial[right + 1] - obj->partial[left];
}

void numArrayFree(NumArray* obj) {
    free(obj);   
}
