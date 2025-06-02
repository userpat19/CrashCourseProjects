import random
import string

chars = " " + string.ascii_letters + string.punctuation + string.digits
chars = list(chars)
key = chars.copy()

random.shuffle(key)

#ENCRYPTION

plain_text = input("Enter the text:")
cipher = ""

for letter in plain_text:

    index = chars.index(letter)
    cipher += key[index]

print(f"Original message: {plain_text}")
print(f"Ciphered message: {cipher}")

#DECRYPTION

cipher = input("Decrypt text:")
plain_text = ""

for item in cipher:

    index = key.index(item)
    plain_text += chars[index]

print(f"Ciphered message: {cipher}")
print(f"Original message: {plain_text}")


