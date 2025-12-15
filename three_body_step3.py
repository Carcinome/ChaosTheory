import math


def vec_add(a, b):
    return a[0] + b[0], a[1] + b[1]

def vec_sub(a, b):
    return a[0] - b[0], a[1] - b[1]

def vec_norm(a):
    return math.sqrt(a[0] * a[0] + a[1] * a[1])


def acceleration_on_i(i, positions, masses, G=1.0, softening=1e-2):
    """
    Acceleration taken by i, for all the other bodies.
    """
    ax, ay = 0.0, 0.0
    pi = positions[i]

    for j in range(len(positions)):
        if j == i:
            continue

        pj = positions[j]
        r = vec_sub(pj, pi)
        dist = vec_norm(r)
        dist_soft = math.sqrt(dist * dist + softening * softening)

        factor = G * masses[j] / (dist_soft ** 3)
        ax += r[0] * factor
        ay += r[1] * factor

    return ax, ay


def main():
    masses = [1.0, 1.0, 1.0]
    positions = [
        (-1.0, 0.0),
        (1.0, 0.0),
        (0.0, 1.0)
    ]

    print("a on 0 =", acceleration_on_i(0, positions, masses))
    print("a on 1 =", acceleration_on_i(1, positions, masses))
    print("a on 2 =", acceleration_on_i(2, positions, masses))


if __name__ == "__main__":
    main()
