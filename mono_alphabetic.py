import random
import string


# Create the random key for encryption

def create_key():
    # Random string of digits
    digits = string.digits
    num_list = list(digits)
    random.shuffle(num_list)
    key1 = "".join(num_list)
    # Random string of english alphabet
    english_alphabet = string.ascii_lowercase
    atoz_list = list(english_alphabet)
    random.shuffle(atoz_list)
    key2 = "".join(atoz_list)
    return key1 + key2


# Encrypt the plain text and generate the ciphertext
def encryption(text, key):
    cipher_text = ""
    for ch in text:
        if ch.islower():
            # value between 0-25
            index = ord(ch) - ord('a')
            cipher_text += key[index + 10]
        elif ch.isupper():
            index = ord(ch) - ord('A')
            cipher_text += key[index + 10]
        elif ch.isdigit():
            index = int(ch)
            cipher_text += key[index]
        else:
            cipher_text += ch
    return cipher_text


# Decryption
def decryption(key, cipher_text):
    decipher_text = ''
    for ch in cipher_text:
        if ch.islower():
            index = key.find(ch)
            decipher_text += chr(index + ord('a') - 10)
        elif ch.isdigit():
            index = key.find(ch)
            decipher_text += str(index)

        else:
            decipher_text += ch
    return decipher_text


# Get the plain text for encryption
plain_text = input("Enter the message: ")
key = create_key()
print(f"key : {key}")

cipher_text = encryption(plain_text, key)
print(f"cipher text : {cipher_text}")

decipher_text = decryption(key, cipher_text)
print(f"decipher text : {decipher_text}")
