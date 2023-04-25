#!/usr/bin/env python
# CRC32 tools by Victor

permitted_characters = set(
    map(ord, 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890_'))  # \w


def get_poly():
    poly = 0xEDB88320
    check32(poly)
    return poly


table = []
table_reverse = []


def init_tables(poly, reverse=True):
    global table, table_reverse
    table = []
    # build CRC32 table
    for i in range(256):
        for j in range(8):
            if i & 1:
                i >>= 1
                i ^= poly
            else:
                i >>= 1
        table.append(i)
    assert len(table) == 256, "table is wrong size"
    # build reverse table
    if reverse:
        table_reverse = []
        found_none = set()
        found_multiple = set()
        for i in range(256):
            found = []
            for j in range(256):
                if table[j] >> 24 == i:
                    found.append(j)
            table_reverse.append(tuple(found))
            if not found:
                found_none.add(i)
            elif len(found) > 1:
                found_multiple.add(i)
        assert len(table_reverse) == 256, "reverse table is wrong size"
        if found_multiple:
            print('WARNING: Multiple table entries have an MSB in {0}'.format(
                rangess(found_multiple)))
        if found_none:
            print('ERROR: no MSB in the table equals bytes in {0}'.format(
                rangess(found_none)))


def calc(data, accum=0):
    accum = ~accum
    for b in data:
        accum = table[(accum ^ b) & 0xFF] ^ ((accum >> 8) & 0x00FFFFFF)
    accum = ~accum
    return accum & 0xFFFFFFFF


def findReverse(desired, accum):
    solutions = set()
    accum = ~accum
    stack = [(~desired,)]
    while stack:
        node = stack.pop()
        for j in table_reverse[(node[0] >> 24) & 0xFF]:
            if len(node) == 4:
                a = accum
                data = []
                node = node[1:] + (j,)
                for i in range(3, -1, -1):
                    data.append((a ^ node[i]) & 0xFF)
                    a >>= 8
                    a ^= table[node[i]]
                solutions.add(tuple(data))
            else:
                stack.append(((node[0] ^ table[j]) << 8,) + node[1:] + (j,))
    return solutions


def reverseBits(x):
    # http://graphics.stanford.edu/~seander/bithacks.html#ReverseParallel
    # http://stackoverflow.com/a/20918545
    x = ((x & 0x55555555) << 1) | ((x & 0xAAAAAAAA) >> 1)
    x = ((x & 0x33333333) << 2) | ((x & 0xCCCCCCCC) >> 2)
    x = ((x & 0x0F0F0F0F) << 4) | ((x & 0xF0F0F0F0) >> 4)
    x = ((x & 0x00FF00FF) << 8) | ((x & 0xFF00FF00) >> 8)
    x = ((x & 0x0000FFFF) << 16) | ((x & 0xFFFF0000) >> 16)
    return x & 0xFFFFFFFF

# Compatibility with Python 2.6 and earlier.
if hasattr(int, "bit_length"):
    def bit_length(num):
        return num.bit_length()
else:
    def bit_length(n):
        if n == 0:
            return 0
        bits = -32
        m = 0
        while n:
            m = n
            n >>= 32
            bits += 32
        while m:
            m >>= 1
            bits += 1
        return bits


def check32(poly):
    if poly & 0x80000000 == 0:
        print('WARNING: polynomial degree ({0}) != 32'.format(bit_length(poly)))
        print('         instead, try')
        print('         0x{0:08x} (reversed/lsbit-first)'.format(poly | 0x80000000))
        print('         0x{0:08x} (normal/msbit-first)'.format(reverseBits(poly | 0x80000000)))


import itertools


def ranges(i):
    for kg in itertools.groupby(enumerate(i), lambda x: x[1] - x[0]):
        g = list(kg[1])
        yield g[0][1], g[-1][1]


def rangess(i):
    return ', '.join(map(lambda x: '[{0},{1}]'.format(*x), ranges(i)))

def reverse_crc32(desired: int):
    # initialize tables
    init_tables(get_poly())
    # find reverse bytes
    accum = 0

    l = []

    for i in permitted_characters:
        for j in permitted_characters:
            patch = (i,j)
            patches = findReverse(desired, calc(patch, accum))
            for last_4_bytes in patches:
                if all(p in permitted_characters for p in last_4_bytes):
                    patch2 = patch + last_4_bytes
                    if calc(patch2, accum) == desired: # sanity check
                        l.append(''.join(map(chr, patch2)))

    return l