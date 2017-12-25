#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>

int cipher(string, string);
int checkPass(string);

int main(int argc, string argv[])
{
    // check if there is a pass
    if (argc != 2)
    {
        printf("Usage: ./vignere pass\nBad cli cipher string pass...Must quit now before you break everything...\n");
        return 1;
    }

    // check if pass is good, and stop if not
    if (checkPass(argv[1]) == 1)
    {
        return 1;
    }

    string pass = argv[1];
    string text;

    printf("pass: %s\n", pass);
    printf("plaintext: ");
    text = get_string();

    cipher(pass, text);
}


int cipher(string pass, string text)
{
    int textLen = 0;
    int passLen = 0;
    int start = 0;
    int index = 0;
    int countPass = 0;

    textLen = strlen(text);
    passLen = strlen(pass);

    printf("ciphertext: ");

    for (int i = 0; i < textLen; i++)
    {
        if (isupper(text[i]))
        {
            start = 65;
        } else if (islower(text[i]))
        {
            start = 97;
        }
        if (isalpha(text[i]))
        {
            // new index, be sure to be in range 0-26
            // change pass to lower, then remove 97 iot have A=a=0, B=b=1, and so on...
            index = (text[i] - start + tolower(pass[countPass])-97)%26;
            printf("%c", start + index);
            // set countPass and be sure to be in range 0-passLen
            countPass = (countPass + 1)%passLen ;
        } else {
            printf("%c", text[i]);
        }
    }
    printf("\n");

    return 0;
}


int checkPass(string pass)
{
    int i = 0;
    int n = strlen(pass);

    // check if non alpha char in pass
    for (i=0; i<n; i++)
    {
        if (!isalpha(pass[i]))
        {
            printf("pass invalid, only alpha allowed...\n");
            return 1;
        }
    }
    return 0;
}