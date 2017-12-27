# crack password no longer than 4 char, with only alphabeticals letters
# passwords can contains 1 to 4 char
# create a brute force dictionary, then compare to hashed_password entered by user
# use of recursive function to test from 1 to 4 letters pass

import sys
import crypt # to use crypt function
import string # to simply have a-zA-Z list
import itertools # create combinaison_with_replacement
import json # to create a dictinary of hashed values

if len(sys.argv) != 2:
    print("Usage : python3 crack.py hashed_password")
    exit(1)

# hashed_pass to find:
#  andi:50.jPgLzVirkc
#  jason:50YHuxoCN9Jkc
#  malan:50QvlJWn2qJGE
#  mzlatkova:50CPlMDLT06yY
#  patrick:50WUNAFdX/yjA
#  rbowden:50fkUxYHbnXGw
#  summer:50C6B0oz0HWzo
#  stelios:50nq4RV/NVU0I
#  wmartin:50vtwu4ujL.Dk
#  zamyla:50i2t3sOSAZtk


CRYPTO = sys.argv[1]

LETTERS = string.ascii_letters[:]
DIGITS = string.digits
POSSIBLE_SALT = LETTERS + DIGITS

#  CRYPTO = crypt.crypt("rolf","50")
SALT = str(50)

########################################
# FUNCTIONS
########################################

# check password for 1 to 4 letters
def test_hash(word, salt, crypted_word):
    if crypt.crypt(word, salt) == crypted_word:
        return(0)


def search_hash(stop, start = 1):
    # use product of itertools, to have all possible words of start characters
    possible_pass = itertools.product(LETTERS, repeat = start)
    pass_list = [list(x) for x in possible_pass]

    # create a list of all possible words
    word = ""

    for i in range(len(pass_list)):
        for char in pass_list[i]:
            word += char
        # search for hash in possible word
        if(test_hash(word, SALT, CRYPTO) == 0):
            return(word)
        word = ""

    # the recursive part
    if start == stop:
        #  print(words)
        print("Nothing found.")
    else:
        return search_hash(stop, start + 1)

########################################
# MAIN
########################################

print(search_hash(4))

########################################
# Massive check
########################################

#  crypto_dict = {"andi":"50.jPgLzVirkc", "jason":"50YHuxoCN9Jkc", "malan":"50QvlJWn2qJGE", "mzlatkova":"50CPlMDLT06yY", "patrick":"50WUNAFdX/yjA", "rbowden":"50fkUxYHbnXGw", "summer":"50C6B0oz0HWzo", "stelios":"50nq4RV/NVU0I", "wmartin":"50vtwu4ujL.Dk", "zamyla":"50i2t3sOSAZtk"}

#  for k,v in crypto_dict.items():
    #  CRYPTO = v
    #  print("{} : {}".format(k,CRYPTO))
    #  print("{} : {}".format(k, search_hash(4)))
