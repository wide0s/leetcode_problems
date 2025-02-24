#include <stdbool.h>
#include <stdio.h>

bool isNumber(char* s) {
    bool exp, dot;
    int digidx, x, fsm_state;
    bool signs[] = {false, false};
    int digits[] = {0, 0};

    if (!s || !(*s))
        return false;
    exp = false;
    dot = false;
    fsm_state = 0; /* 0 - sign state (initial), 1 - number state */
    digidx = 0;
    while (*s) {
        x = *s - '0';
        if (fsm_state) {
            if (!exp && (*s == 'e' || *s == 'E')) {
                exp = true;
                digidx = 1;
                dot = true; /* exponent is always an integer */
                fsm_state = 0; /* return back to the 'sign' state */
            } else if (!dot && *s == '.') {
                dot = true;
            } else if (x >= 0 && x < 10) {
                digits[digidx] += 1;
            } else
                return false;
        } else {
            if (*s == '-' || *s == '+') {
                signs[digidx] = true;
                fsm_state = 1;
            } else if (x >= 0 && x < 10) {
                digits[digidx] += 1;
                fsm_state = 1;
            } else if (!dot && *s == '.') {
                dot = true;
                fsm_state = 1;
            } else
                return false;
        }
        s++;
    }
    if ((exp && !digits[1]) || (dot && !digits[0]) || (signs[0] && !digits[0]))
        return false;
    return true;
}

int main(int argc, char **argv) {
     bool res;
     char *vect[] = {NULL, "", " ", ".", "+", "-", "e", "e1", "e-", "+e2", "1.0e+5", "1.0", "1", "-232", "1212.2e4", "4.66E-5"};

     for (int i = 0; i < sizeof(vect) / sizeof(vect[0]); i++) {
         res = isNumber(vect[i]);
	 printf("'%s' %d\n", vect[i], res);
     }
     return 0;
}
