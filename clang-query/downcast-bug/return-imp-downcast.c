#include <limits.h>
#include <stdio.h>
#include <time.h>

long LONG = (long)INT_MAX + 1;
time_t TIMET = (time_t)INT_MAX + 1;

time_t return_timet_func() { return TIMET; }
long return_long_func() { return LONG; }

long timet_to_long(time_t t) { return (long)t; }

int matched(int type) {
    // 直接代入
    if (type == 0) return TIMET;  // MATCH 1

    // 演算結果を代入
    if (type == 1) return 1 + (TIMET + 2);          // MATCH 2
    if (type == 2) return 1 + return_timet_func();  // MATCH 3

    // long を明示的キャスト
    if (type == 3) return (time_t)LONG;                // MATCH 4
    if (type == 4) return (time_t)return_long_func();  // MATCH 5

    // time_t を返す関数の返り値を代入
    if (type == 5) return return_timet_func();  // MATCH 6

    return 0;
}

int no_matched_long2int() {
    // 直接代入
    return LONG;  // long -> int

    // 演算結果を代入
    return 1 + (LONG + 2);            // long -> int
    return 1 + timet_to_long(TIMET);  // long -> int

    // long を明示的キャスト
    return (long)1;  // long -> int

    // time_t を返す関数の返り値を代入
    return return_long_func();  // long -> int
}

long no_matched_int2long() {
    // 直接代入
    return TIMET;  // time_t -> long

    // 演算結果を代入
    return 1 + (TIMET % 2);          // time_t -> long
    return 1 + return_timet_func();  // time_t -> long

    // long を明示的キャスト
    return (time_t)1;  // time_t -> long

    // time_t を返す関数の返り値を代入
    return return_timet_func();  // time_t -> long
}

int main(void) {
    for (int i = 0; i < 6; i++) {
        printf("%d\n", matched(i));
    }
    return 0;
}