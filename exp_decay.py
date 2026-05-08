import math
from typing import List

def exp_decay(t: float = 0.0, decay_factor: float = 0.0, initial_n: float = 1.0) -> float:
    """Return the remaining amount after time `t` for exponential decay."""
    return initial_n * math.exp(-decay_factor * t)


def get_decay_factor(tn: float, current_n: float, initial_n: float) -> float:
    """Compute the decay constant k from an initial amount and a measurement at time `tn`."""
    if tn <= 0 or initial_n <= 0 or current_n <= 0:
        raise ValueError("values must be positive")
    return math.log(initial_n / current_n) / tn


def tabulate(time_range: int, initial_n: float, tn: float, current_n: float, precision: int = 3):
    """Return a sorted list of (time, amount) for the decay model over a time range."""
    
    decay_factor = get_decay_factor(tn, current_n, initial_n)
    table: List[List[float, float]] = [
        [float(i) for i in range(time_range + 1)],
        [round(exp_decay(i, decay_factor, initial_n), precision) for i in range(time_range + 1)]
    ]

    print(
        f"Using initial amount {initial_n}, known amount {current_n} at t={tn},"
        f" decay factor {decay_factor:.4f}, results for {time_range} days"
    )
    return table

