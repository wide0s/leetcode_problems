int mySqrt(int x) {
    long lo, hi, mid;

    lo = 0;
    hi = x;
    while (lo < hi) {
        mid = (hi + lo) / 2;
        if (mid * mid < x) {
            lo = mid + 1;
        } else {
            hi = mid;
        }
    }
    if (lo * lo > x)
        lo -= 1;
    return lo;
}
