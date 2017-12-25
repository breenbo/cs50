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
    int init[d*d];

    if (d%2==0)
    {
        //1,2
        init[1] = 2;
        init[2] = 1;
    } else
    {
        //2,1
        init[1] = 1;
        init[2] = 2;
    }

    // create the common part of array
    init[0] = 0;
    for (int i=3; i<d*d; i++)
    {
        init[i] = i;
    }
    // print array to check is content
    printf("%7s%7s\n", "Index","Value");
    for (int k=0; k<d*d; k++)
    {
        printf("%7i%7i\n", k, init[k]);
    }
}
