#include <cs50.h>
#include <stdio.h>


int card_type(long n);
long power(int n, int p);
int digit(int n);


int main(void)
{
    long credit = get_long("Number: ");
    int total = card_type(credit);
    printf("%i\n", total);
}

int card_type(long n)
{
    //4003600000000014
    int evens = 0;

    for (int i=2;i<=16;i+=2)
    {
        evens_first += ((n % power(10, i)) / power(10,i-1));
        if(digit(evens_first<1))
        {
            
        }

    }
    return evens;
}

long power(int n, int p)
{
    if (p == 0)
    {
        return 1;
    }
    long m = n;
    for (int i=1; i<p; i++)
    {
        m *= n;
    }
    return m;
}

int digit(int n)
{
    int m;
    int counter = 0;
    for (int i= 1; m = 0 ;i++)
    {
        m = n/power(10,i);
        counter ++;
    }
    return counter;
}