# Encryption


def encryption():
    plain_text = input("Enter the plain text : ")

    shift = int(input("Enter the number of shift : "))

    encrypt_text = ""

    for ch in plain_text:
        # if char is lowercase
        if ch.islower():
            encrypt_text += chr((ord(ch) + shift - ord('a')) % 26 + ord('a'))
        # if char is uppercase
        elif ch.isupper():
            encrypt_text += chr((ord(ch) + shift - ord('A')) % 26 + ord('A'))
        # if char is a digit
        elif ch.isdigit():
            encrypt_text += chr((ord(ch) + shift - ord('0')) % 10 + ord('0'))
        else:
            encrypt_text += ch
    print(encrypt_text)


# Decryption
def decryption():
    cipher_text = input("Enter the cipher text : ")

    shift = int(input("Enter the number of shift : "))

    decrypt_text = ""

    for ch in cipher_text:
        if ch.islower():
            decrypt_text += chr((ord(ch) - shift - ord('a')) % 26 + ord('a'))
        elif ch.isupper():
            decrypt_text += chr((ord(ch) - shift - ord('A')) % 26 + ord('A'))
        elif ch.isdigit():
            decrypt_text += chr((ord(ch) - shift - ord('0')) % 10 + ord('0'))
        else:
            decrypt_text += ch

    print(decrypt_text)


encryption()
decryption()
