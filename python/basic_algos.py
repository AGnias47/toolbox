#!/usr/bin/env python3

"""
Vigenere Cipher - Same as Cesar except the key is a word that is repeated over the text

Kasiski Algorithm - Used to crack Vigenere Cipher. Find a repeated substring to determine the length 
of the key and then do frequency analysis.

Assume that the length of the key is the factor with the highest count, ex. considering this table

| Repeated Substring | Distance   |
| WS AY              | 25 (5x5)   |
| HHA                | 10 (2x5)   |
| KKLA               | 20 (2x2x5) |

We would assume that the key is of length 5. If only 1, we may have to try multiple factors, including the length of the
distance between substrings.

For frequency analysis, we would then use every 5th letter for our frequency analysis.

This method utilizes information leaking.

One Time Pad method uses as many letters in the key as the length of the plain text to prevent information leaking, so
long as a randomized key is generated. Using an English sentance for the key can still be vulnerable to information
leaking.

One time pad uses XOR, so letters are first translated into the binary number of their ASCII value. XOR operations can
be used easily for encryption and decryption, as the inverse is the function itself. XOR gives 0 or 1 with 50%
probability.

Takes plaintext and converts into binary, takes key and converts into binary, uses XOR for encryption and decryption.

Should use a method of generating random numbers with true randomness or a good algo. Computers are deterministic, so
certain input will always give certain output that can be hacked.

Some algos include

Middle-square method
Input: seed
multiply seed by itself, get middle of result, result is the seed in the next iteration.
If we know the seed, we can hack this method.
This method can also reach a period where it reaches a seed it previously used.
N digits, algo uses at most 10^N digits before reusing the seed.
If the seed repeats itself, we essentially have a Vigenere Cipher.

Linear Congruential Generator
Xn+1 = (aXn + c) % m

Seed is X0
"""


def vigenere(text):
    pass


def kasiski(text):
    pass


def otp(text, key):
    text_bin = [ord(c) for c in text]
    key_bin = [ord(c) for c in key]
    otp_coding = list()
    for t, k in zip(text_bin, key_bin):
        print(t ^ k)
        otp_coding.append(bin(t ^ k))
    return "".join(otp_coding)


if __name__ == "__main__":
    key = "XHSLE"
    encrypted = otp("HELLO", key)
    print(encrypted)
    decrypted = otp(encrypted, key)
    print(decrypted)
