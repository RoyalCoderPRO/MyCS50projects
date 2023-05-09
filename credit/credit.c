#include <cs50.h>
#include <stdio.h>

string card_type(long n);
int main(void)
{
    long credit = get_long("Number: ");
    string word = card_type(credit);
    printf("%s\n", word);
}

string card_type(long n)
{
    //4003600000000014
    int evens = 0;

    for (int i=2;i<16;i+=2)
    {
        evens += (n % (10*i));
        printf("%i\n", evens);
    }
    string hi = "hi";
    return hi;
}