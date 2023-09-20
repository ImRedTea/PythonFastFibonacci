
def binarypow(a, n):
    b = type(a)(a)
    while n > 1:
        if n % 2 == 1:
            b *= a
        a = a * a
        n //= 2
    b *= a
    return b
