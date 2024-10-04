def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    ciphertext = ""
    for i in range(len(plaintext)):
        if plaintext[i].isupper():
            cipherchar = ord(plaintext[i]) + shift
            if cipherchar > 90:
                while cipherchar > 90:
                    cipherchar -= 26
            ciphertext += chr(cipherchar)
        elif plaintext[i].islower():
            cipherchar = ord(plaintext[i]) + shift
            if cipherchar > 122:
                while cipherchar > 122:
                    cipherchar -= 26
            ciphertext += chr(cipherchar)
        elif (plaintext[i].isdigit()) or (not plaintext[i].isalpha() and not plaintext[i].isdigit()):
            ciphertext += plaintext[i]
    return ciphertext

def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    plaintext = ""
    for i in range(len(ciphertext)):
        if ciphertext[i].isupper():
            plainchar = ord(ciphertext[i]) - shift
            if plainchar < 65:
                while plainchar < 65:
                    plainchar += 26
            plaintext += chr(plainchar)
        elif ciphertext[i].islower():
            plainchar = ord(ciphertext[i]) - shift
            if plainchar < 97:
                while plainchar < 97:
                    plainchar += 26
            plaintext += chr(plainchar)
        elif (ciphertext[i].isdigit()) or (not ciphertext[i].isalpha() and not ciphertext[i].isdigit()):
            plaintext += ciphertext[i]
    return plaintext