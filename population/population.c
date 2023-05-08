#include <cs50.h>
#include <stdio.h>

int main(void)
{

    int start = start();
    int end = end(start);


    // TODO: Calculate number of years until we reach threshold
    
}

int start(void){
    do {
    int start = get_int("Start size: ");
    }
    while (start < 9);
    return start;
}

int end(int n){
    do {
    int end = get_int("End size: ");
    }
    while (end < n);
    return end;
}

