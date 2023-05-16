flag = b"dohctf{flag_segfault_}\x00\x00"

assert len(flag) % 4 == 0

ar = []
for i in range(0, len(flag), 4):
    x = int.from_bytes(flag[i : i + 4], "little")
    ar.append(x)

data = [x ^ y for x, y in zip(ar, ar[1:])]
print("{", ", ".join(map(str, data)), "}")

for i, x in enumerate(ar):
    if i > 0:
        data[i - 1] ^= x
    if i < len(data):
        data[i] ^= x
    
