from string import ascii_uppercase
import string


cipher = "H98A9W_H6UM8W_6A_9_D6C_5ZCI9C8I_8F7GK99J"
table = ascii_uppercase + string.digits
def encrypt(text,s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char != '_'):
            result += table[(table.index(char) + s)%36]
        else:
            result += char
    return result
print(encrypt(cipher,-5))