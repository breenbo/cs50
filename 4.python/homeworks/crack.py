# crack password no longer than 4 char, with only alphabeticals letters
# passwords can contains 1 to 4 char

import sys
import crypt # to use crypt function

if len(sys.argv) != 2:
    print("Usage : python3 crack.py string")
    exit(1)

# usage of crypt : crypt.crypt(word, salt)
