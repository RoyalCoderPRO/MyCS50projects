#include <stdio.h>
#include <cs50.h>
// importing packages
int main(void) //no parameters
{
    string name = get_string("What's your name? "); //asks for user name input
    printf("hello, %s\n", name); //concatenates and prints hello and user name
}