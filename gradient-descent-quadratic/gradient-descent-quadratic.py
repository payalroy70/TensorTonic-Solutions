def gradient_descent_quadratic(a: float, b: float, c: float, x0: float, lr: float, steps: int) -> float:
    """
    Returns the final scalar x after the requested iterations.
    """
    x = x0          # start here

    for _ in range(steps):
        gradient = 2 * a * x + b
        x = x - lr * gradient  # move from current x
    
    return float(x)
    