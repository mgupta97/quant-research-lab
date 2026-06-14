from src.pricing.black_scholes import (
    call_delta,
    gamma,
)

S = 100
K = 100
T = 1
r = 0.05
sigma = 0.2

h = 0.01

delta_up = call_delta(
    S + h,
    K,
    T,
    r,
    sigma,
)

delta_down = call_delta(
    S - h,
    K,
    T,
    r,
    sigma,
)

numerical_gamma = (
    delta_up - delta_down
) / (2 * h)

analytic_gamma = gamma(
    S,
    K,
    T,
    r,
    sigma,
)

print(
    f"Numerical Gamma: {numerical_gamma:.6f}"
)

print(
    f"Analytic Gamma : {analytic_gamma:.6f}"
)