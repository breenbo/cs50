#include <stdio.h>

// Demonstration of ascii char <-> numbers

int main(void)
{
    for (int i = 65; i < 65 + 26; ++i) {
        // use i as ascii number and number
        printf("%c is %i\n", i, i);
    }
}
