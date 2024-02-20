//////////////////////////|
//|File: rocket.c
//|Author: Jerrin C. Redmon
//|Language: C
//|Version: 1.0
//|Date: Febuary 6, 2023
//////////////////////////|

#include <stdio.h>
#include <time.h>

//Rocket ASCII
 const char *rocket = "\n\
                            /\\ \n\
                           /  \\ \n\
                          /    \\ \n\
                         /      \\ \n\
                         |______|\n\
                         |      |\n\
                         |      |\n\
                         |    N |\n\
                         |    A |\n\
                         |    S |\n\
                         |    A |\n\
                         |      |\n\
                         |      |\n\
                         |      |\n\
                         |      |\n\
                         |      |\n\
                        /|      |\\ \n\
                       /||      ||\\ \n\
                      /|||______|||\\ \n\
                           \\\\\\\\\\ \n\
                           /////";

int main(){
    printf("\x1b[2J%s\n", rocket);
    for (int i = 0; i < 30; i++) {
        struct timespec start_tp, end_tp;
        clock_gettime(CLOCK_MONOTONIC, &start_tp);
        end_tp = start_tp;
        double start_time = start_tp.tv_sec + start_tp.tv_nsec / 1000000000.0;
        double end_time = start_time;
        while (end_time < start_time + 0.1) {
            clock_gettime(CLOCK_MONOTONIC, &end_tp);
            end_time = end_tp.tv_sec + end_tp.tv_nsec / 1000000000.0;
        }
        putchar('\n');
    }
    return 0;
}
