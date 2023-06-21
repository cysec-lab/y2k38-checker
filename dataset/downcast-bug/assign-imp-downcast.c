#include <limits.h>
#include <stdio.h>
#include <time.h>

long LONG = (long)INT_MAX + 1;
time_t TIMET = (time_t)INT_MAX + 1;

time_t return_timet_func() { return TIMET; }
long return_long_func() { return LONG; }

long timet_to_long(time_t t) { return (long)t; }

void time_t_to_int() {
    int i1 = 1 + (TIMET * 2) % 3600;
    int i2 = return_timet_func();
    int i3 = 1 + return_timet_func();
    int i4 = (time_t)(INT_MAX + 1);
    i1 *= TIMET;
    i1 += TIMET;
}

void time_t_to_long() {
    long i1 = 1 + (TIMET * 2) % 3600;
    long i2 = return_timet_func();
    long i3 = 1 + return_timet_func();
    long i4 = (time_t)(INT_MAX + 1);
    i1 *= TIMET;
    i1 += TIMET;
}

void no_matched() {
    int i1 = 1 + (LONG + 2);
    int i2 = return_long_func();
    int i3 = LONG_MAX;
    int i4 = 1 + timet_to_long(TIMET);
    int i5 = LONG;
}

int main(void) { return 0; }
