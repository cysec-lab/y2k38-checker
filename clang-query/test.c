#include <math.h>
#include <stdio.h>
#include <sys/stat.h>
#include <sys/time.h>
#include <sys/types.h>
#include <time.h>
#include <utime.h>

void referFileTimeStamp() {
    struct stat statBuf;
    if (stat("a.c", &statBuf) == 0) {
        printf("%ld\n", statBuf.st_atime);
        printf("%ld\n", statBuf.st_mtime);
        printf("%ld\n", statBuf.st_ctime);
    }
}

int throwExplicitlyDowncast() {
    struct stat stat_buf;
    if (stat("a.c", &stat_buf) == 0) {
        return (int)stat_buf.st_atime;
    }
    return -1;
}

int throwImplicitlyDowncast() {
    time_t t = pow(2, 32);
    int overflowed = t - (t % 3600);
    // double not_overflowed = difftime(t, t % 3600);
    return overflowed;
}

void writeFileTimestamp() {
    time_t actime = 0x7fffffff;
    time_t modtime = 0x7fffffff;

    struct utimbuf ubuf = {actime, modtime};
    utime("a.txt", &ubuf);
    utimes("a.txt", &ubuf);
}

int main(void) {
    referFileTimeStamp();
    throwExplicitlyDowncast();
    throwImplicitlyDowncast();
    writeFileTimestamp();

    return 0;
}
