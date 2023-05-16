def encrypt_string(input_string):
    # Convert input string into a list of characters
    input_list = list(input_string)
    
    # Loop through each character in the list
    for i in range(len(input_list)):
        # Convert the character to its ASCII value
        ascii_val = ord(input_list[i])
        
        # Scramble the ASCII value using bitwise operations
        scrambled_ascii_val = (((ascii_val << 3) & 0xff) | ((ascii_val >> 5) & 0xff)) ^ 0xaa
        
        # Convert the scrambled ASCII value back into a character
        scrambled_char = chr(scrambled_ascii_val)
        
        # Replace the original character with the scrambled character
        input_list[i] = scrambled_char
    
    # Convert the list of characters back into a string and return it
    return ''.join(input_list)


flag = "DoHCTF{If_you_solved_in_less_than_120secs_youre_clever_hehe}"

import dis
#content of byteme.pyc
dis.dis(encrypt_string) 
