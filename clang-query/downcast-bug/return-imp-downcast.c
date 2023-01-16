#include <limits.h>
#include <math.h>
#include <stdio.h>
#include <sys/stat.h>
#include <sys/time.h>
#include <sys/types.h>
#include <time.h>

int f1() {
    time_t timestamp_2038 = (time_t)INT_MAX + 1;
    // 本来はここに範囲チェックを入れべき
    return timestamp_2038;
}

int f2() {
    time_t timestamp_2038 = (time_t)INT_MAX + 1;
    time_t t = timestamp_2038 + 100;
    // 本来はここに範囲チェックを入れべき
    return t - (t % 2);
}

int no_match1() {
    long l = INT_MAX + 1;
    return l;
}
int no_match2() {
    long l = INT_MAX + 1;
    return l - (l % 2);
}

int main(void) {
    printf("%d\n", f1());
    printf("%d\n", f2());

    return 0;
}
