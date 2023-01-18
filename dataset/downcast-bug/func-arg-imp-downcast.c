#include <limits.h>
#include <stdio.h>
#include <time.h>

long LONG = (long)INT_MAX + 1;
time_t TIMET = (time_t)INT_MAX + 1;

time_t return_timet_func() { return TIMET; }
long return_long_func() { return LONG; }

long timet_to_long(time_t t) { return (long)t; }

// 検査対象関数
int int_arg_func(int n) {
    printf("%d\n", n);
    return 0;
}
void long_arg_func(long t) {}

void matched() {
    // 直接代入
    int_arg_func(TIMET);  // Potential Overflow 1

    // 演算結果を代入
    int_arg_func(1 + (TIMET + 2));          // Potential Overflow 2
    int_arg_func(1 + return_timet_func());  // Potential Overflow 3

    // long を明示的キャスト
    int_arg_func((time_t)LONG);                // Potential Overflow 4
    int_arg_func((time_t)return_long_func());  // Potential Overflow 5

    // time_t を返す関数の返り値を代入
    int_arg_func(return_timet_func());  // Potential Overflow 6

    // ネストされた関数 // FIXME: match されるように
    printf("%d\n", int_arg_func(1 + return_timet_func()));  // Potential Overflow 7
}

void no_matched() {
    // 直接代入
    int_arg_func(LONG);    // long -> int
    long_arg_func(TIMET);  // time_t -> long

    // 演算結果を代入
    int_arg_func(1 + (LONG + 2));            // long -> int
    int_arg_func(1 + timet_to_long(TIMET));  // long -> int
    long_arg_func(1 + (TIMET + 2));          // time_t -> long
    long_arg_func(1 + return_timet_func());  // time_t -> long

    // long を明示的キャスト
    int_arg_func((long)1);     // long -> int
    long_arg_func((time_t)1);  // time_t -> long

    // time_t を返す関数の返り値を代入
    int_arg_func(return_long_func());    // long -> int
    long_arg_func(return_timet_func());  // time_t -> long
}

int main(void) {
    matched();
    return 0;
}
