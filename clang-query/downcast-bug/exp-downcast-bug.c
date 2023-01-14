#include <limits.h>
#include <sys/stat.h>
#include <time.h>

void explicitlyDowncast() {
    time_t t = INT_MAX + 1;
    // 本来はここに範囲チェックを入れべき
    int i = (int)t;  // エラーにならない
    printf("%d\n", i);
    // -2147483648
}

void downcastSttime() {
    struct stat stat_buf;
    if (stat("a.c", &stat_buf) == 0) {
        printf("%d\n", stat_buf.st_atime);
        printf("%d\n", stat_buf.st_atime);
    }
}

int main(void) {
    explicitlyDowncast();
    // downcastSttime();
    return 0;
}