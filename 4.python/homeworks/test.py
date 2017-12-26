import string
import crypt

def test_crypt(word, crypto):
    for i in possible_salt:
        for j in possible_salt:
            if crypt.crypt(word, i+j) == crypto:
                print("pass : " + word)
                print("salt : " + i+j)
                exit(0)

#  crypto = "50fkUxYHbnXGw"
letters = string.ascii_letters[:]
digits = string.digits
possible_salt = letters + digits

crypto = crypt.crypt("c","cz")

# check password for 1 to 4 letters
for i in range(1, 5, 1):
    if i == 1:
        for j in letters:
            test_crypt(j)
    elif i == 2:
        for j in letters:
            for k in letters:
                test_crypt(j+k)
    elif i == 3:
        for j in letters:
            for k in letters:
                for l in letters:
                    test_crypt(j+k+l)
    else:
        for j in letters:
            for k in letters:
                for l in letters:
                    for m in letters:
                        test_crypt(j+k+l+m)
