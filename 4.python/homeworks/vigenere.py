import sys

# vigenere : get key string and crypt some plaintext

if len(sys.argv) != 2 or sys.argv[1].isdigit():
    print("Usage : python3 vigenere.py key_string")
    exit(1) # c return equivalent

# to use cli argv : sys.argv[1]
key = sys.argv[1].lower()

plain = input("plaintext : ")
cipher = ""
key_index = 0

# convert char to int : ord()
# convert int to char : chr()
for i in range(len(plain)):
    # convert each char in ascii int, transform to new char with key
    # convert only char in azAZ
    
    # set key index depending on number of key char
    cipher_key = ord(key[key_index]) - 97

    # check if alpha - no change for number, punctuation or spaces:
    if plain[i].isalpha():

        # check is lower or upper, then set the index
        if plain[i].islower():
            index = 97
        else:
            index = 65

        # set new char (%26 to cycle a-z) from index
        cipher_char = index + (ord(plain[i]) - index + cipher_key)%26
        # transform ascii int to char
        cipher_char = chr(cipher_char)
        # increment 1 to key_index, but stay in lenght key with modulo
        key_index = (key_index +1)%len(key)
    else:
        cipher_char = plain[i]

    # concatenate in cipher
    cipher += cipher_char

print("ciphertext : " + cipher)
