#include <stdio.h>
#include <sys/stat.h>
#include <sys/types.h>

int main(void) {
    struct stat buf;

    if (stat("../test.txt", &buf) == 0) {
        printf("%ld\n", buf.st_atime);  // Potential Overflow
        printf("%ld\n", buf.st_mtime);  // Potential Overflow
        printf("%ld\n", buf.st_ctime);  // Potential Overflow
    };

    return 0;
}