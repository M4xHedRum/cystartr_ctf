import random

def encryption_level_1337(msg):
    key = random.randint(1, 255)
    encrypted_text = ""
    for c in msg:
        if c.isalpha():
            shifted = ord(c) + key
            if c.isupper():
                encrypted_text += chr((shifted - 65) % 26 + 65)
            else:
                encrypted_text += chr((shifted - 97) % 26 + 97)
        else:
            encrypted_text += c
    encoding_level_1338 = ' '.join(format(ord(x), '08b') for x in encrypted_text)

    encoding_level_1339= ''.join(['1' if x=='0' else '0' for x in encoding_level_1338])
    return encoding_level_1338

with open('message.txt', 'r') as file:
    message = file.read().strip()

encrypted = encryption_level_1337(message)
print(encrypted)
