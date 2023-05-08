#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int height;
    do
    {
        height = get_int("Height: ");
    }
    while (height < 1 || height > 8);

    for (int i = 1; i <= height; i++)
    {
        int whitespace_counter = height - i;
        for (int j = 0; j < whitespace_counter; j++)
        {
            printf("  ");
        }
        for (int h = 0; h < i; h++)
        {
            printf("#");
        }
        printf(" ");
        for (int h = 0; h < i; h++)
        {
            printf("#");
        }
        for (int j = 0; j < whitespace_counter; j++)
        {
            printf(" ");
        }
        printf("\n");

    }


}