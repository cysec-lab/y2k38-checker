#include <limits.h>
#include <stdio.h>
#include <time.h>

long LONG = (long)INT_MAX + 1;
time_t TIMET = (time_t)INT_MAX + 1;

time_t return_timet_func() { return TIMET; }
long return_long_func() { return LONG; }

long timet_to_long(time_t t) { return (long)t; }

// time_t -> int
int time_t_to_int(int type) {
    return TIMET;
    return 1 + (TIMET + 2);
    return 1 + return_timet_func();
    return (time_t)LONG;
    return (time_t)return_long_func();
    return return_timet_func();
}

// time_t -> long
long time_t_to_long() {
    return TIMET;
    return 1 + (TIMET + 2);
    return 1 + return_timet_func();
    return (time_t)LONG;
    return (time_t)return_long_func();
    return return_timet_func();
}

// long -> int
int no_matched_long_to_int() {
    return LONG;
    return 1 + (LONG + 2);
    return 1 + timet_to_long(TIMET);
    return (long)1;
    return return_long_func();
}

// time_t -> long long
long long no_matched_int_to_long() {
    return TIMET;
    return 1 + (TIMET % 2);
    return 1 + return_timet_func();
    return (time_t)1;
    return return_timet_func();
}

int main(void) { return 0; }