#include <sys/time.h>
#include <sys/types.h>
#include <utime.h>
#include <sys/stat.h>

int main(void) {
    struct utimbuf buf = {
        .actime = 0x7fffffff,
        .modtime = 0x7fffffff,
    };
    utime("./test.txt", &buf);  // Potential Overflow
    utimes("./test.txt", &buf);  // Potential Overflow
    utimenstat("./test.txt", &buf);  // Potential Overflow

    struct timeval tv = {
        .tv_sec = 0x7fffffff,
        .tv_usec = 0x7fffffff,
    };
    futimes(0, &tv);
    lutimes("./test.txt",  &tv);
    

    return 0;
}