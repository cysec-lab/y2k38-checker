#include <sys/types.h>
#include <utime.h>

int utime(const char *filename, const struct utimbuf *times);

#include <sys/time.h>

int utimes(const char *filename, const struct timeval times[2]);

int main(void) {
    struct utimbuf buf = {
        .actime = 0x7fffffff,
        .modtime = 0x7fffffff,
    };

    utime("../test.txt", &buf);  // MATCH

    utimes("../test.txt", &buf);  // MATCH

    return 0;
}