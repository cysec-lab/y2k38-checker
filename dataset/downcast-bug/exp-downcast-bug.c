#include <limits.h>
#include <stdio.h>
#include <time.h>

long LONG = (long)INT_MAX + 1;
time_t TIMET = (time_t)INT_MAX + 1;

time_t return_timet_func() { return TIMET; }
long return_long_func() { return LONG; }

long timet_to_long(time_t t) { return (long)t; }
long timet_to_timet(time_t t) { return t; }

void matched() {
    // 直接代入
    printf("%d\n", (int)TIMET);  // MATCH 1

    // 演算結果を代入
    printf("%d\n", (int)(1 + (TIMET + 2)));  // MATCH 2 // FIXME* match しない
    printf("%d\n", (int)(1 + return_timet_func()));  // MATCH 3

    // long を明示的キャスト
    printf("%d\n", (int)(time_t)LONG);                // MATCH 4
    printf("%d\n", (int)(time_t)return_long_func());  // MATCH 5

    // time_t を返す関数の返り値を代入
    printf("%d\n", (int)return_timet_func());  // MATCH 6
}

void no_matched() {
    // 直接代入
    printf("%d\n", (int)LONG);     // long  -> int
    printf("%ld\n", (long)TIMET);  // time_t -> long

    // 演算結果を代入
    printf("%d\n", (int)(1 + (LONG + 2)));  // long  -> int
    printf("%d\n",
           (int)(1 + timet_to_long(TIMET)));           // long  -> int
    printf("%ld\n", (long)(1 + (TIMET + 2)));          // time_t -> long
    printf("%ld\n", (long)(1 + return_timet_func()));  // time_t -> long

    // long を明示的キャスト
    printf("%d\n", (int)(long)1);      // long  -> int
    printf("%ld\n", (long)(time_t)1);  // time_t -> long

    // time_t を返す関数の返り値を代入
    printf("%d\n", (int)return_long_func());     // long  -> int
    printf("%ld\n", (long)return_timet_func());  // time_t -> long
}

int main(void) {
    matched();
    return 0;
}