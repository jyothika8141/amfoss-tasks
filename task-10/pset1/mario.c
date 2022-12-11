#include <cs50.h>
#include <stdio.h>

int main(void){
    while (true){
        int x = get_int("Height: ");
        int y = x;
        if (1 <= x && x<= 8)
        {
            for (int i = 1; i <= x; i++ )
            {
                for (int j = y-1; j >= 0; j--)
                {
                    printf(" ");
                }
                for (int k = 1; k <= i; k++)
                {
                    printf("#");
                }
                printf(" ");
                for (int l = 1; l <= i; l++)
                {
                    printf("#");
                }
                printf("\n");
                y--;
            }
            break;
        }
    }
}
