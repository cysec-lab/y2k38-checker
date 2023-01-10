#include <sys/time.h>  // utimes()
#include <time.h>
#include <utime.h>  // utime()

void writeFileTimestamp() {
    time_t actime = 0x7fffffff;
    time_t modtime = 0x7fffffff;

    struct utimbuf ubuf = {actime, modtime};
    utime("a.txt", &ubuf);
    utimes("a.txt", &ubuf);
}

int main(void) {
    writeFileTimestamp();
    return 0;
}