from lib import invmod

class RSA:
    def __init__(self, p, q, e):
        phi = (p - 1) * (q - 1)

        self.n = p * q
        self.e = e
        self.d = invmod(e, phi)

    def encrypt(self, m):
        return pow(m, self.e, self.n)

    def decrypt(self, t):
        return pow(t, self.d, self.n)

if __name__ == '__main__':
    p = 199
    q = 443
    e = 7
    rsa = RSA(p, q, e)

    message = 104
    message_encrypted = rsa.encrypt(104)
    print(f"{message} encrypted to {message_encrypted}")
    print(f"{message_encrypted} encrypted to {rsa.decrypt(message_encrypted)}")
