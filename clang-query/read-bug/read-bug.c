#include <sys/stat.h>

void referFileTimeStamp() {
    struct stat statBuf;
    if (stat("a.c", &statBuf) == 0) {
        printf("%ld\n", statBuf.st_atime);
        printf("%ld\n", statBuf.st_mtime);
        printf("%ld\n", statBuf.st_ctime);
        printf("%ld\n", statBuf.st_mode);  // st_[amc]time 以外はマッチされない
    }
}
