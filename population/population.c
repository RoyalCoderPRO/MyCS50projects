#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size
    int start = start()
    int end = end()
    // TODO: Prompt for end size

    // TODO: Calculate number of years until we reach threshold

    // TODO: Print number of years
}

int start(void){
    do {
    int start = get_int("Start size: ");
    }
    while (start < 9);
    return start
}

int end(int n){
    do {
    int end = get_int("End size: ");
    }
    while (end < n)
    return end
}

