#include <limits.h>
#include <stdio.h>
#include <time.h>

long LONG = (long)INT_MAX + 1;
time_t TIMET = (time_t)INT_MAX + 1;

time_t return_timet_func() { return TIMET; }
long return_long_func() { return LONG; }

long timet_to_long(time_t t) { return (long)t; }

// 検査対象関数
void int_arg_func(int n) {
    printf("%d\n", n);
    return;
}
void long_arg_func(long t) {
    printf("%ld\n", t);
    return;
}

void time_t_to_int() {
    int_arg_func(TIMET);
    int_arg_func(1 + (TIMET * 2));
    int_arg_func(1 + return_timet_func());
    int_arg_func((time_t)LONG);
    int_arg_func((time_t)return_long_func());
    int_arg_func(return_timet_func());
}
void time_t_to_long() {
    long_arg_func(TIMET);
    long_arg_func(1 + (TIMET * 2));
    long_arg_func(1 + return_timet_func());
    long_arg_func((time_t)LONG);
    long_arg_func((time_t)return_long_func());
    long_arg_func(return_timet_func());
}

void no_matched() {
    int_arg_func(LONG);
    int_arg_func(1 + (LONG + 2));
    int_arg_func(1 + timet_to_long(TIMET));
    int_arg_func((long)1);
    int_arg_func(return_long_func());
}

int main(void) {
    matched();
    return 0;
}
