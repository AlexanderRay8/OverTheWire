#This is a rot13 decrypting script
import string
data = open("data.txt")
for i in data.read():
    if (i.isupper()):
        print(string.ascii_uppercase[(string.ascii_uppercase.index(i) + 13) % len(string.ascii_uppercase) ], end="")
    elif (i.islower()):
        print(string.ascii_lowercase[(string.ascii_lowercase.index(i) + 13) % len(string.ascii_lowercase)], end="")
    else:
        print(i,end="")
print("")