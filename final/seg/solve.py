ar = [ 85133584, 958138136, 956302367, 302714898, 1953237054 ]
x = int.from_bytes(b"DoHC", "little")
for y in ar:
    z = x.to_bytes(4, "little")
    print(z.decode(), end="")
    x ^= y
z = x.to_bytes(4, "little")
print(z.decode(), end="")
