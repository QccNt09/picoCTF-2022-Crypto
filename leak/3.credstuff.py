

fp = open("passwords.txt","r").read().split()
fu = open("usernames.txt","r").read().split()

for i in range(len(fu)):
    if "cultiris" in fu[i]:
        print(i, fu[i])
        print(fp[i])