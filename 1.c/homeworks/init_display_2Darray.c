#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("usage: ./init n\n");
        return 1;
    }
    int d = atoi(argv[1]);
    int init[d][d];

    // create the common part of array
    // initiate the maximum value
    int value = d * d - 1;

    // loop through rows
    for (int i=0; i<d; i++)
    {
        // loop through columns
        for (int j=0; j<d; j++)
        {
            init[i][j] = value;
            value --;
        }
    }

    init[3][3] = 10;
    printf("%i\n", init[3][3]);

    // print array to check is content
    for (int k=0; k<d; k++)
    {
        for (int l=0; l<d; l++)
        {
            printf("[%2i] ", init[k][l]);
        }
        printf("\n");
    }
}
