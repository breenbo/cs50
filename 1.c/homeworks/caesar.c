#include <stdio.h>
#include <cs50.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

// accept cli argument for k
int main(int argc, string argv[])
{
    int index, i, k, start, n;
    string plaintext;

    if (argc != 2 )
    {
        printf("Usage: ./caesar k\nBad cli cipher key...Must quit now before you break everything...\n");
        return 1;
    }

    //transform string in int with atoi
    k = atoi(argv[1]);
    printf("%i\n", k);
    printf("plaintext: ");
    plaintext = get_string();
    n = strlen(plaintext);

    printf("ciphertext: ");

    for (i=0; i<n; i++)
    {
        // check if upper or lower
        if (isupper(plaintext[i]))
        {
            start = 65;
        } else if (islower(plaintext[i]))
        {
            start = 97;
        }

        if (isalnum(plaintext[i]))
        {
            // be sure that index is in range 0-26
            index = (plaintext[i] - start + k)%26;
            printf("%c", start + index);
        }
        else
        {
            printf("%c", plaintext[i]);
        }
    }
    printf("\n");

    return 0;
}