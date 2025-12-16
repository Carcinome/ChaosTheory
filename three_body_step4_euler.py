import math


# --------------------------
# VECTORIAL 2D TOOLS
# --------------------------

def vec_add(a, b):
    """
    Addition of two 2D vectors.
    Example: (1, 2) + (3, 4) = (4, 6)
    """
    return a[0] + b[0], a[1] + b[1]

def vec_sub(a, b):
    """
    Substraction of two 2D vectors.
    Example: (3, 4) - (1, 2) = (2, 2)
    """
    return a[0] - b[0], a[1] - b[1]

def vec_mul(a, k):
    """
    Multiplication of a 2D vector by a scalar.
    Example: 2 * (1, 3) = (2, 6)
    """
    return a[0] * k, a[1] * k

def vec_norm(a):
    """
    Norm (length) of a 2D vector.
    |(x, y)| = sqrt(x² + y²)
    """
    return math.sqrt(a[0] * a[0] + a[1] * a[1])


# --------------------------
# GRAVITY : ACCELERATION
# --------------------------

def acceleration_on_i(i, positions, masses, G=1.0, softening=1e-2):
    """
    Calculate acceleration on body 'i' caused by all the other bodies.
    """
    # Total acceleration (initially zero).
    ax, ay = 0.0, 0.0

    # Position of 'i' body.
    pi = positions[i]

    # Check all bodies.
    for j in range(len(positions)):
        if j ==i:
            continue

        # J body position.
        pj = positions[j]

        # Direction vector 'i -> j'.
        r = vec_sub(pj, pi)

        # Distance between 'i' and 'j'.
        dist = vec_norm(r)

        # Softening to avoid dist = 0.
        dist_soft = math.sqrt(dist * dist + softening * softening)

        # Newton's vectorial law.
        factor = G * masses[j] / (dist_soft **3)

        # 'j' contribution to 'i' acceleration.
        ax += r[0] * factor
        ay += r[1] * factor

    return ax, ay