import sys
from pathlib import Path 

sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.pricing.black_scholes import (call_price, vega)

S = 100
K = 100
T = 1
r = 0.05
sigma = 0.2         

h = 0.01
price_up = call_price(S, K, T, r, sigma + h)
price_down = call_price(S, K, T, r, sigma - h)
numerical_vega = (price_up - price_down) / (2 * h)
analytic_vega = vega(S, K, T, r, sigma)

print(f"Numerical Vega: {numerical_vega:.6f}")
print(f"Analytic Vega: {analytic_vega:.6f}")