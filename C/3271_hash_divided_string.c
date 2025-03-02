#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* stringHash(char* s, int k) {
    char *s2, *p;
    size_t n;
    int hash, i, j;

    if (!s || k < 1)
        return NULL;
    n = strlen(s);
    s2 = calloc(n / k + 1, sizeof(char));
    if (s2) {
        for (i = 0, p = s2; i < n; i += k, p++) {
            hash = 0;
            for (j = 0; j < k; j++)
                hash += s[i + j] - 'a';
            *p = hash % 26 + 'a';
        }
    }
    return s2;
}

int main(int argc, char **argv) {
    char *s;

    s = stringHash("abcd", 2);
    printf("abcd is %s\n", s);

    s = stringHash("mxz", 3);
    printf("mxz is %s\n", s);

    return 0;
}
