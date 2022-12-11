#include <stdio.h>
#include <cs50.h>
#include <string.h>


int main(void)
{
    int key = get_int("KEY: ");
    string s = get_string("Plain Text: ");
    printf("CipherText: ");
    for (int i=0; i < strlen(s); i++)
    {
        if (s[i]== 32 || s[i] ==44 )
        {
            printf("%c", s[i]);
        }
        else if (s[i] >= 97 && s[i] <= 122)
        {
            int new = s[i] + key;
            if (new > 122)
            {
                new = new - 122;
                s[i] = 96 + new;
                printf("%c", s[i]);
            }
            else
            {
               s[i] += key;
               printf("%c", s[i]);
            }
        }
        else if (s[i] >= 65 && s[i] <= 90)
        {
            int new = s[i] + key;
            if (new > 90)
            {
                new = new - 90;
                s[i] = 64 + new;
                printf("%c", s[i]);
            }
            else
            {
               s[i] += key;
               printf("%c", s[i]);
            }
        }
    }
    printf("\n");

}
