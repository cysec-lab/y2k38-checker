#include <stdio.h>
#include <sys/stat.h>

int throwExplicitlyDowncast() {
    struct stat stat_buf;
    if (stat("a.c", &stat_buf) == 0) {
        return (int)stat_buf.st_atime;
    }
    return -1;
}