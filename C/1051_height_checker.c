#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <assert.h>

static void *arrcpy(size_t count, size_t size, const void *src) {
    void *copy = NULL;
    if (count && size && src) {
        copy = calloc(count, size);
        if (copy)
            memcpy(copy, src, count * size);
    }
    return copy;
}

static int ge(const void* a, const void* b)
{
    int arg1 = *(const int*)a;
    int arg2 = *(const int*)b;

    if (arg1 < arg2) return -1;
    if (arg1 > arg2) return 1;
    return 0;
}

int heightChecker(int* heights, int heightsSize) {
    int *sorted, n = 0;

    sorted = arrcpy(heightsSize, sizeof(int), heights);
    if (sorted) {
        qsort(sorted, heightsSize, sizeof(int), ge);
        for (int i = 0; i < heightsSize; i++) {
            if (heights[i] != sorted[i])
                n++;
        }
        free(sorted);
    }
    return n;
}

#define arrsz(a) (sizeof(a)/sizeof(a[0]))

int main(int argc, char **argv) {
    int heights1[] = {1, 1, 4, 2, 1, 3};
    int heights2[] = {5, 1, 2, 3, 4};
    int heights3[] = {1, 2, 3, 4, 5};
    assert(heightChecker(&heights1[0], arrsz(heights1)) == 3);
    assert(heightChecker(&heights2[0], arrsz(heights2)) == 5);
    assert(heightChecker(&heights3[0], arrsz(heights3)) == 0);
    return 0;
}

