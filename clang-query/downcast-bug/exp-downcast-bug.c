#include <limits.h>
#include <sys/stat.h>
#include <time.h>

void explicitly_downcast() {
    time_t t = INT_MAX + 1;
    printf("%d\n", (int)t);
    printf("%d\n", (int)(t - (t % 2)));
}

void not_matched() {
    long l = INT_MAX + 1;
    printf("%d\n", (int)l);
    printf("%d\n", (int)(l - (l % 2)));
}

int main(void) {
    explicitly_downcast();
    // downcastSttime();
    return 0;
}