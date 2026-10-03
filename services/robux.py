def calculate_robux_price(robux: int, rate_per_1000: float) -> float:
    if robux <= 0 or rate_per_1000 <= 0:
        raise ValueError("Robux and rate must be positive")
    return round((robux / 1000) * rate_per_1000, 2)
