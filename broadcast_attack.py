from functools import reduce
from simple_rsa import RSA

def mul_inv(a, b):
    b0 = b
    x0 = 0
    x1 = 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

p1 = 31013
q1 = 72431
p2 = 31193
q2 = 74357
p3 = 32507
q3 = 75707

e = 3

rsa1 = RSA(p1, q1, e)
rsa2 = RSA(p2, q2, e)
rsa3 = RSA(p3, q3, e)

m = 10000

cipher1 = rsa1.encrypt(m)
cipher2 = rsa2.encrypt(m)
cipher3 = rsa3.encrypt(m)

print(cipher1, cipher2, cipher3)

n = [rsa1.n, rsa2.n, rsa3.n]
a = [cipher1, cipher2, cipher3]
print(chinese_remainder(n, a))
