# Krypton

This is a war game that focuses on basic cryptography.

hostname: krypton.labs.overthewire.org
port: 2231

## Krypton 0 -> 1

There is no ssh command for this level, just use your local machine.

### Info

Welcome to Krypton! The first level is easy. The following string encodes
the password using Base64:

S1JZUFRPTklTR1JFQVQ=

Use this password to log in to krypton.labs.overthewire.org with username
krypton1 using SSH on port 2231. You can find the files for other levels in
/krypton/

### Solution

This is a simple problem to solve, just decoding the base64 encoded string.
base64 is GNU utility that will encode and decode base64.
It reads in from a file or accepts input from stdin
-d is the flag to decode a string

```bash
echo "S1JZUFRPTklTR1JFQVQ=" | base64 -d
```

### Output

    KRYPTONISGREAT

## Krypton 1 -> 2

ssh command:

```bash
ssh krypton1@krypton.labs.overthewire.org -p 2231
```

### Info

The password for level 2 is in the file 'krypton2'. It is 'encrypted' using a
simple rotation. It is also in non-standard ciphertext format. When using alpha
characters for cipher text it is normal to group the letters into 5 letter clusters,
regardless of word boundaries. This helps obfuscate any patterns.
This file has kept the plain text word boundaries and carried them to the cipher text.
Enjoy!

### Solution

I needed to create a program, `rotate.py` that rotates text. I decided to make it a bit more robust
with optional rotation amounts you can provide, or it will just print all of the rotations.

The main part of the program just adds by the rotation amount, wrapping around to the
beginning if it runs past 'Z'.

```bash
./rotate.py -r 13
```

### Output

    LEVEL TWO PASSWORD ROTTEN

## Krypton 2 -> 3

ssh command:

```bash
ssh krypton2@krypton.labs.overthewire.org -p 2231
```

### Info
