#include <stdlib.h>
#include <string.h>
#include <stdio.h>

char* baseNeg2(int n) {
    int r, pos;
    char *buf, c;

    buf = (char *)calloc(2, 1);
    if (!buf)
        return NULL;

    if (n == 0) {
        buf[0] = '0';
        return buf;
    }

    pos = 0;
    while (n) {
        r = n % (-2);
        n /= -2;
        if (r < 0) {
            n++;
            r += 2;
        }
        buf = realloc(buf, pos + 2);
        if (!buf)
            return NULL;
        buf[pos++] = r + '0';
    }
    buf[pos] = 0;

    /* reverse string */
    r = 0;
    pos--;
    while (r < pos) {
        c = buf[r];
	buf[r] = buf[pos];
	buf[pos] = c;
	r++;
	pos--;
    }
    return buf;
}

int main(int argc, char **argv) {
    char *ptr;
    int i;

    for (i = 0; i < 1025; i++) {
        ptr = baseNeg2(i);
	if (ptr) {
            printf("%d is %s\n", i, ptr);
	    free(ptr);
	}
    }

    return 0;
}
