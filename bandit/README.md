# Bandit
This is a war game that focuses on the basics of linux.

hostname: bandit.labs.overthewire.org
port: 2220

## Bandit 0

The goal of this level is for you to log into the game using SSH.
The host to which you need to connect is bandit.labs.overthewire.org, on port 2220. 
The username is bandit0 and the password is bandit0. 
Once logged in, go to the Level 1 page to find out how to beat Level 1.

ssh command:
```bash
ssh bandit0@bandit.labs.overthewire.org -p 2220
# Password is bandit0
```

## Bandit 0 -> 1

ssh command:
```bash
ssh bandit0@bandit.labs.overthewire.org -p 2220
```

### Info

The password for the next level is stored in a file called readme located in 
the home directory. Use this password to log into bandit1 using SSH. 
Whenever you find a password for a level, use SSH (on port 2220) to log into 
that level and continue the game.

### Solution

For this level all we need to do is open the readme file.

Commands:
```bash
cat readme
```
Output:
    NH2SXQwcBdpmTEzi3bvBHMM9H66vVXjL

## Bandit 1 -> 2

ssh command:
```bash
ssh bandit1@bandit.labs.overthewire.org -p 2220
```

### Info

The password for the next level is stored in a file
called - located in the home directory

### Solution

This file can be opened if you put './' in front of the file name.

Commands:
```bash
cat ./-
```

Output:
    rRGizSaX8Mk1RTb1CNQoXTcYZWU6lgzi

## Bandit 2 -> 3

ssh command:
```bash
ssh bandit2@bandit.labs.overthewire.org
```

### Info

The password for the next level is stored in a file 
called "spaces in this filename" located in the home directory

### Solution

This file can be read using quotes around the file name.

Commands:
```bash
cat "spaces in this filename"
```

Output:
    aBZ0W5EmUfAf7kHTQeOwd8bauFJ2lAiG

## Bandit 4 -> 5

ssh command:

```bash
ssh bandit4@bandit.labs.overthewire.org -p 2220
```

### Info

### Solution

Output:
    password


## Bandit 6 -> 7

ssh command:

```bash
ssh bandit6@bandit.labs.overthewire.org -p 2220
```

### Info

### Solution

Output:
    password


## Bandit 8 -> 9

ssh command:

```bash
ssh bandit8@bandit.labs.overthewire.org -p 2220
```

### Info

### Solution

Output:
    password


## Bandit 10 -> 11

ssh command:

```bash
ssh bandit10@bandit.labs.overthewire.org -p 2220
```

### Info

### Solution

Output:
    password


## Bandit 12 -> 13

ssh command:

```bash
ssh bandit12@bandit.labs.overthewire.org -p 2220
```

### Info

### Solution

Output:
    password


## Bandit 14 -> 15

ssh command:

```bash
ssh bandit14@bandit.labs.overthewire.org -p 2220
```

### Info

### Solution

Output:
    password


## Bandit 16 -> 17

ssh command:

```bash
ssh bandit16@bandit.labs.overthewire.org -p 2220
```

### Info

### Solution

Output:
    password


## Bandit 18 -> 19

ssh command:

```bash
ssh bandit18@bandit.labs.overthewire.org -p 2220
```

### Info

### Solution

Output:
    password


## Bandit 20 -> 21

ssh command:

```bash
ssh bandit20@bandit.labs.overthewire.org -p 2220
```

### Info

### Solution

Output:
    password


## Bandit 22 -> 23

ssh command:

```bash
ssh bandit22@bandit.labs.overthewire.org -p 2220
```

### Info

### Solution

Output:
    password


## Bandit 24 -> 25

ssh command:

```bash
ssh bandit24@bandit.labs.overthewire.org -p 2220
```

### Info

### Solution

Output:
    password


## Bandit 26 -> 27

ssh command:

```bash
ssh bandit26@bandit.labs.overthewire.org -p 2220
```

### Info

### Solution

Output:
    password


## Bandit 28 -> 29

ssh command:

```bash
ssh bandit28@bandit.labs.overthewire.org -p 2220
```

### Info

### Solution

Output:
    password


## Bandit 30 -> 31

ssh command:

```bash
ssh bandit30@bandit.labs.overthewire.org -p 2220
```

### Info

### Solution

Output:
    password


## Bandit 32 -> 33

ssh command:

```bash
ssh bandit32@bandit.labs.overthewire.org -p 2220
```

### Info

### Solution

Output:
    password


