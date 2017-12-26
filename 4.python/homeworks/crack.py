# crack password no longer than 4 char, with only alphabeticals letters
# passwords can contains 1 to 4 char

import sys
import crypt # to use crypt function
import string # to simply have a-zA-Z list

if len(sys.argv) != 2:
    print("Usage : python3 crack.py hashed_password")
    exit(1)

# usage of crypt : crypt.crypt(word, salt)
# create a loop to test all char a-zA-Z, then crypt, and compare to hashed_password.
# if true, break
# implement 1 to 4 char
# 2 * 26 + 1 char : a-zA-Z and null=0
# test possible word
# test with possible salts

hashed_password = sys.argv[1]

# define list of test chars. +1 because stop is excluded
letters = string.ascii_letters[:]
digits = string.digits
possible_salt = letters + digits

# check password for 1 to 4 letters
def test_crypt(word, crypto):
    #change this function to store pass, salt and hash in dictionnary
    for i in possible_salt:
        for j in possible_salt:
            if crypt.crypt(word, i+j) == crypto:
                print("pass : " + word)
                print("salt : " + i+j)
                exit(0)

crypto = crypt.crypt("c","cz")

# check password for 1 to 4 letters
# create a dictionnary with all possible hash, then compare to the hashed_password
for i in range(1, 5, 1):
    if i == 1:
        print("Test " + str(i) + " char pass")
        for j in letters:
            test_crypt(j, hashed_password)
            print(chr(9) + "Test with " + j)
    elif i == 2:
        print("Test " + str(i) + " char pass")
        for j in letters:
            print(chr(9) + "Test with " + j + ".")
            for k in letters:
                test_crypt(j+k, hashed_password)
                print(2 * chr(9) + "Test with " + j + k)
    elif i == 3:
        print("Test " + str(i) + " char pass")
        for j in letters:
            print(chr(9) + "Test with " + j + "..")
            for k in letters:
                print(2 * chr(9) + "Test with " + j + k + ".")
                for l in letters:
                    test_crypt(j+k+l, hashed_password)
                    print(3 * chr(9) + "Test with " + j + k + l)
    else:
        print("Test 4 char pass")
        for j in letters:
            print(chr(9) + "Test with " + j + "...")
            for k in letters:
                print(2 * chr(9) + "Test with " + j + k + "..")
                for l in letters:
                    print(3 * chr(9) + "Test with " + j + k + l + ".")
                    for m in letters:
                        test_crypt(j+k+l+m, hashed_password)
                        print(4 * chr(9) + "Test with " + j + k + l + m)

exit(0)
