#include <sys/time.h>
#include <sys/types.h>
#include <utime.h>

int main(void) {
    struct utimbuf buf = {
        .actime = 0x7fffffff,
        .modtime = 0x7fffffff,
    };

    utime("./test.txt", &buf);  // Potential Overflow

    utimes("./test.txt", &buf);  // Potential Overflow

    return 0;
}