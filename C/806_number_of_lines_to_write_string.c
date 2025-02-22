/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* numberOfLines(int* widths, int widthsSize, char* s, int* returnSize) {
    size_t i;
    int *output;

    output = calloc(2, sizeof(int));
    if (!output) {
        *returnSize = 0;
        return NULL;
    }
    *returnSize = 2;

    output[0] = 1;
    while (*s) { 
        i = *s - 'a';
        if (output[1] + widths[i] > 100) {
            output[1] = 0;
            output[0] += 1;
        }
        output[1] += widths[i];
        ++s;
    }
    return output;
}
