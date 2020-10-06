#!/usr/bin/env python3

"""
Cesar Cipher - Assigns ints to each letter; key encrypts by moving string n spaces, where n is the integer encoding of
the key. Implementation is imperfect but prevents us from having to create a full dict mapping of all characters. Works
for standard english characters, which is the main purpose of the cipher.
"""


def cesar_cipher(body, key, action="encrypt"):
    key_val = char_to_int(key)
    if action == "encrypt":
        return "".join([chr((char_to_int(c) + key_val) % 26 + 64) for c in body])
    elif action == "decrypt":
        return "".join([chr((char_to_int(c) - key_val) % 26 + 64) for c in body])
    raise ValueError


def char_to_int(c):
    return ord(c.upper()) - 64


if __name__ == "__main__":
    key = "E"
    encrypted = cesar_cipher("HelloWorld", key, "encrypt")
    print(encrypted)
    decrypted = cesar_cipher(encrypted, key, "decrypt")
    print(decrypted)
