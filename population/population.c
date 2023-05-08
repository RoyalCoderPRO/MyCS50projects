#include <cs50.h>
#include <stdio.h>
int start(void);
int end(int n);

int main(void)
{

    int start_num = start();
    int end_num = end(start_num);
    int year_num = year(start_num, end_num);
    printf("Years: %i\n", year_num);

    // TODO: Calculate number of years until we reach threshold

}

int start(void){
    int start;
    do {
    start = get_int("Start size: ");
    }
    while (start < 9);
    return start;
}

int end(int n){
    int end;
    do
    {
        end = get_int("End size: ");
    }
    while (end < n);
    return end;
}

int year(int population, int end){
    int year;
    do
    {
        population = int (population / 4) - int (population / 3);
        year ++;
    }
    while(population < end);
    return year;
}