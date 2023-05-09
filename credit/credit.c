#include <cs50.h>
#include <stdio.h>

int main(void)
{
    long credit = get_long("Number: ");
    printf("%s\n",card_type(credit));
}

string card_type(long n)
{
    //4003600000000014
    int evens = 0;
    for (i=1;i<16;i++)
    {
        evens += (n % (10*i)) - (n % 10*(i-1));
        printf("%i", evens);
    }
    return 
}