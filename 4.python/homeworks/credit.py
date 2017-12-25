#  Prompt user to enter a credit card number and report if it's a valid AMEX, Mastercard or Visa card number
#  AMEX start with 34 or 37, MasterCard : 51, 52, 53, 54, 55, Visa : 4
#  AMEX : 15 digits, MasterCard : 16 digits, Visa :13 or 16


##############################
# FUNCTIONS
##############################

def check_sum(card_number):
    first_sum = 0
    second_sum = 0
    final = 0
    # select the second to last numbers in card_number, multiplie by 2 and sum
    for i in range(1, len(card_number), 2):
        first = 2 * int(card_number[i])
        # 14 + 4 + 12 -> 1+4+4+1+2
        first = str(first)
        for k in range(len(first)):
            first_sum += int(first[k])

    for l in range(0, len(card_number), 2):
        second_sum += int(card_number[l])

    final = first_sum + second_sum

    if final % 10 == 0:
        return 0
    else:
        return 1

def check_number(card_number, bank):
    if bank == "AMEX":
        first_digits = [34, 37]
        nb_digits = 2
    elif bank == "MASTERCARD":
        first_digits = range(51,56)
        nb_digits = 2
    elif bank == "VISA":
        first_digits = [4]
        nb_digits = 1

    if int(card_number[:nb_digits]) in first_digits:
        if check_sum(card_number) == 0:
            print(bank)
            exit(0)
        else:
            print("INVALID")
            exit(9)
    else:
        print("INVALID")
        exit(2)

##############################
# MAIN
##############################
card_number = ""

#  check the format of card number
while not card_number.isdigit() :
    card_number = input("Card number, without spaces or hyphens : ")

#  check the number of digits :
if len(card_number) not in [13, 15, 16]:
    print("INVALID")
    exit(1)

if len(card_number) == 13:
    check_number(card_number, "VISA")
if len(card_number) == 15 :
    check_number(card_number, "AMEX")
if len(card_number) == 16:
    if int(card_number[:2]) in range(51,56):
        check_number(card_number, "MASTERCARD") 
    else:
        check_number(card_number, "VISA")
