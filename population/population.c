#include <cs50.h>
#include <stdio.h>

int start(void);
int end(int n);
int year(int population, int end);
int main(void)
{

    int start_num = start();
    int end_num = end(start_num);
    int year_num = year(start_num, end_num);
    printf("Years: %i\n", year_num);

}

int start(void)
{
    int start;
    do
    {
        start = get_int("Start size: ");
    }
    while (start < 9);
    return start;
}

int end(int n)
{

    int end;
    do
    {
        end = get_int("End size: ");
    }
    while (end < n);

    return end;
}

int year(int population, int end){
    int current = 0;
    while (population <= end)
    {
        int born = (int) population / 3;
        int dead = (int) population / 4;
        population = population + born - dead;
        current += 1;
    }

    return current;
}