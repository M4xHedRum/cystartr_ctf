binary_str = '01000010 01101101 01000110 01000001 01010010 01000100 01111011 01000111 01000010 01011001 01001100 01011111 01010010 01000110 01000011 01011111 01000010 01000011 01000001 01010000 01010111 01001110 01010010 01001101 01001101 01010000 01111101'
binary_list = binary_str.split()

ascii_str = ''.join([chr(int(binary, 2)) for binary in binary_list])

for key in range(1, 256):
    decrypted = ''
    for c in ascii_str:
        if c.isalpha():
            shifted = ord(c) - key
            if c.isupper():
                decrypted += chr((shifted - 65) % 26 + 65)
            else:
                decrypted += chr((shifted - 97) % 26 + 97)
        else:
            decrypted += c
    if "DoH" in decrypted:
        print(f"Key: {key}, Decrypted message: {decrypted}")
