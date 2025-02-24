#include <stdbool.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

bool isPalindrome(char* s) {
    char *start, *end;

    if (!s || !(*s))
        return true;
    start = s;
    end = s + strlen(s);
    while (start < end) {
        if (!isalnum(*start)) {
            start++;
	    continue;
	}
	if (!isalnum(*end)) {
            end--;
	    continue;
	}
	if (tolower(*start) != tolower(*end))
            return false;
	start++;
	end--;
    }
    return true;
}

int main(int argc, char **argv) {
    bool res;
    char *vects[] = {"", " ", NULL, " A bC1dD1cB   a ", "1 2  3 abC  cB A32 1"};

    for (int i = 0; i < sizeof(vects) / sizeof(vects[0]); i++) {
        res = isPalindrome(vects[i]);
        printf("\'%s\' %d\n", vects[i], res);
    }
    return 0;
}
