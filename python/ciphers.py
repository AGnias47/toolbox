#!/usr/bin/env python3

"""
Cesar Cipher - Assigns ints to each letter; key encrypts by moving string n spaces, where n is the integer encoding of
the key. Implementation is imperfect but prevents us from having to create a full dict mapping of all characters. Works
for standard english characters, which is the main purpose of the cipher.

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


Diffie-Hellman Key Exchange

Finding factors is extremely hard. Using prime numbers makes factorization practically impossible. Use large prime numbers.

Main disadvantage of private key system is that private key must be exchanged. DH can exchange private keys over a
public channel.
Information not shared, not used for encryption or decryption, just sharing keys.

Steps
Generate hue prime number n, g must be primative root of n. Primitive root - g^1 to n gives all numbers in that range as a mod of n. ex. n=11, g=8.
Algo
Sender generates n and g, sends those to receiver
Sender and receiver generate a random number [1,n), x and y respectively
Sender calculates k_1 = g^x mod n, sends this to receiver
Receiver calculates k_2 = g^y mod n, sends to receiver
Both calculate shared secret key
Sender: k2^x mod n = (g^y mod n)^x mod n = g^xy mod n
Receiver: k1^y mod n = (g^x mod n)^y mod n = g^yx mod n
Using primitive root ensures we have the maximum number of keys, prevents brute force attacks

Cracking
Relies on there being no efficient way to calculate the discrete log
Trapdoor function - easy to calculate in one direction, difficult to inverse
Man in the middle - attacker has k1, sends m1 to receiver, attacker gets k2, sends m2 to sender. Can be circumvented with SHA256 hashes. If tampered with, hashes will be different.
"""


def cesar_cipher(body, key, action="encrypt"):
    key_val = char_to_int(key)
    if action == "encrypt":
        return "".join([chr((char_to_int(c) + key_val) % 26 + 64) for c in body])
    elif action == "decrypt":
        return "".join([chr((char_to_int(c) - key_val) % 26 + 64) for c in body])
    raise ValueError


def otp(text, key):
    if isinstance(text, list):
        text_bin = text
        encode, decode = False, True
    else:
        text_bin = [ord(c.upper()) for c in text]
        encode, decode = True, False
    key_bin = [ord(c) for c in key]
    otp_coding = list()
    for t, k in zip(text_bin, key_bin):
        otp_coding.append(bin(t ^ k))
    if encode:
        return [int(c, 2) for c in otp_coding]
    if decode:
        return "".join([chr(int(c, 2)) for c in otp_coding])
    raise ValueError


def char_to_int(c):
    return ord(c.upper()) - 64


if __name__ == "__main__":
    key = "KDOVYKCNGIX"
    encrypted = cesar_cipher("HelloWorld", key[-1], "encrypt")
    print(encrypted)
    decrypted = cesar_cipher(encrypted, key[-1], "decrypt")
    print(decrypted)
    encrypted_otp = otp("Hello World", key)
    print(encrypted_otp)
    decrypted_otp = otp(encrypted_otp, key)
    print(decrypted_otp)
