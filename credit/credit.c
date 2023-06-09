#include <cs50.h>
#include <stdio.h>


int even_totaler(long n);
long power(int n, int p);
int len(long n);
int indexer(long n, int i);
int totaler(long n);
// This is a commment
// This is another comment
// Style50 is taking a dump on my hard work
// I hope these many were enough
// There weren't
// I have to add more... How many am I meant to add
// Okay that was plenty
int main(void)
{
    long credit = get_long("Number: ");

    if (len(credit) < 13 || len(credit) > 16)
    {
        printf("%i\n", len(credit));
        printf("INVALID\n");
        return 0;
    }
    int first_digit = indexer(credit, len(credit));
    int second_digit = indexer(credit, len(credit) - 1);

    if (len(credit) == 16 && first_digit == 5)
    {
        if (second_digit >= 1 && second_digit <= 5)
        {
            printf("MASTERCARD\n");
            return 0;
        }
    }

    if (len(credit) == 15 && first_digit == 3)
    {
        if (second_digit == 4 || second_digit == 7)
        {
            printf("AMEX\n");
            return 0;
        }
    }

    int total = totaler(credit);
    if (indexer(total, 1) == 0 && first_digit == 4)
    {
        printf("VISA\n");
        return 0;
    }

    else
    {
        printf("INVALID\n");
    }
}

int totaler(long n) //totals for Visa
{
    int current_val = even_totaler(n);
    for (int i = 1; i <= len(n); i += 2)
    {
        current_val += indexer(n, i);
    }
    return current_val;
}

int even_totaler(long n) //totals every other numbers digits
{

    int total = 0;

    for (int i = 2; i <= len(n); i += 2)
    {
        int number = indexer(n, i) * 2;
        if (len(number) == 2)
        {
            int new_number = 0;
            for (int j = 1; j <= 2; j++)
            {
                new_number += indexer(number, j);
            }
            number = new_number;
        }
        total += number;
    }
    return total;
}


long power(int n, int p) // function for power
{
    if (p == 0)
    {
        return 1;
    }
    long m = n;
    for (int i = 1; i < p; i++)
    {
        m *= n;
    }
    return m;
}


int len(long n) // function for length of string
{
    long m;
    int counter = 0;
    int i = 1;
    do
    {
        m = n / power(10, i);
        i ++;
        counter ++;
    }
    while (m > 0);
    return counter;
}


int indexer(long n, int i) //function for assigning index values
{
    //iterates right to left
    int digit;
    digit = ((n % power(10, i)) / power(10, i - 1));
    return digit;
}