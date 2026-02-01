import random
import math


def uniform_minus1_1(rng: random.Random) -> float:
    """Sample uniformly from [-1, 1]."""
    return 2 * rng.random() - 1


def generate_point(rng: random.Random) -> tuple[float, float]:
    """Generate one point (x, y) uniformly in [-1,1]^2."""
    return uniform_minus1_1(rng), uniform_minus1_1(rng)


def error_scale_pi(N: int) -> float:
    """Monte Carlo error scale ~ 4/sqrt(N) for the pi estimator."""
    return 4 / math.sqrt(N)


def estimate_pi_running(N: int, step: int = 1000, seed: int | None = None) -> None:
    """Print running Monte Carlo estimates of pi."""
    rng = random.Random(seed)
    inside = 0

    for k in range(1, N + 1):
        x, y = generate_point(rng)
        if x * x + y * y <= 1:
            inside += 1

        if k % step == 0:
            pi_hat = 4 * inside / k
            err = error_scale_pi(k)
            print(f"k={k:7d}  pi_hat={pi_hat:.6f}  err~{err:.6f}")


if __name__ == "__main__":
    estimate_pi_running(N=100_000, step=5_000, seed=42)
