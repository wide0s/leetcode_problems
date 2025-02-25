static int ge(const void* a, const void* b)
{
    int arg1 = *(const int*)a;
    int arg2 = *(const int*)b;
 
    if (arg1 < arg2) return -1;
    if (arg1 > arg2) return 1;
    return 0;
}

int hIndex(int* citations, int citationsSize) {
    int h, H_index = 0;

    if (!citations)
        return 0;
    qsort(citations, citationsSize, sizeof(int), ge);
    /* this loop can be replaced with a binary search,
     * see 275_h-index_ii.c */
    for (int i = 0; i < citationsSize; i++) {
        h = citationsSize - i;
        if (citations[i] >= h && h > H_index)
            H_index = h;
    }
    return H_index;
}
