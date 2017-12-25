import sys

if len(sys.argv) != 2 or not sys.argv[1].isdigit() or int(sys.argv[1]) < 0:
    print("Usage : python3 caesar.py positive_integer")
    exit(1) # c return equivalent

# to use cli argv : sys.argv[1]
key = int(sys.argv[1])

plain = input("plaintext : ")
cipher = ""

# convert char to int : ord()
# convert int to char : chr()
for i in range(len(plain)):
    # convert each char in ascii int, transform to new char with key
    # convert only char in azAZ
    if plain[i].isalpha():
        # check is lower or upper, then set the index
        if plain[i].islower():
            index = 97
        else:
            index = 65

        # set new char (%26 to cycle a-z) from index
        cipher_char = index + (ord(plain[i]) - index + key)%26
        # transform ascii int to char
        cipher_char = chr(cipher_char)
    else:
        cipher_char = plain[i]

    # concatenate in cipher
    cipher += cipher_char

print("ciphertext : " + cipher)
