#include <cs50.h>
#include <stdio.h>

int main(void){
    float x = get_float("Change owed: ");
    int count = 0;
    while (x >= 0.25){
        x -= 0.25;
        count += 1;
        // printf("%d", count);
    }
    while (x >= 0.10){
        x -= 0.10;
        count += 1;
    }
    while (x >= 0.05){
        x -= 0.05;
        count += 1;
    }
    while (x > 0){
        x -= 0.01;
        count += 1;
    }
    printf("%d", count);
    printf("\n");
}
