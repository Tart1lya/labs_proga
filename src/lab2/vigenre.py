def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    encrypt_vigenere("python", "a")
    'python'
    encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    i = 0
    j = 0
    while i != len(plaintext):
        if plaintext[i].isupper():
            cipherchar = ord(plaintext[i]) + ord(keyword[j]) - 65
            if cipherchar > 90:
                while cipherchar > 90:
                    cipherchar -= 26
            ciphertext += chr(cipherchar)
        elif plaintext[i].islower():
            cipherchar = ord(plaintext[i]) + ord(keyword[j]) - 97
            if cipherchar > 122:
                while cipherchar > 122:
                    cipherchar -= 26
            ciphertext += chr(cipherchar)
        elif (plaintext[i].isdigit()) or (not plaintext[i].isalpha() and not plaintext[i].isdigit()):
            ciphertext += plaintext[i]
        j += 1
        if j == len(keyword):
            j = 0
        i += 1
    return ciphertext

def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    decrypt_vigenere("python", "a")
    'python'
    decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    i = 0
    j = 0
    while i != len(ciphertext):
        if ciphertext[i].isupper():
            plainchar = ord(ciphertext[i]) - ord(keyword[j]) + 65
            if plainchar < 65:
                while plainchar < 65:
                    plainchar += 26
            plaintext += chr(plainchar)
        elif ciphertext[i].islower():
            plainchar = ord(ciphertext[i]) - ord(keyword[j]) + 97
            if plainchar < 97:
                while plainchar < 97:
                    plainchar += 26
            plaintext += chr(plainchar)
        elif (ciphertext[i].isdigit()) or (not ciphertext[i].isalpha() and not ciphertext[i].isdigit()):
            plaintext += ciphertext[i]
        j += 1
        if j == len(keyword):
            j = 0
        i += 1
    return plaintext