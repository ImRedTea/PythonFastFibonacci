
def binarypow(a, n):
    b = []
    while n > 1:
        if (n % 2 == 1):
            b.append(a)
        a *= a
        n /= 2
    for i in b:
        a *= i
    return a