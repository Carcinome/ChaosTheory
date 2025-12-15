import math

def vec_sub(a, b):
    return a[0] - b[0], a[1] - b[1]

def vec_norm(a):
    return math.sqrt(a[0] * a[0] + a[1] * a[1])

def acceleration_from_j_to_i(pi, pj, mj, G=1.0, softening=1e-2):
    """
    acceleration taken by i (position pi) from j (position pj, masse mj).
    """
    r = vec_sub(pj, pi)
    dist = vec_norm(r)

    dist_soft = math.sqrt(dist * dist + softening * softening)

    # G * mj * r /dist³
    factor = G * mj / (dist_soft**3)
    return r[0] * factor, r[1] * factor


def main():
    pi = (0.0, 0.0)
    pj = (1.0, 0.0)
    mj = 2.0

    ax, ay = acceleration_from_j_to_i(pi, pj, mj)
    print("a =", (ax, ay))


if __name__ == "__main__":
    main()
