# crack password no longer than 4 char, with only alphabeticals letters
# passwords can contains 1 to 4 char
# create a brute force dictionary, then compare to hashed_password entered by user
# use of recursive function to test from 1 to 4 letters pass

import sys
import crypt # to use crypt function
import string # to simply have a-zA-Z list
import itertools # create combinaison_with_replacement

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

LETTERS = string.ascii_letters[:]
DIGITS = string.digits
POSSIBLE_SALT = LETTERS + DIGITS

CRYPTO = crypt.crypt("c","cz")
WORDS = []

########################################
# FUNCTIONS
########################################

# check password for 1 to 4 letters
def test_crypt(word, crypt_word):
    #change this function to store pass, salt and hash in dictionnary
    for i in POSSIBLE_SALT:
        for j in POSSIBLE_SALT:
            if crypt.crypt(word, i+j) == crypt_word:
                print("pass : " + word)
                print("salt : " + i+j)
                exit(0)

# recursive search :
# loop for i in range(nb_char)
# if i = nh_char : finished
# else : do for i+1


def create_dict(stop, start = 1):
    print("Search for " + str(start) + " char pass")
    possible_pass = start * ["a"] 
    print(possible_pass)

    possible_pass = itertools.combinations_with_replacement(LETTERS, start)
    pass_list = [list(x) for x in possible_pass]

    # create a list of all possible words
    word = ""
    words = []
    for i in range(len(pass_list)):
        for char in pass_list[i]:
            word += char
        words.append(word)
        word = ""

    # store hashed_value for every possible words
    #  print(len(words))

    # the recursive part
    if start == stop:
        print(words)
        print("Done")
        return words
        #  exit(0)
    else:
        create_dict(stop, start + 1)


########################################
# MAIN
########################################

print(create_dict(2))

# check password for 1 to 4 letters
# create a dictionnary with all possible hash, then compare to the hashed_password
# use recursive function too...
#  for i in range(1, 5, 1):
    #  if i == 1:
        #  print("Test " + str(i) + " char pass")
        #  for j in letters:
            #  test_crypt(j, hashed_password)
            #  print(chr(9) + "Test with " + j)
    #  elif i == 2:
        #  print("Test " + str(i) + " char pass")
        #  for j in letters:
            #  print(chr(9) + "Test with " + j + ".")
            #  for k in letters:
                #  test_crypt(j+k, hashed_password)
                #  print(2 * chr(9) + "Test with " + j + k)
    #  elif i == 3:
        #  print("Test " + str(i) + " char pass")
        #  for j in letters:
            #  print(chr(9) + "Test with " + j + "..")
            #  for k in letters:
                #  print(2 * chr(9) + "Test with " + j + k + ".")
                #  for l in letters:
                    #  test_crypt(j+k+l, hashed_password)
                    #  print(3 * chr(9) + "Test with " + j + k + l)
    #  else:
        #  print("Test 4 char pass")
        #  for j in letters:
            #  print(chr(9) + "Test with " + j + "...")
            #  for k in letters:
                #  print(2 * chr(9) + "Test with " + j + k + "..")
                #  for l in letters:
                    #  print(3 * chr(9) + "Test with " + j + k + l + ".")
                    #  for m in letters:
                        #  test_crypt(j+k+l+m, hashed_password)
                        #  print(4 * chr(9) + "Test with " + j + k + l + m)

#  exit(0)
