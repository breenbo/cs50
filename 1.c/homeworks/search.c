#include <stdio.h>
#include <stdlib.h> //use of atoi
#include <stdbool.h> //use of bool

bool search(int value, int values[], int n);

int main(int argc, char *argv[])
{
    if (argc !=2)
    {
        printf("usage : ./search n\n");
        return 1;
    }

    printf("Enter value to find: ");
    int value = atoi(argv[1]);
    int values[] = {1,2,3,4,5,6,7,8,9};

    search(value, values, 9);
    return 0;
}

bool search(int value, int values[], int n)
{
    // TODO: implement a searching algo - dichotomie
    int start = 0, end = n-1;
    // protect against infinite loop
    int count = 0;

    while (true)
    {

        // define the middle of the array and sub-arrayx
        int k = (start+end)/2;
        // check if empty sub-array
        if (start > end)
        {
            printf("Value not in array\n");
            return false;
        }

        // check the value of the middle
        if (values[k] == value)
        {
            printf("Found you in rank %i!\n", k);
            return true;
        } else if (values[k] > value)
        {
            printf("%i\n",k);
            printf("too big\n");
            // reduce array : change end because value < middle
            end = k - 1 ;
            count ++;
        } else if (values[k] < value)
        {
            printf("%i\n",k);
            printf("too small\n");
            // reduce array : change start because value > middle
            start = k + 1 ;
            count ++;
        }

        if (count==20)
        {
            printf("infinite loop\n");
            return false;
        }
    }
    return false ;
}
