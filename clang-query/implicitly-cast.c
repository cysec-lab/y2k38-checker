#include <time.h>

int throwImplicitlyDowncast() {
    time_t t = pow(2, 32);
    int overflowed = t - (t % 3600);
    // double not_overflowed = difftime(t, t % 3600);
    return overflowed;
}

int main(void) {
    throwImplicitlyDowncast();
    return 0;
}