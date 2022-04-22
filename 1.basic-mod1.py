
import string
table = string.ascii_uppercase+string.digits

f = open("basic-mod1.txt","r")
arr = f.read().split()
arr = [int(i) for i in arr]

b = []
d = []
for i in arr:
    b.append(i%37)
for i in b:
    if(i <26):
        c = chr(i+65)
    elif(i>25 and i<36):
        c = chr(i+22)
    else:
        c = "_"
    d.append(c)
print(''.join([i for i in d]))