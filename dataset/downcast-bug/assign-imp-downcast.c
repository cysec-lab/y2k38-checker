#include <limits.h>
#include <stdio.h>
#include <time.h>

long LONG = (long)INT_MAX + 1;
time_t TIMET = (time_t)INT_MAX + 1;

time_t return_timet_func() { return TIMET; }
long return_long_func() { return LONG; }

long timet_to_long(time_t t) { return (long)t; }

void matched() {
    int i = TIMET;
    int i = 1 + (TIMET + 2);
    int i = return_timet_func();

    i += TIMET;
    i *= TIMET;

    int i2 = 1 + return_timet_func();
    int i1 = (time_t)LONG;
    int i2 = (time_t)return_long_func();
}

void no_matched() {
    {
        // 直接代入
        int i = LONG;     // long -> int
        long l2 = TIMET;  // time_t -> long
    }
    {
        // 演算結果を代入
        int i1 = 1 + (LONG + 2);            // long -> int
        int i2 = 1 + timet_to_long(TIMET);  // long -> int
        long l2 = 1 + (TIMET % 2);          // time_t -> long
        long l3 = 1 + return_timet_func();  // time_t -> long
    }
    {
        // long を明示的キャスト
        int i = (long)1;      // long -> int
        long l1 = (time_t)1;  // time_t -> long
    }
    {
        // time_t を返す関数の返り値を代入
        int i = return_long_func();    // long -> int
        long l = return_timet_func();  // time_t -> long
    }
}

int main(void) {
    matched();

    return 0;
}
