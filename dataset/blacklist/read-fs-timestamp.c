#include <stdio.h>
#include <sys/stat.h>
#include <sys/types.h>

int main(void) {
    struct stat buf;

    if (stat("../test.txt", &buf) == 0) {
        printf("%ld\n", buf.st_atime);  // MATCH
        printf("%ld\n", buf.st_mtime);  // MATCH
        printf("%ld\n", buf.st_ctime);  // MATCH
    };

    return 0;
}