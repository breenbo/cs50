#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(void)
{
    char name[7] = "emicile";

    int n = strlen(name);
    for (int i = 0; i < n ; ++i) 
    {
        // convert char toupper
        printf("%c\n",toupper(name[i]));
    }
    printf("%s", name);
}
