#include <limits.h>
#include <math.h>
#include <stdio.h>
#include <sys/stat.h>
#include <sys/time.h>
#include <sys/types.h>
#include <time.h>

time_t timestamp_2038 = (time_t)INT_MAX + 1;

int f1() {
    // 本来はここに範囲チェックを入れべき
    return timestamp_2038;
}

int f2() {
    time_t t = timestamp_2038 + 100;
    // 本来はここに範囲チェックを入れべき
    return t - (t % 2);
}

int main(void) {
    printf("%d\n", f1());
    printf("%d\n", f2());

    return 0;
}
