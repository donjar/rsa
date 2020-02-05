from lib import invmod
from simple_rsa import RSA

def decrypt(rsa, ciphertext):
    new_ciphertext = (ciphertext * pow(2, rsa.e)) % rsa.n
    return (rsa.decrypt(new_ciphertext) * invmod(2, rsa.n)) % rsa.n

p = 31013
q = 72431

rsa = RSA(p, q, 65537)

m = 123456
ciphertext = rsa.encrypt(m)
print(decrypt(rsa, ciphertext))
