#include <string.h>

static const int days_passed[] = {0,31,59,90,120,151,181,212,243,273,304,334};

int dayOfYear(char* date) {
    int y, m, d, doy;
    if (!date || strlen(date) < 9)
        return -1;
    y = (date[0] - '0') * 1000 + (date[1] - '0') * 100 + 
	    (date[2] - '0') * 10 + 
	    (date[3] - '0');
    m = (date[5] - '0') * 10 + (date[6] - '0');
    d = (date[8] - '0') * 10 + (date[9] - '0');
    doy = days_passed[m - 1] + d;
    if (m > 2 && ((y % 4 == 0 && y % 100 != 0) || y % 400 == 0))
        doy++;
    return doy;
}
