from Crypto.Util.number import *
import string
table = string.ascii_uppercase+string.digits


f = open("basic-mod2.txt","r")
arr = f.read().split()
arr = [int(i) for i in arr]

arrA = []

for i in arr:
    a = inverse(i, 41)
    arrA.append(a)
table = "abcdefghijklmnopqrstuvwxyz0123456789_"
flag = "picoCTF{"
for i in arrA:
    flag += table[i-1]

print(flag,'}')

# a = "picoCTF{M98F9B_M6ZR8B_6F_9_I6H_5EHN9H8N_8K7LP99O}"
# print(a.lower())
# def encrypt(text,s):
#     result = ""
#     for i in range(len(text)):
#         char = text[i]
#         if (char != '_'):
#             result += table[(table.index(char) + s)%36]
#         else:
#             result += char
#     return result
# print(encrypt(cipher,-5))