# e.g. hex(17) is 0x11. We need to truncate the '0x'
def int_to_hex(i):
    return hex(i)[2:]

def str_to_int(string):
    return int(''.join([int_to_hex(ord(c)) for c in string]), 16)

def int_to_str(number):
    hex_repr = int_to_hex(number)
    if len(hex_repr) % 2 != 0:
        hex_repr = '0' + hex_repr

    res = ''
    for i in range(0, len(hex_repr), 2):
        res += chr(int(hex_repr[i:i + 2], 16))

    return res

print(hex(str_to_int('abc')))
print(int_to_str(0x616263))
