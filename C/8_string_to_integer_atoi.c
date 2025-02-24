#include <stdlib.h>
#include <stdio.h>
#include <stdint.h>

int myAtoi(char* s) {
    int value;
    int sign, x, fsm_state;

    if (!s || !(*s))
        return 0;
    fsm_state = 0; /* 0 - sign, 1 - digits */
    sign = 1;
    value = 0;
    while (*s != '\0') {
        x = *s - '0';
        if (fsm_state == 1) {
            if (x < 0 || x > 9)
                break;
	    if (value > INT32_MAX / 10 || 
			    (value == INT32_MAX / 10 && x > INT32_MAX % 10)) {
                return sign < 0 ? INT32_MIN : INT32_MAX;
	    }
	    value = value * 10 + x;
        } else {
            if (*s == '-') {
                sign = -1;
                fsm_state = 1;
            } else if (*s == '+') {
                fsm_state = 1;
            } else if (x >= 0 && x <= 9) {
                value = x;
                fsm_state = 1;
            } else if (*s != ' ' && *s != '\t') {
                break;
            }
        }
        s++;
    }
    return sign < 0 ? -value : value;
}

int main(int argc, char **argv) {
    int value;
    char* vectors[] = {NULL, "", "  +5", "+1", " 3", " 42", "0", "2147483647", "2147483648",
	               "-0", "   -1", " -2", "-2147483648", "-2147483649", " 12 word", " -34 gr", "sdsds -45"};

    for (int i = 0; i < sizeof(vectors) / sizeof(vectors[0]); i++) {
	    value = myAtoi(vectors[i]);
	    printf("'%s' is %d\n", vectors[i], value);
    }

    return 0;
}
