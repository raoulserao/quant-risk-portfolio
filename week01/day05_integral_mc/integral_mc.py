import random
import math


def square(x: float) -> float:
    """Square of x."""
    return x * x


def uniform_0_1(rng: random.Random) -> float:
    """Sample uniformly from [0, 1]."""
    return rng.random()


def sample_uniform_01(rng: random.Random) -> float:
    """Generate one sample uniformly in [0,1]."""
    return uniform_0_1(rng)


def error_scale_integral(N: int) -> float:
    """Monte Carlo error scale ~ 1/sqrt(N) for the integral estimator."""
    return 1 / math.sqrt(N)


def estimate_integral_running(N: int, step: int = 1000, seed: int | None = None) -> None:
    """Print running Monte Carlo estimates of the integral of x^2 on [0,1]."""
    rng = random.Random(seed)
    value = 0.0

    for k in range(1, N + 1):
        x = sample_uniform_01(rng)
        value += square(x)

        if k % step == 0:
            integral_hat = value / k
            err = error_scale_integral(k)
            print(f"k={k:7d}  integral={integral_hat:.6f}  err~{err:.6f}")


if __name__ == "__main__":
    estimate_integral_running(N=100_000, step=5_000, seed=42)
    print("Exact value = 1/3")
