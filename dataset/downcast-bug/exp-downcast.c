#include <limits.h>
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

long LONG = (long)INT_MAX + 1;
time_t TIMET = (time_t)INT_MAX + 1;

time_t return_timet_func() { return TIMET; }
long return_long_func() { return LONG; }

long timet_to_long(time_t t) { return (long)t; }
long timet_to_timet(time_t t) { return t; }

void time_t_to_int() {
    printf("%d\n", (int)++TIMET);
    printf("%d\n", (int)time(NULL));
    printf("%d\n", (int)time(0));
    printf("%d\n", (int)(time_t)LONG);
    printf("%d\n", (int)(1 + ((((TIMET++))) + 2)));
    printf("%d\n", (int)(1 + ((((++TIMET))) + 2)));
    printf("%d\n", (int)(time_t)return_long_func());
    printf("%d\n", (int)((1 + return_timet_func())));
    printf("%d\n", (int)((1 + return_timet_func())));
}

void time_t_to_long() {
    printf("%ld\n", (long)++TIMET);
    printf("%ld\n", (long)(time_t)1);
    printf("%ld\n", (long)(1 + ((((TIMET))) + 2)));
    printf("%ld\n", (long)(1 + return_timet_func()));
    printf("%ld\n", (long)(1 + return_timet_func()));
}

void no_matched() {
    printf("%d\n", (int)++LONG);
    printf("%d\n", (int)(long)1);
    printf("%d\n", (int)(1 + (LONG++ + 2)));
    printf("%d\n", (int)return_long_func());
    printf("%d\n", (int)(1 + timet_to_long(TIMET)));
}

int main() {
    to_int();
    return 0;
}
