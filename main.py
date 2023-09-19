import Pow
import Matrix

def fibonaccinnum(n: int):
    a = Matrix.Matrix2x2(0, 1, 1, 1)
    b = Matrix.Matrix2x1(0, 1)
    return (b * Pow.binarypow(a, n)).a1


if __name__ == "__main__":
    for i in range(1, 100):
        print(i, fibonaccinnum(i))
