#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(void)
{
    printf("Please enter your name : ");
    //string name = get_string();
    char name[50] = "B    h";
    printf("Your name is %s\n", name);

    int n = strlen(name);

    for (int i = 0; i < n; i++) 
    {
        // check if empty char
        while (name[i] == 32)
        {
            // replace chars to remove space
            for (int j = i; j < n ; j++)
            {
                name[j] = name[j+1];
            }
        }
    }
    printf("Your new name is %s\n", name);
}
