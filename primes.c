////////////////////////////|
//|File: primes.c
//|Author: Jerrin C. Redmon
//|Language: C
//|Version: 1.0
//|Date: August 28, 2023
////////////////////////////|

/*
 * Description:
 * a sieve of eratosthenes
 */

// Includes //
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

// Main //
int main(int argc, char *argv[]) {

    int n = atoi(argv[1]);
    bool *a = malloc((n + 1) * sizeof(*a));
    memset(a, 1, n + 1);

    for (int i = 2; i <= sqrt(n); i++) {
        if (a[i]) {
            for (int p = i * i; p <= n; p += i) {
                a[p] = 0;
            }
        }
    }
    
    for (int i = 2; i <=n; i++) {
        if (a[i]) {
            printf("%d,",i);
        }
    }
}
