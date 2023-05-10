#include <cs50.h>
#include <stdio.h>


int totaler(long n);
long power(int n, int p);
int digit(long n);
int indexer(long n, int i);


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

    for (int i=2;i<=digit(n);i+=2)
    {
        int number = indexer(n, i)*2;
        printf("%i\n", number);
        if (digit(number)==2)
        {
            for (int j= 1; j <= 2; j++)
                {
                number += indexer(number,j);
                }
        }
        total += number;
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


int digit(long n)
{
    long m;
    int counter = 0;
    int i = 1;
    do
    {
        m = n/power(10,i);
        i ++;
        counter ++;
    }
    while(m>0);
    printf("%)
    return counter;
}


int indexer(long n, int i)
{
    int digit;
    digit = ((n % power(10, i)) / power(10,i-1));
    return digit;
}