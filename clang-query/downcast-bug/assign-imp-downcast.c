#include <limits.h>
#include <stdio.h>
#include <time.h>

void assign_directly() {
    time_t t = INT_MAX + 1;  // -Winteger-overflow
    int i = t;               // -Wshorten-64-to-32
    printf("assigned directly: int: %d\n", i);
}

int assign_with_arithmetic() {
    time_t t = INT_MAX + 3602;
    int i = t - (t % 3600);  // -Wshorten-64-to-32
    if (i < 0) {
        puts("overflowed !!!");
    }
}

void no_matched() {
    long t = INT_MAX + 1;
    int i1 = t - (t % 3600);
    int i2 = t - (t % 3600);
}

int main(void) {
    assign_directly();
    assign_with_arithmetic();

    return 0;
}