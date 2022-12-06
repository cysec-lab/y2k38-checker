#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <time.h>

int main(void) {
    struct stat stat_buf;

    if (stat("./example.txt", &stat_buf) == 0) {
        printf("st_atime: %ld \n", stat_buf.st_atime);
        printf("st_mtime: %ld \n", stat_buf.st_mtime);
        printf("st_ctime: %ld \n", stat_buf.st_ctime);
    } else {
        return EXIT_FAILURE;
    }

    return EXIT_SUCCESS;
}