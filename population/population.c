#include <cs50.h>
#include <stdio.h>
int start(void);
int end(int n);

int main(void)
{

    int start = start();
    int end = end(start);


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

int year(int start, int end){
    int year;
    int population;
    do
    {
        population = population / 4 - population / 3
        year ++;
    }
    while()
}