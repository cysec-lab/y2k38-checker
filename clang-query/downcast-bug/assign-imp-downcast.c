#include <limits.h>
#include <stdio.h>
#include <time.h>

time_t time_func(int n) { return (time_t)INT_MAX + n; }

void assignDirectly() {
    time_t t = time_func(1);  // -Winteger-overflow
    // printf("assigned directly: time_t: %ld\n", t);
    int i = t;  // -Wshorten-64-to-32
    printf("assigned directly: int: %d\n", i);
}

int assignWithArithmetic() {
    time_t t = time_func(3602);
    int i = t - (t % 3600);  // -Wshorten-64-to-32
    if (i < 0) {
        puts("overflowed !!!");
    }
}

int main(void) {
    assignDirectly();
    assignWithArithmetic();

    return 0;
}