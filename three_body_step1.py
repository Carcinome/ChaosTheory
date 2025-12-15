import math

def vec_add(a, b):
    """Two vectors added together: (ax, ay) + (bx, by)."""
    return a[0] + b[0], a[1] + b[1]

def vec_sub(a,b):
    """subtract two vectors: (ax, ay) - (bx, by)."""
    return a[0] - b[0], a[1] - b[1]

def vec_mul(a, k):
    """Scalar multiplication: k * (ax, ay)."""
    return a[0] * k, a[1] * k

def vec_norm(a):
    """Length (norm) of a vector: sqrt(x² + y²)."""
    return math.sqrt(a[0] * a[0] + a[1] * a[1])


def main():
    a = (3.0, 4.0)
    b = (1.0, 2.0)

    print("a + b =", vec_add(a, b))
    print("a - b =", vec_sub(a, b))
    print("2 * a =", vec_mul(a, 2.0))
    print("|a|   =", vec_norm(a))


if __name__ == "__main__":
    main()

