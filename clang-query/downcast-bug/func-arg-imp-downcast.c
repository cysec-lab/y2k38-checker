#include <limits.h>
#include <math.h>
#include <stdio.h>
#include <sys/stat.h>
#include <sys/time.h>
#include <sys/types.h>
#include <time.h>

void timet_to_int(int n) {
    printf("%d\n", n);
    return;
}

int main(void) {
    time_t t = INT_MAX + 1;
    timet_to_int(t);
    timet_to_int((time_t)INT_MAX + 1);

    return 0;
}
