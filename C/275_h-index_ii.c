int hIndex(int* citations, int citationsSize) {
    int lo, hi, mid;

    if (!citations)
        return 0;

    lo = 0;
    hi = citationsSize;
    while (lo < hi) {
        mid = (hi + lo) / 2;
        if (citations[mid] < citationsSize - mid) {
            lo = mid + 1;
        } else {
            hi = mid;
        }
    }
    return citationsSize - lo;
}
