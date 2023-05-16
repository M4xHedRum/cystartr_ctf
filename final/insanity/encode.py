zwsp = '\u200B' # 0
zwnj = '\u200C' # 1

def encode():
    out = open('result.txt', 'w')
    cover = "M4xHEDRUMCTF{obviously_not_the_flag}"
    plain = "DoHCTF{digital_invisible_ink}"
    binary = ''.join(format(ord(x) , 'b').zfill(8) for x in plain).replace('0', zwsp).replace('1', zwnj)
    third = int(len(cover) / 3)
    half = int(len(binary) / 2)
    result = cover[:third] + binary[:half] + cover[third:2 * third] + binary[half:] + cover[2 * third:]
    out.write(result)

encode()

