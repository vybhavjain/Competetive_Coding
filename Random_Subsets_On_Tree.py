def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

t = int(input())
s = modinv(pow(2,t),1000000007)
s1 = (pow(2,t) - 1)*s 
print(s1%1000000007)
