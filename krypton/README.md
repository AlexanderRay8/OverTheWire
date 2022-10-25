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

ROT13 is a simple substitution cipher.

Substitution ciphers are a simple replacement algorithm. In this example of a substitution cipher, we will explore a ‘monoalphebetic’ cipher. Monoalphebetic means, literally, “one alphabet” and you will see why.

This level contains an old form of cipher called a ‘Caesar Cipher’. A Caesar cipher shifts the alphabet by a set number. For example:

plain:  a b c d e f g h i j k ...
cipher: G H I J K L M N O P Q ...

In this example, the letter ‘a’ in plaintext is replaced by a ‘G’ in the ciphertext so, for example, the plaintext ‘bad’ becomes ‘HGJ’ in ciphertext.

The password for level 3 is in the file krypton3. It is in 5 letter group ciphertext. It is encrypted with a Caesar Cipher. Without any further information, this cipher text may be difficult to break. You do not have direct access to the key, however you do have access to a program that will encrypt anything you wish to give it using the key. If you think logically, this is completely easy.

One shot can solve it!

Have fun.

Additional Information:

The encrypt binary will look for the keyfile in your current working directory. Therefore, it might be best to create a working direcory in /tmp and in there a link to the keyfile. As the encrypt binary runs setuid krypton3, you also need to give krypton3 access to your working directory.

### Solution

Running the encrypt script given, I tested it with an alphabet string to see how it changes the values. I then used rotate.py to see how far it rotated. I saw it rotates things by 12. To decode it, I can rotate it by 14.

Commands:
```bash
# On remote
echo "abcdefghijklmnopqrstuvwxyz" > test.txt
/krypton/krypton2/encrypt test.txt # Outputs MNOPQRST...
# On local machine
echo "abcdefghijklmnopqrstuvwxyz" > test.txt # recreate
./rotate.py ./test.txt # Find number for MNOPQRST... -> 14
sftp sftp://krypton2@krypton.labs.overthewire.org:2231//krypton/krypton2/krypton3
# ^^^ put in ROTTEN for password ^^^
./rotate.py ./krypton3 -r 14
```

Output:
    CAESARISEASY

## Krypton 3 -> 4

ssh command:
```bash
ssh krypton3@krypton.labs.overthewire.org -p 2231
```

### Info

Well done. You’ve moved past an easy substitution cipher.

The main weakness of a simple substitution cipher is repeated use of a simple key. In the previous exercise you were able to introduce arbitrary plaintext to expose the key. In this example, the cipher mechanism is not available to you, the attacker.

However, you have been lucky. You have intercepted more than one message. The password to the next level is found in the file ‘krypton4’. You have also found 3 other files. (found1, found2, found3)

You know the following important details:

    The message plaintexts are in American English (*** very important) - They were produced from the same key (*** even better!)

Enjoy.

### Solution

Grabbed all of the files to local machine and copied them to an external website and played around with the text substitutions. (https://crypto.interactive-maths.com/frequency-analysis-breaking-the-code.html)

Commands:
```bash

```