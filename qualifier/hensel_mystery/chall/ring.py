from sage.all import *
import codecs

def read_flag():
    with open('flag.txt', 'r') as file:
        return file.read().strip()

def encode_flag(flag):
    encoded = codecs.encode(flag.encode(), 'hex')
    return int(encoded, 16)

def generate_polynomial(flag):
    ranges = int(log(flag, 2))
    p = 35671
    k = 100
    N = p**k
    d = 5
    P = PolynomialRing(Zmod(N), names='x', implementation='NTL')
    x = P.gen()
    poly = 0
    for c in range(d):
        poly += ZZ.random_element(2**ranges, 2**(ranges+1))*x**c
    remainder = poly(flag)
    poly = poly - remainder
    assert poly(flag) == 0
    return poly

def main():
    flag = read_flag()
    encoded_flag = encode_flag(flag)
    poly = generate_polynomial(encoded_flag)
    print(poly)

if __name__ == '__main__':
    main()
