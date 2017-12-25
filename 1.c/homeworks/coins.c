#include <stdio.h>
#include <math.h>

/* Find numbers of quarter (0.25), dime (0.1), nickel(0.05) and pennies(0.01) to have change */
/* Beware of imprecision : need to multiply by 100 and round results */

/* Declaration of functions */
int coin(float, float);

int main(void)
{
    float change = 0.41;
    float rest;
    int quarter;
    int dime;
    int nickel;
    int pennie;

    quarter = coin(change, 0.25);
    rest = change - quarter * 0.25;
    dime = coin(rest, 0.10);
    rest -= dime * 0.1;
    nickel = coin(rest, 0.05);
    rest -= nickel * 0.05;
    pennie = coin(rest, 0.01);

    printf("You need %i quarter, %i dime, %i nickel and %i pennies", quarter, dime, nickel, pennie);
}

/* Function to calculate number of coins */
int coin(float money, float coinValue)
{
    int result = round(money*100) /round(coinValue * 100);
    return result;
}
