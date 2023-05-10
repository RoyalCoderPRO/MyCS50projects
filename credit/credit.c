#include <cs50.h>
#include <stdio.h>


int totaler(long n);
long power(int n, int p);
int digit(int n);
int iterator(long n, int i);


int main(void)
{
    long credit = get_long("Number: ");
    int total = totaler(credit);
    printf("%i\n", total);
}

int totaler(long n)
{
    //4003600000000014
    int total = 0;

    for (int i=2;i<=16;i+=2)
    {
        total += iterator(n, i);
        if (digit(total)>1)
        {
            for (int i= 0; i< digit(total); i++)

            iterator(n,i);
        }
    }
    return total;
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
    do
    {
        int i = 1;
        m = n/power(10,i);
        i ++;
        counter ++;
    }
    while(m>0);
    return counter;
}

int iterator(long n, int i)
{
    int digit;
    digit = ((n % power(10, i)) / power(10,i-1));
    return digit;
}