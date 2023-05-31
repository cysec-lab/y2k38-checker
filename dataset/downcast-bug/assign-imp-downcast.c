#include <limits.h>
#include <stdio.h>
#include <time.h>

long LONG = (long)INT_MAX + 1;
time_t TIMET = (time_t)INT_MAX + 1;

time_t return_timet_func() { return TIMET; }
long return_long_func() { return LONG; }

long timet_to_long(time_t t) { return (long)t; }

void time_t_to_int() {
    int i = 1 + (TIMET * 2) % 3600;
    int i = return_timet_func();
    int i = 1 + return_timet_func();
    int i = (time_t)(INT_MAX + 1);
    i *= TIMET;
    i += TIMET;
}

void time_t_to_long() {
    long i = 1 + (TIMET * 2) % 3600;
    long i = return_timet_func();
    long i = 1 + return_timet_func();
    long i = (time_t)(INT_MAX + 1);
    i *= TIMET;
    i += TIMET;
}

void no_matched() {
    int i = return_long_func();
    int i = LONG_MAX;
    int i2 = 1 + timet_to_long(TIMET);
    int i = LONG;
    int i1 = 1 + (LONG + 2);
}

int main(void) { return 0; }
