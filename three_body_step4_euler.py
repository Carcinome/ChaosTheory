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


# --------------------------
# EULER INTEGRATION
# --------------------------

def euler_step(positions, velocities, masses, dt):
    """
    Make one step of Euler method integration.

    positions: tuple list (x, y)
    velocities: tuple list (vx, vy)
    masses: list of masses
    dt: time step
    """
    new_positions = []
    new_velocities = []

    # We treat all bodies one by one.
    for i in range(len(positions)):
        # Actual acceleration.
        acc = acceleration_on_i(i, positions, masses)

        # New velocity.
        # v(t + dt) = v(t) + a(t) * dt
        v_next = vec_add(
            velocities[1],
            vec_mul(acc, dt)
        )

        # New position.
        # p(t + dt) = p(t) + v(t) * dt
        p_next = vec_add(
            positions[1],
            vec_mul(velocities[1], dt)
        )

        new_velocities.append(v_next)
        new_positions.append(p_next)

    return new_positions, new_velocities


# --------------------------
# PRINCIPAL PROGRAM
# --------------------------

def main():
    # Masses of three bodies.
    masses = [ 1.0, 1.0, 1.0]

    # Initial positions.
    positions = [
        (-1.0, 0.0),
        (1.0, 0.0),
        (0.0, 0.8),
    ]

    # Initial velocities.
    velocities = [
        (0.3, 0.2),
        (-0.3, 0.2),
        (0.0, -0.4),
    ]

    # Time step.
    dt = 0.01

    # Number of iterations.
    steps = 10

    print("Initial statement: ")
    for i in range(3):
        print(f"Body {i}: pos={positions[i]}, vel={velocities[i]}")

    print("\nEvolution: \n")

    # Time loop.
    for step in range(steps):
        positions, velocities = euler_step(
            positions, velocities, masses, dt
        )

        print(f"After {steps + 1} steps: ")
        for i in range(3):
            print(f"Body {i}: pos={positions[i]}, vel={velocities[i]}")
        print()

if __name__ == "__main__":
    main()