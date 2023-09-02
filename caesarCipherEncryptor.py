def caesarCipherEncryptor(string, key):
    return "".join([chr((ord(c) - 97 + key) % 26 + 97) for c in string])
